# Rewrite

The request points at an existing text: an earlier answer, a draft, or a report. A **rewrite** applies every rule in [SKILL.md](SKILL.md) and adds the constraints below.

Before writing, count the words of the original. **Edit by exception**: keep each sentence that already serves this reader, change only the sentences that fail them, and add only what this reader lacks.

The **word budget** depends on the reader, unless the user asks for a different length:

- **A reader who owns the system** (their common ground holds the names): the original length. Run `check_draft.py --original <file> --owner`; it fails above 1.2x.
- **Any other reader**: up to 1.5x, spent on the glosses and domain basics this reader lacks. Run `check_draft.py --original <file>`; it fails above 1.5x.

- Preserve the original's headings, structure, tables, and diagrams unless the user asks to restructure them (such as turning a prose status update into the structured bullets of [PROGRESS.md](PROGRESS.md)).
- Place each appositive gloss inside the existing sentence, and weave missing domain basics into the existing paragraphs.
- Bring in a fact from elsewhere in the material only when the passage requires it to be understood.
- After the text, list what stayed **Open**, limited to items that change what the reader decides or does, **documenting the null** for each one. The Open list counts toward the word budget.

The short contrasts at the end of [EXAMPLE.md](EXAMPLE.md) show the two rewrite failures to look for: glossing names the reader owns, and glossing what no source explains.

## Check

Done when every item below holds:

- The script passes the word budget for this reader (`--owner` for a reader who owns the system), counting the Open list. If it fails, tighten sentences and recount.
- Every item of the original is still there: the budget trims words, never items, and a count never replaces a list.
- The original structure, tables, and diagrams are preserved (unless the ask changed the format).
- Every addition is an appositive gloss, a grounded basic the reader needed, or a documented Open item.
