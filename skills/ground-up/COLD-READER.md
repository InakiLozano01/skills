# Cold reader

A **cold reader** is a reader with fresh eyes: someone who gets only the text, exactly as the real reader will. You wrote the draft, so you cannot unknow what you know; the cold reader can. Their **teach-back** shows the gap between what the text says and what you meant.

## Steps

1. **Hand off.** Start one subagent with a fresh context, on the strongest model you can choose (another model family when you have one). Give it only two things: the copyable block (or the whole text when there is no block) and one reader line in this shape: `"<name>, <role>; already knows <systems, names, decisions they own>; does not know <what this message reports>"`. Keep the material, the conversation, and your intent out of the brief. Send this brief, with the placeholders filled:

   > You are `<reader line>`. You received the message below and know nothing else about the work. Answer in at most twelve lines, and quote the text wherever a question asks for it:
   > 1. Teach it back: what the writer asks you to do or decide, by when, and what you would tell the people you report to.
   > 2. Copy the opening's claim word for word, with every count, date, and scope. Then list each item the body covers, one line each, and mark every place where the two disagree.
   > 3. Quote each sentence or gloss that tells you, as this reader, something you already know, and each sentence that repeats an earlier one.
   > 4. Quote each sentence or name you could not follow, and each pair of sentences that cannot both be true.
   > 5. Name what you expected to find, given the ask, and did not find.
   >
   > `<message>`

   Done when the subagent has answered.
2. **Compare.** Set its answer beside your intent: the ask, the date, and the one thing the reader must take away. Compare its body list (answer 2) with every item you gathered, and its answer 5 with what you meant to cover. Check each quote in answer 3 against the reader's common ground before you cut it. Done when every difference is listed.
3. **Fix.** Close each difference in the draft: make the opening the summary of the body, cut what the reader already knows, ground or drop what they could not follow, add what was missing. Run `check_draft.py` again. Done when the script exits 0 and the teach-back matches your intent. Run the hand-off once more only when a fix changed the ask or the opening.

When you cannot start a subagent, answer the five questions yourself as the reader, from the block alone, before comparing, and say in the note to the user that the cold read was done by the writer.
