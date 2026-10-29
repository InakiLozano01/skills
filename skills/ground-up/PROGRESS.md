# Progress report

A **progress report** tells a reader whose ask is track where the work stands. It keeps every rule in SKILL.md and adds these.

Anchor the report in the product. The spec and its acceptance criteria are the measure, and the code is evidence. When the material has no written acceptance criteria, measure against the behaviour the work was meant to deliver, and say that no criteria are written.

Write the basics ground up, then:

1. What the work is for: the behaviour the product or its users should get.
2. What users or the business can do now that they could not before, measured against that behaviour. Each item states its certainty and where it was checked. Merged code, deployed code, and code verified in an environment are three different states.
3. What remains, and what blocks it. Each blocker names who can unblock it.
4. Risks that change the scope, the plan, or the date.
5. What you need from the reader, if anything. A decision goes as in [DECISION-REQUEST.md](DECISION-REQUEST.md).

For an engineering reader, technical facts back each item: the contract, the migration, the PR. For a domain reader, they stay out unless they change the scope, a risk, or a date.

## Check

- Every item is a behaviour of the product, in the reader's language, with its certainty.
- Every item called done names the environment where it was verified, or says it is only merged or only deployed.
- Every blocker names who can unblock it.
