---
name: ground-up
description: Writes text an outsider can follow, in the reader's own language, for explanations, decision requests, progress reports, messages, and rewrites, in Spanish or English.
disable-model-invocation: true
---

Every text this skill fixes failed the same way: the **curse of knowledge**. The writer knows the work so well that they cannot imagine a reader who does not. Every rule below serves one purpose: this reader understands and acts with the fewest words. Apply a rule where it serves that purpose; `scripts/check_draft.py` holds the mechanical lines.

Measure the text against the reader's **common ground**: what this reader and you already share. Say as much as this reader needs, and no more. A reader who owns the system already holds its names, so spend the words on what you found. When you do not know the reader, write for an outsider: general technical vocabulary (PR, API) and nothing of this project's domain, names, or history.

- **Ground up**: ground every concept before a sentence leans on it. Each sentence opens with what the reader holds and ends on what is new.
- **Appositive gloss**: keep each name as the source writes it. When the reader needs a name outside their common ground, say on first use what it is and what role it plays here (`"<name>, the <kind of thing> that <role>, ..."`), using only what a source says. Leave out names the reader does not need, and leave names they own bare.
- **BLUF**: a structured text opens with its bottom line in plain words. Write it last, as the summary of the body, with every count, date, and exception the body holds, so it stays true for a reader who reads nothing else.
- **Certainty**: where a claim changes what the reader believes or does, say in the sentence how sure it is. Verified: say how and where you checked (a real case, a test, the code, and which branch or environment). Inferred: name the fact it rests on; an estimate built from the team's estimates or the calendar is an inference the reader needs, so give it as a range with its assumption. In progress: what works and what is missing. Planned: who decided it. Open: the sources you checked that came back empty, and the one person who owns the answer. Check `main` before you call something missing.
- **Show, don't tell**: show the rule, the case, the actor, and the number. A sentence that could move unchanged into another project's update, or that changes nothing for this reader, gets replaced by the concrete case or cut.
- **Backstage**: the reader sees the result. Your searches, tools, subagents, session failures, and git mechanics stay backstage, and so do this skill's own terms: the reader gets the plain thing each one names. Bring a backstage fact on stage only when it changes what the reader decides, does, or when they get it.

## Know the reader and the ask

Write in the words the reader uses for their own work. When the reader is unclear, pick the likeliest one, write for them, and name them in the note to the user; ask first only when a different reader would change the whole text.

- **Domain** (a client, a product lead): rules, cases, people, money, dates. Code, branches, and PRs stay backstage.
- **Engineering** (a tech lead): contracts, data, risk, cost. Tie each technical point to what changes for users or the business.
- **No background** (another team): start from the most basic domain premise and gloss every project term.
- **User** (the person in the chat): usually engineering; when the text will reach someone else, add what changes for that reader.

The ask picks the shape. To **decide**, read [DECISION-REQUEST.md](DECISION-REQUEST.md). To **track** where work stands or how much is left (`¿cuánto falta?`), read [PROGRESS.md](PROGRESS.md). To **understand** how or why, write narrative prose, and read [LONG-TEXT.md](LONG-TEXT.md) for a long document. To improve an existing text, read [REWRITE.md](REWRITE.md). [EXAMPLE.md](EXAMPLE.md) shows each shape and the short contrasts of common failures. The question sets the size: a narrow question gets a narrow answer.

## Steps

1. **Gather.** Read the sources behind the topic (conversation, code, `main`, open PRs, docs, tickets) and wait for every exploration to return. List what the reader already holds and each name the text needs from outside it, taking glosses from the repo's glossary when it has one. Done when every claim you will make has a source or a certainty, and every name outside the reader's common ground has a gloss from a source or is out of the text.
2. **Order.** A narrative runs from what the reader holds to the problem, what is known, and what follows. A structured text follows its file: BLUF first, then each section ground up. Done when every concept appears after the sentence that grounds it.
3. **Write.** Write clean on the first pass, in the voice below. Done when the draft is complete.
4. **Check.** For a text meant for anyone but the user, run the **cold reader** in [COLD-READER.md](COLD-READER.md). Run `python3 scripts/check_draft.py <draft>` from this skill's folder (`--decide` for a decision request, `--original <file>` for a rewrite, plus `--owner` when the reader owns the system) and fix every `ERROR`. Done when the script exits 0, the cold reader's teach-back matches your intent, the check list of the file you loaded holds, and:
   - the BLUF states the body, count for count, and every count equals the items that follow;
   - names the reader owns stay bare, and every gloss comes from a source;
   - the text is the size the question calls for;
   - the copyable block for another reader comes first, with notes for the user after it (open items, the reader you assumed, glossary terms to add).

## Voice and language

Write in **classic style**: one colleague showing another something real. People and systems are the subjects, their actions are the verbs, and each sentence picks up what the last one left, so the text reads as one argument. Keep it tight, not terse: trim words, never items, and keep the articles and connectives of speech. Write each listed item as a full clause with its actor, verb, and behaviour (`"calcular cuándo vence cada poder"`), in place of a shorthand label. A sentence that follows every rule and still sounds machine-written has failed; fix it another way. Use one name per thing, periods, commas, and parentheses.

Write in the language of the request. In Spanish, use neutral Spanish with "tú", and Spanish verbs for the work (`integrar`, `desplegar`, `tomar`), keeping English only for names the team uses as names (`main`, `PR`). Identifiers are evidence: for an engineering reader, put the PR or ticket in parentheses or at the end; for a domain reader, only when they will look for it, saying where. A message to paste into Slack goes in a copyable code block with plain-text headers and `•` bullets.
