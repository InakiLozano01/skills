---
name: ground-up
description: Writes text an outsider can follow, in the reader's own language: explanations, decision requests, progress reports, messages, and rewrites, in Spanish or English.
disable-model-invocation: true
---

Write so an **outsider** can follow the text from the first line. The outsider knows general technical vocabulary (PR, API, package manager) and nothing of this project's domain, internal names, abstractions, or history.

Three moves carry the skill:

- **Ground up**: every concept appears after its explanation. In a narrative text, the whole piece runs from the basics to the subject, what is known, and what follows. In a structured text, such as a progress report, an executive summary in plain words can open the piece, and each section or bullet goes ground up inside.
- **Gloss**: keep every internal name as it is, and on its first use add a short phrase that says what it is and what role it plays here.
- **Certainty**: where it changes what the reader believes or does, a claim shows its state, so the reader can tell what is proven from what is believed, planned, or unknown.

## Say only what the material supports

Every sentence comes from the material or from something you checked. A **gap** is something the material does not answer. Investigate each gap, or name it as Open when the reader needs it. A plausible sentence written to fill a gap is a fabrication, and so is a known fact reshaped to cover it. When the material does not explain the basics, start ground up from what it does say.

A claim has one of five states. Show the state where it changes what the reader believes or does, as plain words inside the sentence. A fact that comes straight from the material is stated plainly.

- **Verified**: checked. When the reader might doubt it, say how: a real case, a test with synthetic data, or reading the code.
- **Inferred**: deduced from a fact the text names, and unchecked. Include an inference only when the reader needs it to decide or act, and say what would confirm it.
- **In progress**: started and partial. Say what exists and what is missing.
- **Planned**: decided or proposed, and unstarted. Say who decided or who proposes, and whether it is approved. A rule the material calls decided and not implemented stays decided and not implemented.
- **Open**: unknown so far, or waiting on a decision. Name an Open item only when it changes what the reader decides or does. Name it where it arises and, when known, say who can answer it.

Say where each claim about the current state was checked: a working branch, the main branch, or an environment. Before you write that something does not exist yet, check the main branch too (`main` or `origin/main`).

## Size the text to the question

The question sets the scope. A narrow question gets a narrow answer: a question about a few names gets a gloss for each and why each matters here. Explaining one decision takes a few paragraphs. When you explain a decision already made, focus on the chosen option and its consequence, and mention a rejected option in one sentence only when it explains that consequence.

## Know the reader

Two things about the reader shape the text. Read both from the request and the material. If the material does not settle the reader's context, ask the user one question before you write.

The **reader context** is the bounded context the reader works in. Write in its ubiquitous language: the words that reader already uses for their own work.

- **Domain**: the reader owns the business, such as a client or a product superior. Their language is rules, cases, people, money, and dates. Treat the implementation like a deep module: show the reader a small interface (the rule, concrete examples, the consequences, and the cost) and keep the code, components, and PRs out of sight. Bring in a technical fact only when it changes what they decide or when they get it.
- **Engineering**: the reader owns technical decisions, such as a technical superior. Their language is contracts, data, modules, risk, and cost. Tie every technical point to its product consequence: what changes for the users or the business, and what failure or edge case each piece prevents.
- **No background**: the reader knows nothing of the work, such as someone from another team. Gloss everything and start from the most basic part.
- **User**: the person in the chat, who wants to understand something themselves. Write in their context, usually engineering. When the subject will reach another reader, add that reader's lens: what changes for them, in their language, and what they are likely to ask.

The **ask** is what the text needs from the reader.

- **Decide**: the reader must choose. Read [DECISION-REQUEST.md](DECISION-REQUEST.md), then [EXAMPLE.md](EXAMPLE.md), which shows a decision request and a progress report before and after these rules.
- **Track**: the reader follows where the work stands. Read [PROGRESS.md](PROGRESS.md) and [EXAMPLE.md](EXAMPLE.md).
- **Understand**: the reader needs to know how something works or why it is so.

For a reader other than the user, write the shortest text that lets that person understand and act. A message opens with one line that names the topic and what you need from the reader, in their language.

When the request points at an existing text, such as an earlier answer, a draft, or a report, read [REWRITE.md](REWRITE.md), and [EXAMPLE.md](EXAMPLE.md) when the text is full of internal names. When the user asks for a document, a report, an onboarding guide, or an explanation from zero, the text is long: read [LONG-TEXT.md](LONG-TEXT.md) too.

## Steps

1. **Gather.** Read the material behind the topic: the conversation, the code, docs, tickets, PRs, and any knowledge base the session can reach. List every internal name and term the text will need (components, task codes, domain words, people, acronyms) and every claim it will make. For each name, find what it is and what role it plays in this case. For each claim, find its certainty. Done when every name on the list has a gloss backed by a source, or is marked Open. An Open name appears in the text as an open question.
2. **Order.** Choose the shape that fits the ask:
   - **Narrative (`understand`)**: order the whole text from the basics of the domain, to the subject or problem, what is known and how certain it is, the decision or proposal, and the consequence and next step. Use only the parts the question needs.
   - **Structured (`track` or `decide`)**: follow [PROGRESS.md](PROGRESS.md) or [DECISION-REQUEST.md](DECISION-REQUEST.md). If the structure opens with an executive summary, keep internal names out of the summary so it needs no glosses; then order each section and each bullet ground up inside (the problem or behaviour first, then the mechanism with its glosses, its certainty, and its evidence).
   Done when every concept appears after its explanation.
3. **Write.** Apply the writing rules below.
4. **Check.** Reread the draft as the outsider, top to bottom. The draft is done only when all of these hold, plus the checks of each linked file you read:
   - The text answers the question asked, at the size the question calls for.
   - Every internal name has a gloss on its first use. If there is an executive summary, it uses plain words without unglossed internal names.
   - Every concept appears after its explanation, either across the narrative or inside its section and bullet.
   - Every sentence traces to the material or to something you checked, or is marked as inferred or Open. Domain terms and states match the material word for word.
   - Every claim about the current state says where it was checked, and every "not yet" was checked against the main branch.
   - Every claim whose state changes what the reader believes or does shows that state. Every Open item changes what the reader decides or does, and is named where it arises.
   - The text speaks the language of the reader context. For a domain reader, every technical fact left in changes what they decide or when they get it. For an engineering reader, every technical point names its product consequence and the problem it solves.
   - Every identifier follows the identifier rule.
   - Format matches the ask and channel: prose for explanations (`understand`), the structured sections and bullets of [PROGRESS.md](PROGRESS.md) for status updates (`track`), and copy-ready plain-text formatting when the output is a message to paste into Slack or chat.

   Fix each failure and check again. Then deliver in the chat, unless the user asks for a file or a destination.

## Writing rules

### Gloss names and terms

- Gloss every internal name: components, repositories, task codes, products, domain words, and people (with their role). Public names and general technical vocabulary go as they are.
- A gloss is one phrase, inside the sentence where the term first appears, with what the thing is and why it matters here: "`<name>`, the <kind of thing> that <role in this case>, …".
- Keep proper names, domain terms, and identifiers exactly as the source writes them, because the reader will meet them later in the code, the board, or a conversation.
- Replace jargon with plain words. Keep a technical term only when the reader will meet it in the material, and gloss it.
- If the repository has a glossary (`GLOSSARY.md`, a `GLOSSARY-MAP.md` that points to one, or a glossary under `docs/`), take glosses from it first. After the text, addressed to the user, propose the terms you glossed that it lacks. Leave the file as it is.
- An identifier is a task code, ticket, PR number, state, flag, field, or file name. Name the thing in plain words and make the thing the subject of the sentence. For the user or an engineering reader, place the identifier or PR/ticket URL in parentheses or at the end of the item as evidence, because they will check it in the repo or board. For a domain or no-background reader, add the identifier only when that person will look for it in a shared board, and say where they will find it.

### Write in ASD-STE100

Write in ASD-STE100 Simplified Technical English, without its controlled dictionary. Two of its rules need the most care:

- One idea per sentence, most sentences under about 25 words. Mix lengths so the text reads like a person explaining.
- One name per thing, used everywhere, and one meaning per word.

### Match the format to the ask and channel

- For **explanations (`understand`)** and short answers, write prose by default. Each paragraph picks up where the previous one ended, so the text reads as one account.
- For **progress reports and status updates (`track`)**, use the sections and bullets in [PROGRESS.md](PROGRESS.md) so the reader can scan the summary, what advanced, what comes next, and the asks.
- For **decision requests (`decide`)**, write the basics in prose and use bullets for the options and a numbered list for the final questions, as in [DECISION-REQUEST.md](DECISION-REQUEST.md).
- Use a numbered list for a real sequence, such as steps, stages, or numbered questions.
- Use bullets for parallel, independent items the reader scans or acts on, such as capabilities in a progress report, options in a decision, tasks per person, or acceptance criteria.
- When the user asks for a message to copy and paste into Slack or chat, deliver it inside a copyable code block using plain-text section headers and `•` bullets separated by blank lines so pasting never breaks the formatting. For documents or direct answers in the chat, use standard Markdown (`##`, `-`).

### Language and tone

- Write in the language of the request, unless the user names another one.
- Use a neutral, professional register. In Spanish, use neutral Spanish and address the reader as "tú": no voseo, no "usted", and no regional slang.
