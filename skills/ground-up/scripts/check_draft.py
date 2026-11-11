#!/usr/bin/env python3
"""Check a ground-up draft for the mistakes agents keep repeating.

Usage: python3 check_draft.py (--cold ANSWER | --for-user) [--original ORIGINAL [--owner]] [--allow RULE,...] [FILE]

Reads stdin when FILE is omitted.
--cold: the file where you saved the cold reader's answer (COLD-READER.md). A text over 200 words fails without it.
--for-user: the text is for the person in this chat, so it needs no cold reader.
--original: measure the rewrite's word budget against ORIGINAL (1.5x ceiling).
--owner: the reader owns the system, so the budget ceiling is 1.2x.
--allow: demote the named rules to warnings; use it only when the user asked for that wording or that length.

A draft with no Markdown heading is a message to paste: it warns above 500 words and fails above 800.
A long document carries `#` headings and has no ceiling.

Errors (exit 1) are mechanical and always wrong in a ground-up text.
Warnings (exit 0) list spots to reread against the reader's common ground.
Each message names the fix. Add a rule here when a new repeat shows up.
"""

import argparse
import os
import re
import sys

# Spanish verbs built on English roots. Each entry: pattern, Spanish verb to use.
SPANGLISH = [
    (r"\bmerge[aáeéoó]\w*", "integrar / fusionar (`main` puede quedar como nombre)"),
    (r"\bpicke[aáeéoó]\w*", "tomar / elegir"),
    (r"\bship+e[aáeéoó]\w*", "publicar / entregar"),
    (r"\bdeploy[aáeéoó]\w*", "desplegar"),
    (r"\bpushe[aáeéoó]\w*", "subir"),
    (r"\bcommite[aáeéoó]\w*", "registrar el cambio / hacer commit"),
    (r"\bflagge[aáeéoó]\w*", "marcar"),
    (r"\blinke[aáeéoó]\w*", "enlazar / vincular"),
    (r"\btracke[aáeéoó]\w*", "seguir / registrar"),
    (r"\bsteered\b", "guiado / orientado"),
]

# Voseo forms. The skill writes Spanish with tú.
VOSEO = {
    "podés": "puedes", "tenés": "tienes", "querés": "quieres", "sabés": "sabes",
    "hacés": "haces", "decís": "dices", "venís": "vienes", "sos": "eres",
    "decidís": "decides", "necesitás": "necesitas", "preferís": "prefieres",
    "mirá": "mira", "fijate": "fíjate", "decime": "dime", "avisame": "avísame",
    "contame": "cuéntame", "dejame": "déjame", "pasame": "pásame",
    "usá": "usa", "corré": "corre", "seguí": "sigue", "completá": "completa",
    "confirmá": "confirma", "revisá": "revisa", "elegí": "elige", "probá": "prueba",
    "vos": "tú / ti",
}

# Vocabulary that marks text as machine-written. Each entry: phrase, plain fix.
SLOP = [
    (r"\butili[sz]e\w*", "use"), (r"\bleverag\w*", "use"), (r"\bdelv\w*", "look into"),
    (r"\bseamless\w*", "say what works"), (r"\bpivotal\b", "say why it matters"),
    (r"\bcrucial(es)?\b", "say why it matters"), (r"\bfacilitat\w*", "help"),
    (r"\bfoster\w*", "say the effect"), (r"\bserves as\b", "is"),
    (r"\bit'?s worth noting\b", "state the fact"), (r"\bin summary\b", "state the point"),
    (r"\bcabe (destacar|mencionar|señalar)\b", "di el hecho directamente"),
    (r"\bes importante (destacar|mencionar|señalar)\b", "di el hecho directamente"),
    (r"\bvale la pena (destacar|mencionar)\b", "di el hecho directamente"),
    (r"\ben resumen\b", "di la conclusión directamente"),
    (r"\bsin fisuras\b", "di qué funciona"), (r"\bpotenci(ar|a|amos)\b", "mejorar / ampliar"),
    (r"\baprovechar al máximo\b", "usar"),
]

# Backstage: the writer's process and git mechanics. The reader sees the result.
BACKSTAGE = [
    r"\bground-up\b", r"\bla skill\b", r"\bthe skill\b", r"\bsub-?agentes?\b",
    r"\bsubagents?\b", r"\bworktrees?\b", r"\bcherry-?picks?\b", r"\brebase\w*",
    r"\bmi notebook\b", r"\bmy laptop\b", r"\bproxy\b",
    # The skill's own vocabulary guides your thinking; the reader gets plain words.
    r"\bpuerta (de (un|dos) sentidos?|irreversible)\b", r"\b(one|two)-way door\b",
    r"\bbluf\b", r"\bcommon ground\b", r"\bappositive gloss\b", r"\bdocument the null\b",
    r"\bmece\b", r"\bstaff work\b", r"\btrabajo de estado mayor\b", r"\bcono de incertidumbre\b",
    r"\bcone of uncertainty\b", r"\bso-?what\b", r"\bread-aloud\b",
    r"\bquantity maxim\b", r"\bmáxima de cantidad\b", r"\bedit by exception\b", r"\breverse[- ]outline\b",
    r"\bteach-?back\b", r"\bsbar\b", r"\bpir[áa]mide de minto\b", r"\bminto\b", r"\bcold reader\b", r"\blector en frío\b",
]

# Internal-looking names: CODE-12, snake_case, dotted.ids, UPPER_SNAKE, `code`.
NAME = re.compile(
    r"`[^`]+`|\b[A-Z]{2,}[-_]?\d+\b|\b[a-z]+(?:_[a-z0-9]+)+\b|"
    r"\b[a-z]+(?:\.[a-z_]+){1,}\b|\b[A-Z]{2,}(?:_[A-Z0-9]+)+\b"
)


def strip_code(line):
    return re.sub(r"`[^`]*`|https?://\S+", " ", line)


def recipient_lines(text):
    """Line numbers of the reader's message: the fenced blocks when the draft has any, else every line."""
    lines, inside, fenced = set(), False, set()
    for n, raw in enumerate(text.splitlines(), 1):
        lines.add(n)
        if raw.strip().startswith("```"):
            inside = not inside
        elif inside:
            fenced.add(n)
    return fenced or lines


def check(text):
    errors, warnings = [], []
    seen_names = set()
    reader = recipient_lines(text)
    for n, raw in enumerate(text.splitlines(), 1):
        line = strip_code(raw)
        low = line.lower()
        if "—" in line or re.search(r"\s–\s", line):
            errors.append((n, "dash", "raya (— / –) en la prosa: usa punto, coma o paréntesis"))
        for pat, fix in SPANGLISH:
            for m in re.finditer(pat, low):
                errors.append((n, "spanglish", f"'{m.group(0)}': usa '{fix}'"))
        for word in re.findall(r"[a-záéíóúñ]+", low):
            if word in VOSEO:
                errors.append((n, "voseo", f"'{word}': escribe con tú ('{VOSEO[word]}')"))
        for pat, fix in SLOP:
            for m in re.finditer(pat, low):
                errors.append((n, "slop", f"'{m.group(0)}': {fix}"))
        for pat in BACKSTAGE:
            for m in re.finditer(pat, low):
                if n in reader:
                    errors.append((n, "backstage", f"'{m.group(0)}' es backstage: déjalo en la nota para el usuario o quítalo"))
        for m in NAME.finditer(raw):
            name = m.group(0).strip("`")
            if name not in seen_names and not name.startswith("http"):
                seen_names.add(name)
                warnings.append((n, "name", f"'{name}' primera aparición: si el lector ya lo conoce, déjalo así; si no lo necesita, quítalo; si lo necesita, glósalo solo con lo que diga la fuente"))

    # Refusing to estimate. "When?" gets a range with its assumption.
    for n, raw in enumerate(text.splitlines(), 1):
        low = strip_code(raw).lower()
        if n in reader and re.search(r"no hay (una )?fecha (fiable|confirmada)|(aún|todavía) no (tengo|hay) una estimación|sin recálculo|no recalculo|no (publiqué|tengo) un porcentaje|no reliable (estimate|date)", low):
            errors.append((n, "estimate", "negarse a estimar: da un rango con su supuesto y el evento que lo acota (cone of uncertainty)"))

    # Options that only restate their own name ("cerrarlo deja el PR sin integrar").
    taut = re.compile(r"\b[a-záéíóúñ]+(?:ar|er|ir)(?:lo|la|los|las)?\b[^.;:]{0,90};\s*[a-záéíóúñ]+(?:ar|er|ir)(?:lo|la|los|las)\b", re.I)
    for n, raw in enumerate(text.splitlines(), 1):
        if n in reader and taut.search(strip_code(raw)):
            errors.append((n, "tautology", "cada opción repite su nombre: di a quién afecta, qué cuesta o qué riesgo deja, o quita la oración"))

    # Two numbering schemes: "1)" block headings and "1." questions.
    if re.search(r"(?m)^\s*\d+\)\s", text) and re.search(r"(?m)^\s*\d+\.\s", text):
        errors.append((0, "numbering", "hay bloques '1)' y preguntas '1.': numera solo las preguntas y titula los bloques"))

    # Template phrasing: the same four-word opening on three or more lines.
    openings = {}
    for n, raw in enumerate(text.splitlines(), 1):
        words = re.findall(r"[a-záéíóúñü]+", strip_code(raw).lower())
        if len(words) >= 4:
            openings.setdefault(" ".join(words[:4]), []).append(n)
    for phrase, lines in openings.items():
        if len(lines) >= 3:
            warnings.append((lines[0], "template", f"'{phrase}...' abre {len(lines)} líneas: dilo una vez para el grupo o varía según el caso"))

    # One question per numbered block. A block runs to the next number or the next heading.
    head, asked = None, 0
    rows = text.splitlines() + ["# end"]
    for i, raw in enumerate(rows):
        start = re.match(r"\s*(\d+)[).]\s", raw)
        if start or is_heading(rows, i):
            if head and asked > 1:
                errors.append((0, "questions", f"el punto {head} hace {asked} preguntas: una pregunta por número"))
            head, asked = (start.group(1) if start else None), 0
        asked += raw.count("?")
    return errors, warnings


def is_heading(rows, i):
    """A Markdown heading, or a short unpunctuated line that stands alone after a blank line."""
    line = rows[i].strip()
    if line.startswith("#"):
        return True
    alone = i > 0 and not rows[i - 1].strip()
    return bool(alone and line and len(line.split()) <= 8 and not re.match(r"[•\-*\d]", line) and line[-1] not in ".?!;,")


def words(text):
    return len(re.findall(r"\S+", text))


def reader_text(text):
    """The reader's message: the fenced blocks when the draft has any, else the whole draft."""
    keep = recipient_lines(text)
    return "\n".join(raw for n, raw in enumerate(text.splitlines(), 1) if n in keep)


def check_size(text, rewrite):
    """A message to paste has a word budget. A rewrite is measured against its original instead."""
    body = reader_text(text)
    count = words(body)
    if rewrite or re.search(r"(?m)^#{1,6} ", body):
        return [], []
    fix = "deja el pedido y lo que este lector tiene que hacer, y lleva el detalle de consulta a un enlace o quítalo"
    if count > 800:
        return [(0, "size", f"mensaje de {count} palabras, el techo es 800: {fix}")], []
    if count > 500:
        return [], [(0, "size", f"mensaje de {count} palabras: sobre 500, {fix}")]
    return [], []


def check_cold(text, cold, for_user):
    """A text over 200 words for another reader needs the cold reader's saved answer."""
    if for_user or words(reader_text(text)) <= 200:
        return []
    if not cold:
        return [(0, "cold", "falta la lectura en frío: sigue COLD-READER.md, guarda la respuesta en un archivo y pasa --cold ARCHIVO; si el texto es para el usuario de este chat, pasa --for-user")]
    if not os.path.isfile(cold) or words(open(cold, encoding="utf-8").read()) < 20:
        return [(0, "cold", f"'{cold}' no contiene la respuesta de la lectura en frío: guarda ahí las cinco respuestas de COLD-READER.md")]
    return []


def main(argv):
    parser = argparse.ArgumentParser(usage=__doc__.split("Usage: ")[1].split("\n")[0])
    parser.add_argument("file", nargs="?")
    parser.add_argument("--cold")
    parser.add_argument("--for-user", action="store_true")
    parser.add_argument("--original")
    parser.add_argument("--owner", action="store_true")
    parser.add_argument("--allow", default="")
    parser.add_argument("--decide", action="store_true", help=argparse.SUPPRESS)  # accepted, no effect
    args = parser.parse_args(argv)
    text = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
    errors, warnings = check(text)
    size_errors, size_warnings = check_size(text, rewrite=bool(args.original))
    errors += size_errors + check_cold(text, args.cold, args.for_user)
    warnings += size_warnings
    if args.original:
        base = words(open(args.original, encoding="utf-8").read())
        ratio = words(text) / base
        msg = f"{words(text)} palabras contra {base} del original ({ratio:.2f}x)"
        if args.owner and ratio > 1.2:
            errors.append((0, "budget", msg + ": el lector conoce el sistema, edita por excepción y vuelve cerca del largo original"))
        elif ratio > 1.5:
            errors.append((0, "budget", msg + ": supera el techo de 1.5x, recorta"))
        elif ratio > 1.1:
            warnings.append((0, "budget", msg + ": agrega solo lo que este lector no tiene"))
    allowed = set(filter(None, args.allow.split(",")))
    warnings += [e for e in errors if e[1] in allowed]
    errors = [e for e in errors if e[1] not in allowed]
    for n, rule, msg in errors:
        print(f"ERROR line {n} [{rule}] {msg}")
    for n, rule, msg in warnings:
        print(f"warn  line {n} [{rule}] {msg}")
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
