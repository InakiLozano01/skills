# skills

Agent skills for Claude Code and Codex.

| Skill | Invocation | What it does |
|---|---|---|
| [`ground-up`](skills/ground-up/SKILL.md) | `/ground-up` | Writes text an outsider can follow, in the reader's own language: explanations for you, and decision requests, progress reports, and messages for a client, a superior, or someone with no background. It also rewrites a text that assumes context. Output in Spanish or English. |

`GLOSSARY.md` holds the vocabulary the skills use, such as curse of knowledge, common ground, backstage, appositive gloss, certainty, and door.

## Install

Copy a skill folder into the skills directory of your agent:

```bash
cp -r skills/ground-up ~/.claude/skills/   # Claude Code
cp -r skills/ground-up ~/.agents/skills/   # Codex
```

`ground-up` is user-invoked: it runs only when you call it. In Claude Code, `disable-model-invocation: true` in `SKILL.md` sets that. In Codex, `agents/openai.yaml` sets it with `allow_implicit_invocation: false`.

## Checks

`skills/ground-up/scripts/check_draft.py` checks a draft for the mistakes agents kept repeating: Spanglish verbs, voseo, dashes, AI vocabulary, the writer's process or the skill's own terms in the reader's text, refusals to estimate, options that restate their own name, and the word budget of a rewrite. The skill runs it in its Check step, and a cold-reader subagent (`COLD-READER.md`) covers what a regex cannot: redundancy, contradictions, and an opening that does not match the body.

Each `tests/ground-up/fixtures/fail-*` file is a real past output, anonymized, that must fail the check; `pass-*` must pass. Run the same command CI runs:

```bash
python3 tests/ground-up/test_check_draft.py
```

`AGENTS.md` pairs each rule with what enforces it.
