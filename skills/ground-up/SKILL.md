---
name: ground-up
description: Writes text an outsider can follow, in the reader's own language, for explanations, decision requests, progress reports, messages, and rewrites, in Spanish or English.
disable-model-invocation: true
---

Every text this skill fixes failed the same way: the **curse of knowledge**. The writer knows the work so well that they cannot imagine a reader who does not. Every rule below exists so that this reader understands and acts with the fewest words. Apply a rule where it serves that purpose. `scripts/check_draft.py` checks the mechanical rules.

Measure the text against the reader's **common ground**, which is what this reader and you already share. Say as much as this reader needs, and no more. A reader who owns the system already knows its names, so spend the words on what you found. When you do not know the reader, write for an outsider, who has general technical vocabulary (PR, API) and knows nothing of this project's domain, names, or history.

- **Ground up.** Ground every concept before a sentence depends on it. Each sentence opens with what the reader knows and ends on what is new.
- **Appositive gloss.** Keep each name as the source writes it. When the reader needs a name outside their common ground, say on first use what it is and what role it plays here (`"<name>, the <kind of thing> that <role>, ..."`), using only what a source says. Leave out names the reader does not need, and leave names they own bare.
- **BLUF.** A structured text opens with its bottom line in plain words. Write it last, as the summary of the body, with every count, date, and exception the body contains, so it stays true for a reader who reads nothing else.
- **Certainty.** Where a claim changes what the reader believes or does, say in the sentence how sure it is. For a verified claim, say how and where you checked (a real case, a test, the code, and which branch or environment). For an inferred claim, name the fact it rests on; an estimate built from the team's estimates or the calendar is an inference the reader needs, so give it as a range with its assumption. For work in progress, say what works and what is missing. For a plan, say who decided it. For an open item, name the sources you checked that came back empty and the one person who owns the answer. Check `main` before you call something missing.
- **Show, don't tell.** Show the rule, the case, the actor, and the number. A sentence that could move unchanged into another project's update, or that changes nothing for this reader, gets replaced by the concrete case or cut.
- **Backstage.** The reader sees the result. Your searches, tools, subagents, session failures, and git mechanics stay backstage. So do this skill's own terms, and the reader gets the plain thing each one names. Bring a backstage fact on stage only when it changes what the reader decides, does, or when they get it.

## Know the reader and the ask

Write in the words the reader uses for their own work. When the reader is unclear, pick the likeliest one, write for them, and name them in the note to the user; ask first only when a different reader would change the whole text.

- **Domain** (a client, a product lead). Write about rules, cases, people, money, and dates. Code, branches, and PRs stay backstage.
- **Engineering** (a tech lead). Write about contracts, data, risk, and cost, and tie each technical point to what changes for users or the business.
- **No background** (another team). Start from the most basic domain premise and gloss every project term.
- **User** (the person in the chat). Usually an engineering reader. When the text will reach someone else, add what changes for that reader.

The ask picks the shape. To **decide**, read [DECISION-REQUEST.md](DECISION-REQUEST.md). To **act** (do something or send you something), read [ACTION-REQUEST.md](ACTION-REQUEST.md). To **track** where work stands or how much is left (`¿cuánto falta?`), read [PROGRESS.md](PROGRESS.md). To **understand** how or why, write narrative prose, and read [LONG-TEXT.md](LONG-TEXT.md) for a long document. To improve an existing text, read [REWRITE.md](REWRITE.md). The question sets the size, so a narrow question gets a narrow answer.

## Steps

1. **Gather.** Read the sources behind the topic (conversation, code, `main`, open PRs, docs, tickets) and wait for every exploration to return. List what the reader already knows and each name the text needs from outside it, taking glosses from the repo's glossary when it has one. Done when every claim you will make has a source or a certainty, and every name outside the reader's common ground has a gloss from a source or is out of the text.
2. **Order.** A narrative runs from what the reader knows to the problem, what is known about it, and what follows. A structured text follows its file, with the BLUF first and each section ground up. Done when every concept appears after the sentence that grounds it.
3. **Write.** Write clean on the first pass, in the voice below. Done when the draft is complete.
4. **Check.** For a text meant for anyone but the user, run the **cold reader** in [COLD-READER.md](COLD-READER.md) and save its answer to a file; under 200 words, run it when a misread would cost the reader a decision. Run `python3 scripts/check_draft.py --cold <answer> <draft>` from this skill's folder (`--for-user` in place of `--cold` when the text is for the user, `--original <file>` for a rewrite, plus `--owner` when the reader owns the system) and fix every `ERROR`. Done when the script exits 0, the cold reader's teach-back matches your intent, the check list of the file you loaded holds, and:
   - the BLUF states the body, count for count, and every count equals the items that follow;
   - names the reader owns stay bare, and every gloss comes from a source;
   - the text is the size the question calls for, so a message to paste carries the ask and what this reader must act on, and reference detail moves behind a link or into the notes for the user;
   - the copyable block for another reader comes first, with notes for the user after it (open items, the reader you assumed, glossary terms to add).

## Voice and language

Write in **classic style**, as one colleague showing another something real. People and systems are the subjects, their actions are the verbs, and each sentence starts from what the previous one said, so the text reads as one argument. Keep it tight, not terse. Trim words, never items, and keep the articles and connectives of speech. Write each listed item as a full clause with its actor, verb, and behaviour (`"calcular cuándo vence cada poder"`), in place of a shorthand label. A sentence that follows every rule and still sounds machine-written has failed; fix it another way. Use one name per thing, periods, commas, and parentheses.

Write in the language of the request. In Spanish, use neutral Spanish with "tú", and Spanish verbs for the work (`integrar`, `desplegar`, `tomar`), keeping English only for names the team uses as names (`main`, `PR`). Identifiers are evidence. For an engineering reader, put the PR or ticket in parentheses or at the end. For a domain reader, include one only when they will look for it, and say where. A message to paste into Slack goes in a copyable code block with plain-text headers and `•` bullets; each bullet stays true when someone quotes it alone, and every date is an absolute date (`"el jueves 5 de noviembre"`).
