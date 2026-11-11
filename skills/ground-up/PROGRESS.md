# Progress report

A **progress report** serves a reader whose ask is `track`: a milestone update, a periodic report, or a reply to "how much is left?" (`¿cuánto falta?`). It adds the structure below to the rules in [SKILL.md](SKILL.md).

## Gather

When the request points at a spec, a feedback document, or a checklist, build a **traceability matrix**, with one row per item of that document and its state today (in production, in `main`, in an open PR, unstarted, or waiting on a decision). The document's items and acceptance criteria are the measure; code, PRs, and tests are the evidence. With no written criteria, measure against the behaviour the work is meant to deliver, and say that none are written. Done when every item of the document has a row and every exploration has returned.

## Shape

Pick the size the question asks for.

**Compact reply**, for "how much is left?" or "what is done and what is missing?":

1. The BLUF with the **partition count**, which is the direct answer and the exact count per state (`"De los 18 puntos, 8 están en producción, 7 en revisión y 3 esperan una definición de Operaciones"`).
2. One group of bullets per state. Each bullet is one row of the matrix as a full clause: the behaviour, where it was verified, and, for what is waiting, the person who owns the decision. A count never replaces the list.
3. The closing answers "when?" with a number even when nobody has committed to a date. Give an **Inferred** range placed on the **cone of uncertainty**, with its assumption (`"entre el jueves 5 y el martes 10 de noviembre, si Operaciones confirma las reglas esta semana"`). Then say what can close today and which event narrows the range.

**Full report**, for a milestone or a periodic update, in five sections:

1. The summary, which is the BLUF, says what works and where it was verified, and what is left before users can use it.
2. The context says what the product does, what the whole task is, and which slice this report covers.
3. "What advanced" has one bullet per capability or problem solved, shown through a concrete case, with its certainty and where it was verified.
4. "How it converges and what comes next" says how the unfinished pieces come together, the next steps in order, and what users still see today.
5. "Asks and dependencies" lists each one with the person who owns it. Shape a real choice as in [DECISION-REQUEST.md](DECISION-REQUEST.md).

Keep "integrated", "deployed", and "verified in an environment" apart, because they are three different states. Git mechanics stay backstage behind one plain phrase (`"implementado y en revisión por partes"`). When the user asks for a thread, write two copyable blocks: the root with the summary and the people who must act, and the reply with the other sections.

## Check

Done when every item below holds:

- The cold reader can say what is done, what is left, and the date range.
- Every row of the traceability matrix appears as an item.
- A compact reply closes with a date range, its assumption, what closes today, and the event that narrows the range.
- Every ask and every open item names the person who owns it.
