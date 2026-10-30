---
name: ground-up
description: Writes text an outsider can follow, in the reader's own language, for explanations, decision requests, progress reports, messages, and rewrites, in Spanish or English.
disable-model-invocation: true
---

Write so an **outsider** can follow the text from the first line. The outsider brings **prerequisite** general technical vocabulary (PR, API, package manager) and zero knowledge of this project's domain, internal names, abstractions, or history.

Four moves carry the skill:

- **Ground up**: every concept is **grounded** before a sentence leans on it. The outsider either brings it as a prerequisite or meets its explanation first. In a narrative text (`understand`), the whole piece runs from the domain basics to the subject, what is known, and what follows. In a structured text (`track` or `decide`), open with a **BLUF (Bottom Line Up Front)** in plain words, then build each section and each bullet ground up inside.
- **Appositive gloss**: keep every internal name as the source writes it, and on its first use attach a short appositive phrase that says what it is and what role it plays here (`"<name>, the <kind of thing> that <role in this case>, ..."`).
- **Certainty**: where it changes what the reader believes or does, state a claim's epistemic state inside the sentence so the reader can tell what is verified from what is inferred, in progress, planned, or open.
- **Concrete mechanism over vibes**: state the rule, the concrete case, the actor, and the measured number. Apply the **portability test**: if a sentence could move unchanged to another project's update or docs, replace it with the specific mechanism, scenario, or count from this project.

## Say only what the material supports

Every sentence traces to the material or to something you checked. A **gap** is a question the material leaves unanswered. Investigate each gap, or surface it as **Open** when it changes what the reader decides or does. Keep every claim within what the evidence proves. When the material skips the basics, start ground up from the facts it does provide.

A claim sits in one of five states. State the tier in plain words inside the sentence whenever it changes what the reader believes or does:

- **Verified**: checked. State how it was checked: a real case, a synthetic test, or reading the code, and in which branch or environment (`main`, a PR branch, local tests, or production).
- **Inferred**: deduced from a named fact, and unchecked. Include an inference only when the reader needs it to decide or act, and state what check would confirm it.
- **In progress**: started and partial. Name both what works today and what piece is still missing.
- **Planned**: decided or proposed, and unstarted. Name who decided or proposed it and whether it is approved.
- **Open**: unknown so far, or waiting on a decision. **Document the null**: name the specific sources you checked that returned nothing (for example, `"checked in main and open PRs, with the rule still open for Compliance to define"`), and name who owns the answer.

Before stating that a capability is missing or unstarted, check the main branch (`main` or `origin/main`).

## Size the text to the question

The question sets the scope. Give a narrow question a narrow answer: a question about a few names gets an appositive gloss for each and why each matters here. Explaining one decision takes a few paragraphs. When explaining a decision already made, state the chosen option and its consequence, and add one sentence on a rejected option only when it clarifies that consequence.

## Know the reader

Read two things from the request and the material: the **reader context** and the **ask**. If the material leaves the reader context ambiguous, ask the user one question before writing.

The **reader context** is the **bounded context** the reader works in. Write in its **ubiquitous language**, using the words that reader already uses for their own work:

- **Domain**: the reader owns the business, such as a client or a product lead. Their language is rules, cases, people, money, and dates. Present the implementation as a **deep module**: expose a small interface (the business rule, a concrete scenario, the consequence, and the cost) and keep code, components, branch topology, merge conflicts, and PRs inside the module. Mention a technical fact only when it changes what they decide or when they get it.
- **Engineering**: the reader owns technical decisions, such as a technical lead. Their language is contracts, data shapes, modules, risk, and cost. Tie every technical point to its product consequence: what changes for users or the business, and what failure or edge case each piece prevents. Compress git mechanics (worktrees, cherry-picks, rebases) into one plain phrase unless the reader must act on them.
- **No background**: the reader knows nothing of the work, such as someone from another team. Start from the most basic domain premise and gloss every project term.
- **User**: the person in the chat, who wants to understand something themselves. Write in their context, usually engineering. When the subject will reach another reader, add that reader's lens: what changes for them, in their language, and what they will ask.

The **ask** is what the text needs from the reader, which selects the mode and reference file:

- **Decide**: the reader must choose between options. Read [DECISION-REQUEST.md](DECISION-REQUEST.md) and [EXAMPLE.md](EXAMPLE.md).
- **Track**: the reader follows where the work stands or asks how much is left (`¿cuánto falta?`, `¿qué ya está y qué falta?`). Read [PROGRESS.md](PROGRESS.md) and [EXAMPLE.md](EXAMPLE.md).
- **Understand**: the reader needs to know how something works or why it is built that way. Write narrative prose. When the text is a long document, report, or onboarding guide, read [LONG-TEXT.md](LONG-TEXT.md).

When the request points at an existing draft, answer, or report to improve, read [REWRITE.md](REWRITE.md) and [EXAMPLE.md](EXAMPLE.md).

For a reader other than the user, write the shortest text that lets that person understand and act. Place the copy-ready message for that recipient **first**, and put any operational notes for the user (such as branch state, subagents, or suggested glossary additions) in a brief note after the block.

## Steps

1. **Gather.** Read the primary sources behind the topic: the conversation, the code, `main`, open PRs, docs, tickets, and any connected knowledge base. Wait for all running explorations and subagents to finish before writing the reply. When the request references a spec, feedback document, or checklist, build a complete **traceability matrix** mapping every item in that document to its current repository state (`main`, in an open PR or branch, unstarted, or waiting on an external decision). List the **prerequisite** concepts the outsider brings and every **introduced** concept and internal name the text will need (components, task codes, domain words, people, acronyms). Done when all explorations have returned, every item in any referenced document is mapped to its state, and every internal name on the list has an appositive gloss backed by a source or is marked Open with the searched sources named.
2. **Order.** Pick the structure that matches the ask:
   - **Narrative (`understand`)**: order the whole text from grounded prerequisites and domain basics, to the subject or problem, its certainty, the decision or mechanism, and the consequence.
   - **Structured (`track` or `decide`)**: follow [PROGRESS.md](PROGRESS.md) or [DECISION-REQUEST.md](DECISION-REQUEST.md). Open with a **BLUF** in plain words so the opening needs no internal glosses, then build each section and each bullet ground up inside (the concrete behaviour or problem first, then the mechanism with its appositive glosses, its certainty, and its evidence).
   Done when every concept in the outline appears after the sentence that grounds it.
3. **Write.** Draft the text following the writing rules below and the rules of any disclosed file you loaded (`PROGRESS.md`, `DECISION-REQUEST.md`, `LONG-TEXT.md`, or `REWRITE.md`). Done when the full draft is written.
4. **Check.** Reread the draft top to bottom as the outsider. The draft is done when all of these hold, together with the check list of each disclosed file you loaded:
   - The draft answers the question asked, at the size the question calls for, after all explorations completed.
   - Every concept is grounded before use, and every internal name carries an appositive gloss on its first use. Any BLUF or executive summary uses plain words with zero unglossed internal names.
   - Every multi-item bullet states each item as a complete clause with actor, verb, and concrete behaviour or case.
   - Every sentence passes the portability test, names concrete mechanisms over vibes, and traces to a checked source or states its tier (`Verified`, `Inferred`, `In progress`, `Planned`, or `Open` with the null documented).
   - Every claim about current state names where it was checked, including `main`.
   - The text speaks the ubiquitous language of the reader context, keeps implementation mechanics inside a deep module for domain readers, and ties technical points to product consequences for engineering readers.
   - Every identifier follows the identifier rule, and the prose obeys the ASD-STE100 and clean-prose rules below.
   - Format matches the ask and channel, and for third-party messages the copyable block for the recipient appears first.

   Fix any check that fails and run the check again before delivering.

## Writing rules

### Appositive glosses and concrete clauses

- Gloss every internal name on first use: components, repositories, task codes, products, domain words, and people (with their role). Keep public names and prerequisite technical vocabulary as they are.
- Write each gloss as an **appositive gloss** inside the sentence where the term first appears: `"<name>, the <kind of thing> that <role in this case>, ..."`.
- Keep proper names, domain terms, and identifiers verbatim as the source writes them, so the reader recognizes them in the code, the board, or a meeting.
- When summarizing several items from a document, spec, or backlog, write each item as a complete clause with subject, verb, and concrete behaviour in plain words (for example, `"calcular cuándo vence el poder de cada representante y qué combinación de firmas exige"`), replacing compressed shorthand labels.
- If the repository has a glossary (`GLOSSARY.md`, `GLOSSARY-MAP.md`, or a glossary under `docs/`), take glosses from it first. After the text, in a short note to the user, propose any new terms you glossed that the glossary lacks.
- Make the thing itself the grammatical subject of the sentence, and treat its identifier (task code, ticket, PR number, state, flag, field, or file name) as evidence. For an engineering or user reader, place the identifier or PR/ticket URL in parentheses or at the end of the item. For a domain or no-background reader, include an identifier only when that person will look for it on a shared board, and say where they will find it.

### ASD-STE100 and clean prose (`unslop`)

Write in **ASD-STE100 Simplified Technical English** (without its fixed dictionary) combined with clean, unslopped prose:

- **One thought per sentence**, with most sentences under 25 words. Vary sentence lengths deliberately so short sentences land a point and longer sentences carry a condition and its consequence.
- **One name per thing**, used everywhere, and one meaning per word.
- **Active voice**: name the actor and the action (`"the worker retries the job"`, `"Compliance defines the threshold"`).
- **Direct verbs and plain words**: use `"use"`, `"help"`, `"is"`, and `"has"` in place of AI vocabulary (`"utilize"`, `"leverage"`, `"facilitate"`, `"delve"`, `"crucial"`, `"pivotal"`, `"serves as"`).
- **Whole clauses over trailing participles**: state consequences with a finite verb (`"so users can..."` or `"which prevents..."`) instead of superficial `-ing` tails (`"highlighting..."`, `"ensuring..."`, `"fostering..."`).
- **Clean punctuation**: use periods, commas, and parentheses. Use a colon only to introduce a list or a label, and write full sentences instead of mid-sentence colon reveals (`"The key detail: ..."` -> state the sentence directly) or em dashes (`—`).

### Format, language, and tone

- Match the format to the ask: connected paragraphs of prose for explanations (`understand`), the structured sections and `•` bullets of [PROGRESS.md](PROGRESS.md) for status updates and `"how much is left?"` replies (`track`), and the prose setup plus option bullets and numbered questions of [DECISION-REQUEST.md](DECISION-REQUEST.md) for decisions (`decide`).
- Use a numbered list for an ordered sequence or numbered questions. Use bullets for parallel items the reader scans or acts on.
- When the output is a message to paste into Slack or chat, deliver the recipient's message first inside a copyable code block using plain-text headers and `•` bullets separated by blank lines.
- Write in the language of the request unless the user asks for another. Use a neutral, professional register. In Spanish, use neutral Spanish and address the reader as `"tú"`.
