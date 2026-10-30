# Ground-up writing

Vocabulary for a skill that writes text an outsider can follow from the first line: explanations for the user, progress reports and decision requests for third parties, and rewrites of existing text.

## Reader

**Outsider**:
The default reader: a capable person who brings prerequisite general technical vocabulary (PR, API, package manager) and zero knowledge of this project's domain, internal names, abstractions, or history.
_Avoid_: Beginner, layperson, newcomer

**Reader context**:
The **bounded context** the reader works in, which sets the **ubiquitous language** the text uses. One of four: **domain** (owns the business, such as a client or a product lead), **engineering** (owns technical decisions, such as a technical lead), **no background** (knows nothing of the work), or **user** (the person in the chat).
_Avoid_: Audience, persona, level

**Ask**:
What the text needs from the reader. One of three: **decide** (choose between options), **track** (follow where the work stands or how much is left), or **understand** (learn how something works or why it is built that way).
_Avoid_: Goal, purpose, intent

## Writing moves

**Ground up**:
The rule that every concept is **grounded** before a sentence leans on it: the reader either brings it as a **prerequisite** or meets its explanation first. In a narrative text (`understand`), the whole piece runs from the domain basics to the problem, its certainty, the decision or mechanism, and the consequence. In a structured text (`track` or `decide`), a **BLUF** in plain words opens the piece, and each section or bullet builds ground up inside: the problem or behaviour first, then the mechanism with its appositive glosses, its certainty, and its evidence.
_Avoid_: Bottom-up, from scratch, 0 to 100

**BLUF (Bottom Line Up Front)**:
An opening headline or executive summary in plain words, free of unglossed internal names, that states the direct answer, status partition, or decision request in the first lines before the supporting sections unpack the detail.
_Avoid_: Throat-clearing intro, teaser, abstract overview

**Appositive gloss**:
An internal name or domain term kept verbatim as the source writes it, followed on first use by a short inline appositive phrase that states what it is and what role it plays in this case (`"<name>, the <kind of thing> that <role in this case>, ..."`).
_Avoid_: Definition, translation, alias

**Deep module**:
Presenting complex implementation work through a small, reader-appropriate interface (the business rule, a concrete scenario, the verification state, and the cost) while keeping internal code, branch topology, merge conflicts, and subagent mechanics out of sight.
_Avoid_: Black box, dumbing down

**Portability test**:
Checking whether a sentence could move unchanged to another project's update or documentation; if it can, it carries generic filler instead of this project's **concrete mechanism**, scenario, or measured number, and is replaced.
_Avoid_: Generic summary, vibe check

**Traceability matrix**:
A complete item-by-item mapping between a referenced spec, feedback document, or checklist and the repository's current state (`main`, in an open PR or branch, unstarted, or waiting on an external decision), completed during `Gather` so a status update accounts for 100% of the scope with exact counts.
_Avoid_: Spot check, partial sample

**Decision request**:
A structured text that asks a specific person to decide: a BLUF opening line, the domain basics ground up, what must be decided, the options shown through concrete cases (**Specification by Example**) and what each one changes, whether the choice is a one-way or two-way door, a plain recommendation with its reason, and one short numbered question per decision.
_Avoid_: Consultation, escalation

**Door**:
How reversible a decision is. A **one-way door** is hard to reverse and requires stronger evidence and a named owner. A **two-way door** is cheap to reverse; the text states how to reverse it.
_Avoid_: Impact, severity

**Progress report**:
A structured text for a reader whose ask is `track`. It comes in two sizes, both opening with a BLUF and using `•` bullets inside the copyable message: a **full progress report** (five sections: executive summary in plain words, context with global task and slice, what advanced by capability, how it converges and what comes next, and asks/doubts/dependencies, with a `:thread:` two-message variant for Slack) and a **compact status reply** for questions like `"how much is left?"` (a 1–2 line BLUF with exact item counts from the traceability matrix, followed by state-bucket bullets for `main`, in review/integration, and pending work or decisions, closing with what closes today and what unlocks the final ETA).
_Avoid_: Status update, changelog

## Certainty

**Certainty**:
The epistemic state of a claim, stated in plain words inside the sentence whenever it changes what the reader believes or does.
_Avoid_: Confidence score, evidence level

**Verified**:
Checked, naming how and where it was checked: a real case, a synthetic test, or reading the code, in `main`, a PR branch, local tests, or production.

**Inferred**:
Deduced from a named fact, and unchecked. Included only when the reader needs it to decide or act, together with what check would confirm it.

**Gap**:
A question the material leaves unanswered. A gap is investigated or surfaced as **Open**; claims stay strictly within what the checked sources support.
_Avoid_: Assumption, best guess

**Document the null**:
When surfacing an **Open** item or gap, naming the specific sources, branches, or tools that were checked and returned nothing (for example, `"checked in main and open PRs, with no threshold defined yet in the Compliance spec"`), together with who owns the answer.
_Avoid_: Vague "unknown", silent omission

**In progress**:
Work that has started and is partial, stating both what exists and what is still missing.

**Planned**:
Decided or proposed, and unstarted, naming who proposed or approved it.
_Avoid_: In mind, to do

**Open**:
Unknown so far, or waiting on a decision from a named owner, with the null documented.
_Avoid_: Unclear, TBD
