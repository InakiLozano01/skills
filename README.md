# skills

Agent skills for Claude Code and Codex.

| Skill | Invocation | What it does |
|---|---|---|
| [`ground-up`](skills/ground-up/SKILL.md) | `/ground-up`, `$ground-up`, or automatic | Writes text an outsider can follow, in the reader's own language: explanations for you, and decision requests, progress reports, and messages for a client, a superior, or someone with no background. It also rewrites a text that assumes context. Output in Spanish or English. |

`GLOSSARY.md` holds the vocabulary the skills use, such as curse of knowledge, common ground, backstage, appositive gloss, certainty, and door.

## Install

Copy a skill folder into the skills directory of your agent:

```bash
cp -r skills/ground-up ~/.claude/skills/   # Claude Code
cp -r skills/ground-up ~/.agents/skills/   # Codex
```

`ground-up` runs when you name it (`/ground-up` in Claude Code, `$ground-up` in Codex) and when the model sees a matching task: an explanation for someone without the background, a report or progress update for someone else, a decision or action request, or a rewrite. `agents/openai.yaml` allows implicit invocation in Codex, and `SKILL.md` sets no `disable-model-invocation`, so Claude Code can load it as well.

## Checks

`skills/ground-up/scripts/check_draft.py` checks a draft for the mistakes agents kept repeating: Spanglish verbs, voseo, dashes, AI vocabulary, the writer's process or the skill's own terms in the reader's text, refusals to estimate, options that restate their own name, two questions under one number, the word budget of a rewrite, and the size of a message to paste. The skill runs it in its Check step, and a cold-reader subagent (`COLD-READER.md`) covers what a regex cannot: redundancy, contradictions, and an opening that does not match the body. A text over 200 words fails the script until it receives the cold reader's saved answer (`--cold`) or is declared as written for the user (`--for-user`). A text that asks another reader a question fails until it receives the ask audit's answer (`--asks`, `ASK-AUDIT.md`) with one `NEEDED` line per question.

Each `tests/ground-up/fixtures/fail-*` file is a real past output, anonymized, that must fail the check; `pass-*` must pass. Run the same command CI runs:

```bash
python3 tests/ground-up/test_check_draft.py
```

`AGENTS.md` pairs each rule with what enforces it.
