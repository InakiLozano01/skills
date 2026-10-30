# Decision request

A **decision request** asks one person to decide (`decide`). It applies every rule in [SKILL.md](SKILL.md) and adds the structure below.

## Gather the pending decisions

During `Gather`, list every decision, approval, and confirmation that the material shows as pending on that person, including technical approvals they own. Done when the list covers the whole material. Select what belongs in this message and order blocking decisions first.

## Shape

Open with a **BLUF (Bottom Line Up Front)** sentence in plain words naming the topic and what the person needs to decide, then build the domain basics ground up, followed by:

1. What must be decided, in one sentence.
2. The options, and what changes with each one: who is affected, what it costs, and what risk remains.
3. Whether the decision is a **one-way door** (hard to reverse, requiring stronger evidence and a clear owner) or a **two-way door** (cheap to reverse, stating how to reverse it).
4. The recommendation and its reason, stated plainly.
5. What is needed from the person, and by when.

The **reader context** sets how the options read:

- **Domain decision**: the decision settles a business rule of the spec. Show each option through concrete scenarios, as in **Specification by Example**: a specific case, what the system does with it under that option, and who carries the cost. Show edge cases as concrete scenarios too. State the recommended rule as it would enter the spec: given a case, the system does what.
- **Engineering decision**: show each option as a contract and its trade-offs: what changes in the interface or data shape, what it costs, what risk remains, and its product consequence for users or the business.

End with the questions themselves: one numbered question per decision, so the person can answer by number. Each question asks one thing, is short, stands on its own, and can be answered in one word or by picking an option. When a sentence joins multiple requests (such as confirming a rule, naming an owner, and picking a date), split each request into its own numbered question.

## Check

Done when every item below holds:

- Every pending decision on the gathered list is asked or intentionally scoped out.
- The message opens with a plain-words BLUF and orders blocking decisions first.
- Every decision states whether it is a one-way or a two-way door.
- Each option of a domain decision shows at least one concrete scenario (**Specification by Example**); each option of an engineering decision names its product consequence.
- Each numbered question asks a single thing.
