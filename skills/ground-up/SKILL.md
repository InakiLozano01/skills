---
name: ground-up
description: Writes a clear explanation, decision, status update, action request, or rewrite for the reader's actual background, in Spanish or English.
disable-model-invocation: true
---

Use the smallest shape that answers the ask. Think with these leading words:

- **Common ground** is what this reader and you already share.
- **Ground up** starts each sentence with that ground and adds one new fact, the given-new order.
- **Certainty** separates verified facts, inferences, work in progress, plans, and open questions.
- **BLUF** puts the answer, count, date, and consequence first in a structured text.
- **Completed staff work** settles what the material lets you settle, then gives the reader one clear choice or action.
- **Cold reader** checks what a person without your context can teach back.

Write the reader's language. Keep project names when the reader needs them, and gloss each unfamiliar name with its kind and role on first use. Use concrete actors and verbs. Keep the working process, skill terms, and internal labels in notes unless they change what the reader decides or does. Give estimates as ranges with their assumptions and the event that narrows them.

The ask chooses the branch. Read [DECISION-REQUEST.md](DECISION-REQUEST.md) for a choice, [ACTION-REQUEST.md](ACTION-REQUEST.md) for something to do or send, [PROGRESS.md](PROGRESS.md) for status or remaining work, [LONG-TEXT.md](LONG-TEXT.md) for a long explanation, and [REWRITE.md](REWRITE.md) for an existing text.

1. **Gather.** Read the sources behind the topic. Identify the reader's common ground, the claims you can support, and the names the reader needs. Done when every claim has a source or a stated certainty.
2. **Order.** Put each concept after the sentence that makes it understandable. Put the BLUF first in a structured text. Done when the opening remains true if the reader reads nothing else.
3. **Write.** Match the size to the ask. Use the reader's language, whole sentences, one name per thing, and plain punctuation. Done when the draft carries every item the reader must know or act on.
4. **Check.** For another reader, run [COLD-READER.md](COLD-READER.md) and save its teach-back. Run `python3 scripts/check_draft.py --cold <answer> <draft>` from this folder (`--for-user` for a reply to the user, `--original <file>` for a rewrite, and `--owner` when the reader owns the system). Fix every error. Done when the check passes, the teach-back matches, counts match their lists, and the copyable block comes before notes for the user.

Write in the request's language. In Spanish, use neutral Spanish with "tú" and Spanish verbs for the work, while keeping names such as `main` and `PR`. A message to paste uses a copyable block with plain-text headings and `•` bullets. Use absolute dates. Keep the result human and direct. If a rule makes the prose sound mechanical, rewrite the sentence until it sounds like one colleague explaining something real.
