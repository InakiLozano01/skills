# Progress report

A **progress report** serves a reader whose ask is `track`: a milestone update, a periodic report, or a reply to `"how much is left to close X?"` (`¿cuánto falta?`, `¿qué ya está y qué falta?`). It applies every rule in [SKILL.md](SKILL.md) and adds the structure below.

Anchor the report in the product and the concrete problem each piece solves. When the request references a spec, feedback document, or checklist, use the **traceability matrix** from `Gather` so every item in that document is accounted for. The spec and acceptance criteria are the measure; the code, PRs, and tests are the evidence. When the material has no written acceptance criteria, measure against the behaviour the work is meant to deliver, and state that no written criteria exist yet.

Present the implementation as a **deep module**: expose product behaviours and their verification state as the interface, and compress internal git mechanics (merge conflicts, worktrees, cherry-picks, subagent dispatches) into one plain phrase such as `"implemented and being split into smaller changes for review"`.

## Two sizes (both open with a BLUF and use bullets inside the copyable message)

### 1. Full progress report (for a stage, milestone, or periodic update)

Format the report in five sections with bullets inside each one:

1. **Executive summary — BLUF (`Resumen ejecutivo`)**: 2–4 bullets in plain words, with zero unglossed internal names. State what already works and where it was verified, how the parts connect today, and what remains before users or the business can use the result.
2. **Context and scope (`Contexto`)**:
   - What the system or product does, in one sentence from grounded prerequisites.
   - What the **global task** is, and which slice of that task this update covers.
   - The main repositories or components involved, with an **appositive gloss** for each one's role.
3. **What advanced (`Qué avanzó`)**: one bullet per **capability or problem solved**, built ground up inside:
   - Open with a short capability label.
   - State the concrete mechanism and failure case it handles through a specific scenario (for example, what happens when version 2 of a document arrives while version 1 is active, or when a queue delivery fails and retries).
   - Attach an appositive gloss to any internal term on its first use.
   - State the certainty and where it was verified (`main`, a PR branch, a local test with synthetic data, a simulated provider, or a deployed environment), together with what still lacks connection.
   - For an **engineering** or **user** reader, place the PR or ticket URL/number at the end of the bullet as evidence. For a **domain** or **no-background** reader, include only facts that change the scope, a risk, or a date.
4. **How it converges and what comes next (`Cómo converge y qué sigue`)**:
   - How the pieces in flight come together (such as an integration branch or an end-to-end test between services).
   - The next concrete steps in order.
   - What users or `main` still experience today (for example, endpoints that return unavailable until the full flow is verified).
5. **Asks, doubts, and dependencies (`Pedidos, dudas y dependencias`)**:
   - Every decision, approval, or action needed from the reader or another person, naming who owns each one. When a decision requires weighing options, shape it as in [DECISION-REQUEST.md](DECISION-REQUEST.md).
   - Open items, **documenting the null**: name the external sources or environments that could not be checked in the session and what they are needed for.

### 2. Compact status reply (for `"¿cuánto falta?"` / `"what is done and what is left in document X?"`)

When the user asks what to reply to a narrower question about how much is left to finish a document, spec, or feedback list, format a compact copyable reply with a **BLUF headline** and **state-bucket bullets**:

1. **BLUF headline and partition count** (1–2 lines): state the direct answer in plain words and give the exact item counts from your **traceability matrix** across state buckets (for example, `"De los 18 puntos del documento de feedback, 8 ya están integrados en la rama principal (main), 7 ya tienen código escrito que estamos revisando por partes, y 3 esperan definición de Operaciones o pruebas finales"`), noting whether production verification is still pending.
2. **State buckets in bullets (`•`)**, writing each item as a complete clause with subject, verb, and concrete behaviour:
   - **Already integrated (`Ya resuelto en main`)**: bullets naming the concrete behaviours that work today and where they were verified (`main`, local tests, or production).
   - **In review or integration (`En revisión e integración`)**: bullets naming the behaviours already coded in branches or PRs that are being reviewed, split, or developed in parallel, stated in plain words.
   - **Remaining or waiting on decisions (`Qué falta o requiere definición`)**: bullets separating what still requires engineering work or evaluation from what waits on a decision by a named owner (such as Compliance, Operations, or Product).
3. **Constructive ETA closing (`Cuándo podemos cerrarlo`)**: when asked for a date or `"hoy"`, state what **can** close today (such as updating the tracking document with each item's current status and open questions, or deploying the items already in `main`), and name the **concrete condition that unlocks the full estimate** (for example, `"cuando hoy terminen las revisiones de las primeras cuatro entregas y Operaciones confirme las reglas pendientes"`).

## Slack and thread format

When the report is meant to be pasted into Slack or chat, or when the user asks for a thread (`:thread:` / hilo):

- Place the recipient-facing message **first**, inside copyable code blocks using plain-text headers and `•` bullets separated by blank lines so pasting into Slack preserves the layout. Place any operational notes for the user **after** the copyable block.
- When a thread is requested or standard for a full progress report, split the output into two copyable blocks:
  - **Message 1 (thread root)**:
    `:thread: <GENERAL TOPIC> - <specific report>`
    Followed by the `RESUMEN EJECUTIVO` (BLUF) bullets (`•`) and the tags/mentions for the people who need to read or act on it.
  - **Message 2 (thread reply)**:
    `CONTEXTO`, `QUÉ AVANZÓ`, `CÓMO CONVERGE Y QUÉ SIGUE`, and `PEDIDOS, DUDAS Y DEPENDENCIAS`, with `•` bullets and PR/ticket URLs on their own lines under the relevant bullet.

When the user asks for a long document or a table-based status report directly in the chat, combine this structure with [LONG-TEXT.md](LONG-TEXT.md) using standard Markdown headings (`##`), bullets (`-`), and tables.

## Check

Done when every item below holds:

- All explorations and document comparisons finished before writing, and the **traceability matrix** accounts for every item of any referenced spec or feedback document.
- A full report contains all five sections; a compact `"¿cuánto falta?"` reply contains the BLUF headline with partition counts, the state buckets in `•` bullets, and the constructive ETA closing naming what closes today and what unlocks the final date.
- The BLUF / Executive summary uses plain words with zero unglossed internal names and states whether the work is available to users yet.
- Every bullet states a complete clause with concrete mechanism and behaviour, passes the portability test, and names its certainty and where it was verified.
- Merged code, deployed code, and code verified in an environment are distinguished explicitly, and internal git mechanics stay compressed inside a deep-module phrase.
- For an engineering or user reader, PR or ticket links/numbers back every item that has them.
- Every blocker, ask, or Open item names who owns the answer and documents the null (which sources were checked).
- For Slack or copy-paste messages, the recipient's message appears first inside a copyable block with plain-text headers and `•` bullets.
