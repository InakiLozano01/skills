# Ground-up research and audit

Research for the `ground-up` writing skill. The skill stays short; this file keeps the evidence and the design record out of the always-loaded core.

## Findings that change the design

**Use leading words, not a longer checklist.** Matt Pocock calls these *leading words*: short phrases that bring a larger learned method to mind. His writing-for-agents skill says to front-load the word in a pointer, repeat the token rather than a sentence, and delete instructions that do not change behavior. The current design therefore keeps six words in `SKILL.md` and leaves branch-specific vocabulary in the disclosed files. Matt's term is "leading word". *Leitwort* is the literary source term, not his attribution.

**Keep the core small and disclose by branch.** Matt's skill separates steps from reference and pushes branch-specific material behind pointers. Pstack's public README uses one entry mode, `poteto-mode`, which routes to playbooks and principles. The repo's 35-line, 650-word core limit is stricter than pstack's router because `ground-up` has one user-invoked entry point and does not need a general mode.

**Use outside checks for semantic claims.** Pstack's public material emphasizes verification and real artifacts, but its own skills do not provide a comparable test suite. `ground-up` keeps the stronger local design: mechanical checks in `check_draft.py`, real past outputs as fixtures, and a cold reader for claims about clarity. The remaining semantic risk is that a passing linter cannot prove the opening matches the body or that a gloss is sufficient.

**Write for shared understanding.** Cramton's study of thirteen dispersed teams identifies failures in retaining context, uneven information, interpreting salience, access speed, and the meaning of silence. ADP 6-0 treats shared understanding and clear intent as conditions for coordinated action. These findings support `common ground`, `given-new`, and a plain opening that says what the reader must know or do.

**Separate facts from inferences.** Flower's writer-based prose work and Pinker's explanation of the curse of knowledge support the reader-first move. The cone of uncertainty gives the progress branch a useful operational term: an estimate is a range whose width reflects what is known, with the assumption and the event that narrows it. `Certainty` is therefore a behavior rule, not a decorative label.

**Treat prompting effects as empirical.** The prompting-replication work and the persona study are reasons to distrust a single good run. A leading word can change the model's behavior, but the effect depends on model, prompt, and task. The skill therefore keeps a small regression suite, records real past failures, and treats an output comparison as evidence about that case rather than proof of a universal effect. A reader description should change what gets explained, not turn into a theatrical persona.

**Structure action requests around the listener's next move.** ADP 6-0's shared understanding and commander's intent, completed staff work, and SBAR all point to the same sequence: state the situation, supply only missing background, assess what it means, and ask for the action or decision. The branch file carries that detail; the core only routes to it.

## Candidate leading words

These are useful when the user asks for the corresponding behavior. They should enter the skill only when a fixture shows that the shorter word changes output.

| Word | Behavior it should cue | Source |
|---|---|---|
| `common ground` | Find what the reader already knows before adding context | Clark, Cramton, [Cramton 2001](https://doi.org/10.1287/orsc.12.3.346.10098) |
| `ground up` / `given-new` | Start each sentence from shared information and end on the new point | [Clark and Haviland](https://doi.org/10.1016/S0022-5371(77)80008-X) and Flower, [Writer-Based Prose](https://doi.org/10.58680/ce197916016) |
| `BLUF` | Put the answer and the action before the supporting detail | [ADP 6-0](https://adamdrake.com/static/ADP-6-0-Mission-Command.pdf) |
| `completed staff work` | Resolve what the material permits and recommend before asking | [Completed staff work](https://en.wikipedia.org/wiki/Completed_staff_work) |
| `cone of uncertainty` | Give a range with assumptions and the event that narrows it | [Coding Horror](https://blog.codinghorror.com/the-mysterious-cone-of-uncertainty/) |
| `cold reader` | Test what a reader without the writer's context can restate | [Pinker, mastering style](https://hwpi.harvard.edu/hilt/blog/masteringstyle) |
| `what would make this wrong?` | Search for disconfirming evidence before strengthening a claim | [Leitwörter entry](https://github.com/jonhilt/leitworter/blob/main/entries/what-would-make-this-wrong.md) |
| `deeper, not bigger` | Improve the method and evidence instead of adding sections | [Leitwörter entry](https://github.com/jonhilt/leitworter/blob/main/entries/deeper-not-bigger.md) |

The last two are prompts for the maintainer, not reader-facing vocabulary. They belong in research and review work unless a future evaluation shows that agents need them inside the skill.

## Coordination vocabulary worth keeping plain

The management and team literature adds useful behaviors, but most of its labels would make the skill heavier. Keep the behavior in ordinary words and use the established term only as a maintainer gloss:

- **Intent**: state the outcome, purpose, constraints, and room to act.
- **Boundary**: state the stop conditions and when to escalate.
- **State**: say what is true now, with source and date.
- **Assumption**: name what might be wrong.
- **Evidence**: show what supports or contradicts it.
- **Owner**: name who decides or acts next.
- **Next move**: choose the smallest useful, preferably reversible action.
- **Speak up**: ask for the missing risk, alternative, or contrary evidence.
- **Close loop**: record who acknowledged the request and what came back.

These map to mission command's intent and shared understanding, shared mental models, transactive memory, coordination conditions, psychological safety, sensemaking, and closed-loop communication. The sources also warn against importing authority, false consensus, stale ownership maps, or uncertainty theater. For that reason they remain research vocabulary, not new always-loaded rules.

## Sources audited

- [Matt Pocock, writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md) and [skill mechanics](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md)
- [Cursor pstack README](https://github.com/cursor/plugins/blob/main/pstack/README.md)
- [jonhilt/leitworter](https://github.com/jonhilt/leitworter)
- [Buber and Rosenzweig, Leitwortstil](https://tobias-lib.ub.uni-tuebingen.de/xmlui/bitstream/handle/10900/173736/Schwendemann_299.pdf?sequence=1&isAllowed=y)
- [Pinker, classic style and curse of knowledge](https://hwpi.harvard.edu/hilt/blog/masteringstyle)
- [Graham, Write Like You Talk](https://paulgraham.com/talk.html)
- [Cramton, The Mutual Knowledge Problem](https://doi.org/10.1287/orsc.12.3.346.10098)
- [Vaugrante et al., prompting replication](https://arxiv.org/abs/2409.20303)
- [Zheng et al., personas](https://aclanthology.org/2024.findings-emnlp.888/)
- [ADP 6-0, Mission Command](https://adamdrake.com/static/ADP-6-0-Mission-Command.pdf)
- [Clark and Brennan, Grounding in Communication](https://web.stanford.edu/~clark/1990s/Clark%20%26%20Brennan%201991.pdf)
- [Mathieu et al., shared mental models](https://doi.org/10.1037/0021-9010.85.2.273)
- [Lewis, transactive memory](https://doi.org/10.5465/3069448)
- [Okhuysen and Bechky, coordination](https://doi.org/10.5465/19416520903047533)
- [Edmondson, psychological safety](https://doi.org/10.2307/2666999)
- [Weick, Sutcliffe, and Obstfeld, sensemaking](https://doi.org/10.1287/orsc.1050.0133)
- [Haig et al., SBAR](https://doi.org/10.1016/S1553-7250(06)32022-3)
- [AHRQ TeamSTEPPS](https://www.ahrq.gov/teamstepps/index.html)
- [PlainLanguage.gov guidelines](https://www.plainlanguage.gov/guidelines/)

## Local audit

The current repository version has a 25-line, 457-word `SKILL.md`, six disclosed branch files, no examples file, and a mechanical shape limit of 35 lines and 650 words for the core. The suite passes 17 tests. The three saved Terra outputs from the previous round also pass the checker: 737 words for the rewrite, 318 for the compact progress reply, and 594 for the action request, with no errors. They still produce warnings, so the checker is a gate, not a quality verdict. The action request contains grouped data fields under some numbered points; that remains a semantic review concern for the cold reader, not a new regex rule.
