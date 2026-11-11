# Progress report

A **progress report** serves a reader whose ask is `track`: a milestone update, a periodic report, or a reply to "how much is left?" (`¿cuánto falta?`). It adds the structure below to the rules in [SKILL.md](SKILL.md).

## Gather

When the request points at a spec, a feedback document, or a checklist, build a **traceability matrix**: one row per item of that document with its state today (in production, in `main`, in an open PR, unstarted, or waiting on a decision). The document's items and acceptance criteria are the measure; code, PRs, and tests are the evidence. With no written criteria, measure against the behaviour the work is meant to deliver, and say that none are written. Done when every item of the document has a row and every exploration has returned.

## Shape

Pick the size the question asks for.

**Compact reply**, for "how much is left?" or "what is done and what is missing?":

1. The BLUF with the **partition count**: the direct answer and the exact count per state (`"De los 18 puntos, 8 están en producción, 7 en revisión y 3 esperan una definición de Operaciones"`).
2. One group of bullets per state. Each bullet is one row of the matrix as a full clause: the behaviour, where it was verified, and, for what is waiting, the person who owns the decision. A count never replaces the list.
3. The closing answers "when?" with a number even when nobody has committed to a date: an **Inferred** range placed on the **cone of uncertainty**, with its assumption (`"entre el jueves 5 y el martes 10 de noviembre, si Operaciones confirma las reglas esta semana"`), what can close today, and the event that narrows the range.

**Full report**, for a milestone or a periodic update, in five sections:

1. Summary, the BLUF: what works and where it was verified, and what is left before users can use it.
2. Context: what the product does, the whole task, and the slice this report covers.
3. What advanced: one bullet per capability or problem solved, shown through a concrete case, with its certainty and where it was verified.
4. How it converges and what comes next: how the pieces in flight come together, the next steps in order, and what users still see today.
5. Asks and dependencies: each one with the person who owns it. Shape a real choice as in [DECISION-REQUEST.md](DECISION-REQUEST.md).

Keep "integrated", "deployed", and "verified in an environment" apart: they are three states. Git mechanics stay backstage behind one plain phrase (`"implementado y en revisión por partes"`). When the user asks for a thread, write two copyable blocks: the root with the summary and the people who must act, and the reply with the other sections.

## Check

Done when every item below holds:

- The cold reader can say what is done, what is left, and the date range.
- Every row of the traceability matrix appears as an item.
- A compact reply closes with a date range, its assumption, what closes today, and the event that narrows the range.
- Every ask and every open item names the person who owns it.
