# Decision request

A **decision request** asks one person to decide (`decide`). Deliver **completed staff work**: settle every question the material lets you settle yourself, so the reader's part is to approve, pick, or correct your recommendation. It applies every rule in [SKILL.md](SKILL.md) and adds the structure below.

## Gather the pending decisions

During `Gather`, list every decision, approval, and confirmation that the material shows as pending on that person, including technical approvals they own. Done when the list covers the whole material. Select what belongs in this message and order blocking decisions first.

## Shape

Open with a **BLUF (Bottom Line Up Front)** sentence in plain words naming the topic, what the person needs to decide, what the decisions unblock, and by when. Write it last, as the summary of the decisions below it. Then build the domain basics ground up. Each decision then follows the order below, and each part appears once:

1. What must be decided, in one sentence.
2. The options, each stated by what makes it **distinguishable**: the consequence for who is affected, what it costs, or what risk remains that the other options do not share.
3. When the decision is a **one-way door** (hard to reverse), say so in the sentence that shows what cannot be undone, and back your recommendation with stronger evidence and the person who owns the choice, as part of your staff work. A **two-way door** (cheap to reverse) is the default and needs a mention only when its reversibility is the reason to decide fast.
4. The recommendation and its reason, stated plainly. When you have none for several decisions, say so once for the group.
5. The numbered question that asks for the decision.

The **reader context** sets how the options read:

- **Domain decision**: the decision settles a business rule of the spec. Show each option through concrete scenarios, as in **Specification by Example**: a specific case, what the system does with it under that option, and who carries the cost. Show edge cases as concrete scenarios too. State the recommended rule as it would enter the spec: given a case, the system does what.
- **Engineering decision**: show each option as a contract and its trade-offs: what changes in the interface or data shape, what it costs, what risk remains, and its product consequence for users or the business.

Label each decision block with a short heading, and number only the questions, across the whole message, one per decision, so the person can answer by number. Each ask lives once, in the numbered question at the end of its decision; when the message holds a single decision, that question closes the message. Each question asks one thing, is short, stands on its own, and can be answered in one word or by picking an option. When a sentence joins multiple requests (such as confirming a rule, naming an owner, and picking a date), split each request into its own numbered question.

## Check

Done when every item below holds:

- Every pending decision on the gathered list is asked or intentionally scoped out.
- The message opens with a plain-words BLUF that names the topic, what the decisions unblock, and the date, and orders blocking decisions first.
- Every number, date, and exclusion in the BLUF matches the decisions below it.
- Every decision you have a reason for carries a recommendation; the ones without one are named once, together.
- Every one-way door is named where the irreversible step appears.
- Each option of a domain decision shows at least one concrete scenario (**Specification by Example**); each option of an engineering decision names its product consequence.
- Each numbered question asks a single thing, and each ask appears once (**MECE**).
- Every numbered question asks for something only the reader can decide; everything else is settled in your staff work.
