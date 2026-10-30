# Progress report

A **progress report** tells a reader whose ask is `track` where the work stands, or answers a status question such as "how much is left to close X?" (`¿cuánto falta?`, `¿qué ya está y qué falta?`). It keeps every rule in [SKILL.md](SKILL.md) and adds these.

Anchor the report in the product and the problem each piece solves. The spec, feedback document, and acceptance criteria are the measure, and the code, PRs, and tests are evidence. When the material has no written acceptance criteria, measure against the behaviour the work was meant to deliver, and say that no criteria are written.

Treat the implementation as a **deep module**: show the reader the product behaviours and their verification state as the interface, and keep internal git mechanics (merge conflicts, worktrees, cherry-picks, subagent dispatches) out of the message—or compressed into one plain phrase such as "implemented and being split into smaller changes for review".

## Two sizes (both use bullets inside the copyable message)

### 1. Full progress report (for a stage, milestone, or periodic update)

Use these five sections, with bullets inside each one:

1. **Executive summary** (`Resumen ejecutivo`): 2–4 bullets in plain words, with no unglossed internal names. State what already works and where it was tested, how the parts connect today, and what remains before users or the business can use the result.
2. **Context and scope** (`Contexto`):
   - What the system or product does, in one sentence from zero.
   - What the **global task** is, and which slice of that task this update addresses.
   - The main repositories or components involved, with a gloss for each one's role.
3. **What advanced** (`Qué avanzó`): one bullet per **capability or problem solved**, never a bare list of files or PRs. Build each bullet ground up inside:
   - Open with a short capability label.
   - Explain what problem or failure case it handles, using a concrete scenario (for example, what happens when version 2 of a document arrives while version 1 is active, or when a queue delivery fails and retries).
   - Gloss any internal term on its first use.
   - State the certainty and where it was verified (`main`, a PR branch, a local test with synthetic data, a simulated provider, or a deployed environment), and what still lacks connection.
   - For an **engineering** or **user** reader, include the PR or ticket URL/number at the end of the bullet as evidence. For a **domain** or **no-background** reader, leave PR numbers and code details out unless they change the scope, a risk, or a date.
4. **How it converges and what comes next** (`Cómo converge y qué sigue`):
   - How the pieces in flight come together (such as an integration branch or a first end-to-end test between services).
   - The next concrete steps in order.
   - What users or the main branch still see today (for example, endpoints that still return unavailable until the full flow is verified).
5. **Asks, doubts, and dependencies** (`Pedidos, dudas y dependencias`):
   - Any decision, approval, or action needed from the reader or another person, naming who owns each one. If a decision needs options and trade-offs, shape it as in [DECISION-REQUEST.md](DECISION-REQUEST.md).
   - Open doubts, unverified assumptions, or external sources (such as a plan or board) that could not be checked in the session.

### 2. Compact status reply (for "¿cuánto falta?" / "what is done and what is left in document X?")

When the user asks what to reply to a narrower question about how much is left to finish a document, spec, or feedback list, write a compact copyable reply using bullets (never a multi-paragraph wall of prose):

1. **Headline and partition count** (1–2 lines): state the direct answer in plain words and, when the work tracks a document or checklist, give the real counts across state buckets (for example: "De los 18 puntos del documento de feedback: 8 ya están integrados en `main`, 4 ya están resueltos en código y se están separando para revisión, y 6 siguen en desarrollo o esperan definición de Compliance").
2. **State buckets in bullets** (`•`):
   - **Already integrated (`Ya resuelto en main`)**: bullets naming the concrete behaviours that now work and where they were checked (for example, `main`, local tests, or production).
   - **In review or integration (`En revisión / integrándose`)**: bullets naming the behaviours already coded in branches or PRs that are being reviewed or split, stating each behaviour in plain words.
   - **Remaining or waiting on decisions (`Qué falta o requiere definición`)**: bullets separating what still needs engineering work/evaluation from what waits on a decision by a named owner (such as Compliance or Product).
3. **When asked for a date or ETA (`¿cuánto falta?` / `¿llegamos hoy?`)**: if you cannot give a reliable time, say why in one plain clause, name the **concrete condition that unlocks the estimate** (for example, "cuando terminen las revisiones de las primeras entregas hoy" or "cuando Compliance confirme las reglas pendientes"), and state what **can** be closed today (such as updating the document with each item's current status or deploying the items already in `main`).

## Slack and thread format

When the report is meant to be sent on Slack or chat, or when the user asks for a thread (`:thread:` / hilo):

- Deliver the recipient-facing message **first**, inside copyable code blocks using plain-text headers and `•` bullets separated by blank lines so pasting into Slack never breaks the formatting. Put any operational notes for the user (such as subagents running or branch details) **after** the copyable block.
- When a thread is requested or standard for a full progress report, split the output into two copyable blocks:
  - **Message 1 (thread root)**:
    `:thread: <GENERAL TOPIC> - <specific report>`
    Followed by the Executive summary bullets (`•`) and the tags/mentions for the people who need to read or act on it.
  - **Message 2 (thread reply)**:
    `CONTEXTO`, `QUÉ AVANZÓ`, `CÓMO CONVERGE Y QUÉ SIGUE`, and `PEDIDOS, DUDAS Y DEPENDENCIAS`, with `•` bullets and PR/ticket URLs on their own lines under the relevant bullet.

When the user asks for a long document or a table-based status report in the chat (not a message to paste into Slack), you may combine this structure with [LONG-TEXT.md](LONG-TEXT.md) using standard Markdown headings (`##`), bullets (`-`), and tables.

## Check

- All explorations and document comparisons finished before writing; every item of a referenced spec or feedback document is accounted for.
- A full report has all five parts; a compact "¿cuánto falta?" reply has the headline with bucket counts, the state buckets in `•` bullets, and the condition that unlocks the ETA plus what can close today.
- The Executive summary or headline contains no unglossed internal names and states whether the work is available to users yet.
- Every bullet describes a concrete capability or problem in plain words, never a telegraphic list of internal labels, and states its certainty and where it was verified.
- Merged code, deployed code, and code verified in an environment are distinguished explicitly; internal git mechanics stay behind a deep-module phrase.
- For an engineering or user reader, PR or ticket links/numbers back the items that have them.
- Every blocker, ask, or dependency names who can unblock or answer it.
- If the output is for Slack or a copy-paste message, the recipient's message comes first inside a copyable block with plain-text headers and `•` bullets.
