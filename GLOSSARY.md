# Ground-up writing

Vocabulary for a skill that writes text a reader without the project's context can follow from the first line: explanations for the user, messages and reports for third parties, and rewrites of existing text.

## Reader

**Outsider**:
The default reader: a capable person who knows general technical vocabulary (PR, API, package manager) but not this project's domain, internal names, abstractions, or history.
_Avoid_: Beginner, layperson, newcomer

**Reader context**:
The bounded context the reader works in, which sets the ubiquitous language the text is written in. One of four: **domain** (owns the business, such as a client or a product superior), **engineering** (owns technical decisions, such as a technical superior), **outside** (no background in the work), or **user** (the person in the chat).
_Avoid_: Audience, persona, level

**Ask**:
What the text needs from the reader. One of three: **decide** (choose between options), **track** (follow where the work stands), or **understand** (learn how something works or why it is so).
_Avoid_: Goal, purpose, intent

## Writing moves

**Gloss**:
A proper name kept as is, followed on first use by a short phrase that says what it is and what role it plays in this case.
_Avoid_: Definition, translation, alias

**Ground up**:
The order of a text in which no concept appears before it is explained: basics first, then the problem, its certainty, the decision, and the consequence.
_Avoid_: Bottom-up, from scratch, 0 to 100

**Decision request**:
A text that asks a specific person to decide: the basics ground up, what must be decided, the options and what each one changes, a recommendation with its reason, and what is needed from that person and by when. Each question is short and can be answered on its own.
_Avoid_: Consultation, escalation

**Door**:
How reversible a decision is. A **one-way door** is hard to reverse and needs more evidence and a clear owner. A **two-way door** is cheap to reverse and can be decided fast.
_Avoid_: Impact, severity

**Progress report**:
A text for a reader whose ask is track. It measures the work against the product's acceptance criteria, says what users can do now and how certain that is, and names what remains and who can unblock it. Code is evidence, not the subject.
_Avoid_: Status update, changelog

## Certainty

**Certainty**:
The state of a claim. A claim carries its state in the text when that state changes what the reader believes or does; open doubts are named where they arise.
_Avoid_: Confidence, evidence level

**Verified**:
Checked, with how it was checked: a real case, a synthetic test, or reading the code.

**Inferred**:
Deduced from a fact the text names, but not checked. Appears only when the reader needs it to decide or act.

**Gap**:
Something the material does not answer. A gap is investigated or named as Open; it is never filled with plausible content, and a known fact is never reshaped to cover it.
_Avoid_: Assumption, best guess

**In progress**:
Work that has started and is partial.

**Planned**:
Decided or proposed, but not started.
_Avoid_: In mind, to do

**Open**:
Unknown to everyone so far, or waiting on a decision.
_Avoid_: Unclear, TBD
