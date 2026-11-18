# Decision request

A **decision request** asks one person to decide (`decide`). Deliver **completed staff work**, which means you settle every question the material lets you settle yourself, so the reader's part is to approve, pick, or correct your recommendation. It adds the structure below to the rules in [SKILL.md](SKILL.md).

## Gather

List every decision, approval, and confirmation the material shows as pending on that person, including technical approvals they own. Run [ASK-AUDIT.md](ASK-AUDIT.md) on that list and keep only what it leaves. Choose what belongs in this message and put blocking decisions first. Done when the list covers the whole material.

## Shape

Open with the BLUF: the topic, what the person decides, what the decisions unblock, and by when. Then build the domain basics ground up. Then give each decision a short heading and these parts in order, each one once:

1. What must be decided, in one sentence.
2. The options, each stated by what makes it **distinguishable**: who it affects, what it costs, or what risk it leaves that the others do not. For a domain reader, show each option and each edge case through a concrete case (**Specification by Example**): a specific case, what the system does with it, and who carries the cost. For an engineering reader, show the contract that changes, what it costs, and its consequence for users or the business.
3. A **one-way door** (hard to reverse) is named in the sentence that shows what cannot be undone, and your recommendation carries stronger evidence and the person who owns the choice. A two-way door is the default and goes unmentioned, unless its reversibility is the reason to decide fast.
4. Your recommendation and its reason. For a domain reader, state the recommended rule as it would enter the spec. When you have no recommendation for several decisions, say so once for the group.
5. The numbered question. Number only the questions, across the whole message, so the person can answer by number. Each question asks one thing, stands on its own, and can be answered in a word or by picking an option; a sentence that joins several requests becomes several questions.

<example>
Options by their names: `"Migrar ahora incluye la migración; esperar la deja para después."`
Options by what makes them distinguishable: `"Migrar el martes corta el servicio 20 minutos en horario de atención. Esperar al sábado evita el corte, pero Finanzas recibe una semana más de reportes duplicados."`
</example>

## Check

Done when every item below holds:

- Every pending decision on the list is asked or scoped out on purpose.
- Each ask appears once (**MECE**) and asks for something only the reader can decide.
- Every decision you have a reason for carries a recommendation.
- Every one-way door is named where the irreversible step appears.
