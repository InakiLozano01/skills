# skills

Agent skills for Claude Code and Codex.

| Skill | Invocation | What it does |
|---|---|---|
| [`ground-up`](skills/ground-up/SKILL.md) | `/ground-up` | Writes text an outsider can follow, in the reader's own language: explanations for you, and decision requests, progress reports, and messages for a client, a superior, or someone with no background. It also rewrites a text that assumes context. Output in Spanish or English. |

`GLOSSARY.md` holds the vocabulary the skills use, such as outsider, gloss, certainty, reader context, ask, and door.

## Install

Copy a skill folder into the skills directory of your agent:

```bash
cp -r skills/ground-up ~/.claude/skills/   # Claude Code
cp -r skills/ground-up ~/.agents/skills/   # Codex
```

`ground-up` is user-invoked: it runs only when you call it. In Claude Code, `disable-model-invocation: true` in `SKILL.md` sets that. In Codex, `agents/openai.yaml` sets it with `allow_implicit_invocation: false`.
