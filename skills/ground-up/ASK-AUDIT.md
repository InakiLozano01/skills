# Ask audit

An **ask audit** checks, before you explain an ask, that only this reader can answer it. A clear message that asks something already settled still costs the reader an answer they do not have to give. The audit enforces **completed staff work**: whatever a later decision, the sources, or another person can answer never reaches the reader.

## Steps

1. **List.** Number every ask the text makes: each question, each "review", "confirm", or "mark what looks wrong", each request to another team, and each answer column or form in a page you link. Done when the list holds everything the text and its links ask of the reader.
2. **Hand off.** Start one subagent with a fresh context. Give it the list, the reader line from [COLD-READER.md](COLD-READER.md), and the paths or links to the sources: the decisions with their dates, the documents and data the asks refer to, and the code. Leave out your draft and reasoning. Send this brief:

   > You audit the asks below before they go to `<reader line>`. Read the sources. Assume every ask is unnecessary until a source proves otherwise. For each ask write one line, `N. VERDICT: evidence`, with a path, a date, or a count as evidence:
   > - SETTLED: a decision already answers it. When two decisions conflict, the later one holds. Name what it replaces.
   > - DERIVABLE: the sources answer it, or will once someone reads, compares, or counts them. Say how.
   > - RECHECK: it asks the reader to confirm what follows from rules or decisions they already gave.
   > - OWNER: someone else holds the answer. Name them.
   > - OURS: the choice falls inside our own work. Give the reversible option. When the ask has another team change their system, say which local alternative was measured on real data and how many cases it leaves open.
   > - NEEDED: only this reader can answer, and the answer changes what we do next. Say what it changes.
   >
   > `<asks>`

   Done when the subagent has answered and you have saved its answer to a file.
3. **Act.** Apply every verdict. For SETTLED, apply the later decision and tell the user what it replaces. For DERIVABLE, derive the answer or start the work that does. For OWNER, route the ask to that person or drop it. For OURS, take the reversible option and record it as an assumption. Remove from the text and its linked pages every ask that is not NEEDED. When no ask survives, send no message and tell the user why. Run `check_draft.py --asks <answer file>`. Done when the script exits 0, meaning each question left in the text has its own NEEDED line.

When you cannot start a subagent, write the verdicts yourself from the sources, and say in the note to the user that you audited the asks yourself.

<example>
Before the audit: `"¿Medimos con la política de octubre o con esa política más las 19 reglas que cerraste con Tomás? Acepta o corrige cada fila. En el caso 06, ¿cuáles son los seis controles?"`
After the audit: the later rules answer the first ask (SETTLED). The rows follow from those rules (RECHECK). The analyst's sheet and the stored run hold the six controls (DERIVABLE). No message goes out.
</example>
