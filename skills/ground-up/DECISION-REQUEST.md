# Decision request

A **decision request** asks one person to decide. It keeps every rule in SKILL.md and adds these.

## Gather the pending decisions

While you gather, list every decision, approval, and confirmation that the material shows as pending on that person, including technical approvals they own. Done when the list covers the whole material. Then choose what goes in, putting first what blocks the work. Anything you leave out, leave out on purpose.

## Shape

Write the basics ground up, then:

1. What must be decided, in one sentence.
2. The options, and what changes with each one: who is affected, what it costs, and what risk remains.
3. Whether the decision is a **one-way door**, hard to reverse, or a **two-way door**, cheap to reverse. A one-way door gets more evidence and a clear owner. A two-way door says how to reverse it.
4. The recommendation and its reason, said plainly.
5. What is needed from the person, and by when.

The reader context sets how the options read:

- **Domain decision**: the decision settles a rule of the spec. Show each option through concrete examples, as in Specification by Example: a case, what the system does with it under that option, and who carries the cost. Edge cases appear as examples too. State the recommended rule as it would enter the spec: given a case, the system does what.
- **Engineering decision**: show each option as a contract and its trade-offs: what changes in the interface or the data, what it costs, what risk remains, and what each one changes for the users or the business.

End with the questions themselves: one numbered question per decision, so the person can answer by number. Each question asks one thing, is short, makes sense on its own, and can be answered in one word or by picking an option. A sentence that joins requests, such as "confirm X, or say who will, and tell us Y", holds three questions: split it.

Before you write, read [EXAMPLE.md](EXAMPLE.md). It shows one decision request before and after these rules, in an invented domain.

## Check

- Every pending decision on the gathered list is asked or left out on purpose.
- The blocking decisions come first.
- Every decision says whether it is a one-way or a two-way door.
- Each option of a domain decision shows at least one concrete case. Each option of an engineering decision names its product consequence.
- Each numbered question asks one thing.
