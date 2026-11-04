# Agents

Skills live in `skills/<name>/`. Shared vocabulary lives in `GLOSSARY.md`; change a term there and in the skill in the same commit.

Run `python3 tests/ground-up/test_check_draft.py` before committing a change to `ground-up`. CI runs the same command.

## Rule table

When the operator corrects a `ground-up` output, add the rule here with what enforces it. A rule enforced only by prose that gets corrected again is a repeat: in the same change, move a mechanical rule (a token, a form, a number) up to the script, and turn a semantic rule (redundancy, contradiction, an invented gloss) into a cold-reader question plus a `fail-*` fixture. Each `fail-*` fixture is a real past output. `--allow RULE` demotes a rule to a warning when the user asked for that wording; say so in the note to the user.

| Rule | Enforced by |
|---|---|
| Spanish verbs for the work (`integrar`, `desplegar`, `tomar`), no Spanglish (`mergear`, `pickear`, `shippear`) | `check_draft.py` `[spanglish]` error; fixtures `fail-lena-2026-11-03`, `fail-fin-avances-0145` |
| Spanish with tú, no voseo | `check_draft.py` `[voseo]` error; fixtures `fail-fin-avances-0145`, `fail-crm-precios-374b` |
| No em or en dashes in prose | `check_draft.py` `[dash]` error; fixture `fail-fin-avances-0145` |
| Plain verbs over AI vocabulary | `check_draft.py` `[slop]` error |
| One question per numbered decision | `check_draft.py --decide` `[questions]` error; fixture `fail-lena-2026-11-03` |
| Backstage stays out of the reader's text | `check_draft.py` `[backstage]` error; fixture `fail-cargocheck-example-before`; judgment in `SKILL.md` "Backstage" |
| Gloss names outside the reader's common ground | `check_draft.py` `[name]` warning lists first uses; judgment in `SKILL.md` |
| Same phrase opening three or more lines is template, not prose | `check_draft.py` `[template]` warning; fixture `fail-lena-rewrite-out11` |
| Name a door only when it is one-way, or when reversibility is the reason to decide fast | `DECISION-REQUEST.md` Check (judgment); fixture `fail-lena-rewrite-out11` |
| The skill's vocabulary (door, BLUF, common ground) stays out of the reader's text | `check_draft.py` `[backstage]` error; fixtures `fail-lena-rewrite-out11`, `fail-lena-rewrite-terra-out11` |
| A one-way door's evidence and DRI go in your text, not as new questions | `DECISION-REQUEST.md` Shape (judgment); fixture `fail-lena-rewrite-terra-out11` |
| Rewrite word budget: ceiling 1.5x, aim at 1.0x when the reader shares the names | `check_draft.py --original` `[budget]` error above 1.5x, warning above 1.1x; fixture `fail-lena-rewrite-out11` |
| Each ask appears once (MECE), and asks are only what the reader alone can decide (completed staff work) | `DECISION-REQUEST.md` Check (judgment) |
| "How much is left / when" gets a number and a range | `PROGRESS.md` Check (judgment) |
| "When?" gets an inferred range, never a refusal | `check_draft.py` `[estimate]` error; fixtures `fail-romina-terra-out12`, `fail-fin-sin-recalculo-0145`; `PROGRESS.md` and `SKILL.md` Inferred tier |
| Number only the questions; blocks get headings | `check_draft.py` `[numbering]` error; fixture `fail-lena-rewrite-terra-out12` |
| Rules serve commander's intent, not a checklist to recite (no door questions, no "no responsible identified") | `SKILL.md` (judgment); fixtures `fail-lena-rewrite-terra-out11`, `fail-lena-rewrite-terra-out12` |
| Each option names a consequence its name does not already say | `check_draft.py` `[tautology]` error; fixtures `fail-lena-rewrite-terra-out12`, `fail-lena-rewrite-terra-out13`; `DECISION-REQUEST.md` Shape |
| The reader understands the ask without the writer's context | Cold reader subagent in `COLD-READER.md` (structure: a real context boundary); judgment on its restatement |
| Guess the reader and name the guess; ask only when the reader changes the whole text | `SKILL.md` Know the reader (judgment) |
| Gloss or drop: names the reader does not need leave the text | `SKILL.md` Gather criterion (judgment); `[name]` warning |
| Trim words, never items; absolute dates; bullets true when quoted alone | `REWRITE.md` and `PROGRESS.md` Check (judgment) |
| Rewrite for a reader who owns the system stays near the original length (edit by exception) | `check_draft.py --original --owner` `[budget]` error above 1.2x; fixture `fail-lena-rewrite-luna-out15` |
| The BLUF is the faithful summary of the body (pyramid; reverse outline) | Cold reader question 2; `SKILL.md` and `DECISION-REQUEST.md` Check; fixture `tests/out15/case6-deepseek.md` |
| Names the reader owns stay bare; glosses only from a source (quantity maxim) | Cold reader question 3; `SKILL.md` Appositive gloss; fixture `fail-lena-rewrite-luna-out15` |
| Options stated by what makes them distinguishable | `check_draft.py` `[tautology]` error; `DECISION-REQUEST.md` Shape |
| Announced counts equal the items that follow | `SKILL.md` Check (judgment) |
| BLUF first: the answer before the process | `SKILL.md` Check and `DECISION-REQUEST.md` / `PROGRESS.md` Check (judgment) |
| Every decision carries a recommendation, a date, and a DRI | `DECISION-REQUEST.md` Check (judgment) |
| Approved text stays clean | fixture `pass-fin-aprobado` must exit 0 |
