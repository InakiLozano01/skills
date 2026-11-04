# Ground-up writing

Vocabulary for a skill that writes text an outsider can follow from the first line: explanations for the user, progress reports and decision requests for third parties, and rewrites of existing text.

`SKILL.md` uses ten leading words: **curse of knowledge**, **common ground**, **ground up**, **appositive gloss**, **BLUF**, **certainty**, **show, don't tell**, **backstage**, **classic style**, and **cold reader**. Every other term below belongs to the disclosed file that uses it (for example **completed staff work** to `DECISION-REQUEST.md`, **traceability matrix** and **cone of uncertainty** to `PROGRESS.md`, **edit by exception** to `REWRITE.md`), or explains where a rule came from.

## Reader

**Curse of knowledge**:
The failure this skill fixes: a writer who knows the project cannot imagine a reader who does not, so the text leans on names, history, and steps the reader never saw (Pinker, *The Sense of Style*, 2014; the term comes from Camerer, Loewenstein, and Weber, 1989).
_Avoid_: Jargon problem, too technical

**Common ground**:
What this reader and the writer already share (Clark, *Using Language*, 1996; in distributed teams, Cramton's "mutual knowledge problem", 2001). It decides what needs a gloss: anything outside it is grounded in the text first. A reader who owns the system shares its names and lacks what the writer found out.
_Avoid_: Reader level, background knowledge

**Outsider**:
The default reader when the common ground is unknown: a capable person who brings general technical vocabulary (PR, API, package manager) and zero knowledge of this project's domain, internal names, abstractions, or history.
_Avoid_: Beginner, layperson, newcomer

**Reader context**:
The **bounded context** the reader works in, which sets the **ubiquitous language** the text uses. One of four: **domain** (owns the business, such as a client or a product lead), **engineering** (owns technical decisions, such as a technical lead), **no background** (knows nothing of the work), or **user** (the person in the chat).
_Avoid_: Audience, persona, level

**Ask**:
What the text needs from the reader. One of three: **decide** (choose between options), **track** (follow where the work stands or how much is left), or **understand** (learn how something works or why it is built that way).
_Avoid_: Goal, purpose, intent

## Writing moves

**Ground up**:
The rule that every concept is **grounded** before a sentence leans on it: it sits in the reader's **common ground** or the reader meets its explanation first. Inside sentences and paragraphs it follows the **given-new** order. In a narrative text (`understand`), the whole piece runs from the domain basics to the problem, its certainty, the decision or mechanism, and the consequence. In a structured text (`track` or `decide`), a **BLUF** in plain words opens the piece, and each section or bullet builds ground up inside: the problem or behaviour first, then the mechanism with its appositive glosses, its certainty, and its evidence.
_Avoid_: Bottom-up, from scratch, 0 to 100

**BLUF (Bottom Line Up Front)**:
An opening headline or executive summary in plain words, free of unglossed internal names, that states the direct answer, status partition, or decision request in the first lines before the supporting sections unpack the detail.
_Avoid_: Throat-clearing intro, teaser, abstract overview

**Appositive gloss**:
An internal name or domain term kept verbatim as the source writes it, followed on first use by a short inline appositive phrase that states what it is and what role it plays in this case (`"<name>, the <kind of thing> that <role in this case>, ..."`).
_Avoid_: Definition, translation, alias

**Given-new**:
The order inside a sentence or paragraph: open with what the reader already holds, end on what is new to them (Clark and Haviland, 1977; Gopen and Swan, "The Science of Scientific Writing", 1990).
_Avoid_: Logical order, flow

**Backstage**:
The writer's process and the work's internal mechanics: searches, tools, subagents, session failures, logins, worktrees, cherry-picks, rebases, merge conflicts. It also holds the writer's code words, including this skill's own terms. The reader sees the result on stage, in reader-based prose; a backstage fact comes on stage only when it passes the **so-what test** (Goffman, *The Presentation of Self in Everyday Life*, 1959; Flower, "Writer-Based Prose", 1979).
_Avoid_: Deep module, black box, internal notes

**Show, don't tell**:
Showing the rule, the concrete case, the actor, and the measured number in place of a claim about them. Checked with the **portability test**.
_Avoid_: Concrete mechanism over vibes, be specific

**Classic style**:
The voice of the text: one colleague showing another something real, as equals in conversation, with the thing on stage and the writer's process backstage (Thomas and Turner, *Clear and Simple as the Truth*, 1994; Pinker, 2014). Characters are the subjects and actions are the verbs (Williams, *Style: Lessons in Clarity and Grace*). It keeps the vocabulary of Simplified Technical English (one name per thing, plain verbs) without its staccato, and it is checked with the **read-aloud test** (Graham, "Write Like You Talk", 2015).
_Avoid_: Simplified Technical English as the voice, formal register

**Cold reader**:
A subagent with fresh eyes that gets only the text and a one-line description of the reader, and restates what it is asked to do, by when, and what it could not follow. The gap between its restatement and the writer's intent is the curse of knowledge, made visible (pstack's independent reviewer; Pinker's advice to test drafts on representative readers).
_Avoid_: Self-review, proofread

**Tight, not terse**:
Dense prose that keeps the articles, verbs, and connectives of speech; it trims words, never items (pstack `teach`).
_Avoid_: Telegraphic, compressed

**Quantity maxim**:
Grice's rule, applied in both halves: as informative as this reader needs, and no more. A reader who owns the system already holds its names, so the words go to what the writer found (Grice, 1975; for experts, the expertise reversal effect, Kalyuga et al., 2003).
_Avoid_: Explain everything, be thorough

**Edit by exception**:
In a rewrite, keeping each sentence that already serves the reader and changing only the ones that fail them (DA Pam 600-67's quick-screen edit; management by exception).
_Avoid_: Rewrite from scratch

**Reverse outline**:
One line per section or bullet of the finished draft, used to check that the BLUF is the summary of the body, with every count, date, and exception (Minto: each level summarizes the ideas grouped below it).
_Avoid_: Proofread

**So-what test**:
Checking whether a sentence changes what this reader believes, decides, does, or when they get it. It pairs with the **portability test**: portability asks whether the sentence belongs to this project, so-what asks whether it matters to this reader.
_Avoid_: Relevance check

**Completed staff work**:
A decision request in which the writer has settled every question the material allows, so the reader approves, picks, or corrects a recommendation (memo attributed to Archer J. Lerch, 1942).
_Avoid_: Consultation, asking the reader to think for you

**MECE (mutually exclusive, collectively exhaustive)**:
The rule for lists and groups: each item and each ask appears once, in one group, and the groups cover everything gathered, so announced counts match (Minto, *The Pyramid Principle*).
_Avoid_: Recap list, restating the asks

**Cone of uncertainty**:
An estimate given as a range whose width matches how far along the work is, with its assumption and the event that narrows it (Boehm; McConnell, *Software Estimation*, 2006).
_Avoid_: No estimate yet, depends

**Commander's intent**:
The purpose behind every rule of the skill: the reader understands and acts with the fewest words. A rule applies where it serves that purpose; mechanical lines live in `check_draft.py` (US Army ADP 6-0, *Mission Command*).
_Avoid_: Checklist compliance

**DRI (Directly Responsible Individual)**:
The one named person who owns an answer, a decision, or an action. Every Open item and every ask names its DRI.
_Avoid_: Owner team, someone, TBD

**Portability test**:
Checking whether a sentence could move unchanged to another project's update or documentation; if it can, it carries generic filler instead of this project's concrete case, scenario, or measured number, and is replaced.
_Avoid_: Generic summary, vibe check

**Traceability matrix**:
A complete item-by-item mapping between a referenced spec, feedback document, or checklist and the repository's current state (`main`, in an open PR or branch, unstarted, or waiting on an external decision), completed during `Gather` so a status update accounts for 100% of the scope with exact counts.
_Avoid_: Spot check, partial sample

**Decision request**:
A structured text that asks a specific person to decide: a BLUF opening line, the domain basics ground up, what must be decided, the options shown through concrete cases (**Specification by Example**) and what each one changes, any one-way door named where the irreversible step appears, a plain recommendation with its reason, and one short numbered question per decision.
_Avoid_: Consultation, escalation

**Door**:
How reversible a decision is. A **one-way door** is hard to reverse and requires stronger evidence and a named owner. A **two-way door** is cheap to reverse and is the default; the text mentions it only when reversibility is the reason to decide fast.
_Avoid_: Impact, severity

**Progress report**:
A structured text for a reader whose ask is `track`. It comes in two sizes, both opening with a BLUF and using `•` bullets inside the copyable message: a **full progress report** (five sections: executive summary in plain words, context with global task and slice, what advanced by capability, how it converges and what comes next, and asks/doubts/dependencies, with a `:thread:` two-message variant for Slack) and a **compact status reply** for questions like `"how much is left?"` (a 1–2 line BLUF with exact item counts from the traceability matrix, followed by state-bucket bullets for `main`, in review/integration, and pending work or decisions, closing with a date range, its assumption, what closes today, and the event that narrows the range).
_Avoid_: Status update, changelog

## Certainty

**Certainty**:
The epistemic state of a claim, stated in plain words inside the sentence whenever it changes what the reader believes or does.
_Avoid_: Confidence score, evidence level

**Verified**:
Checked, naming how and where it was checked: a real case, a synthetic test, or reading the code, in `main`, a PR branch, local tests, or production.

**Inferred**:
Deduced from a named fact, and unchecked. Included only when the reader needs it to decide or act, together with what check would confirm it. An estimate built from the team's own estimates or the release calendar is an inference the reader needs, given as a range with its assumption.

**Gap**:
A question the material leaves unanswered. A gap is investigated or surfaced as **Open**; claims stay strictly within what the checked sources support.
_Avoid_: Assumption, best guess

**Document the null**:
When surfacing an **Open** item or gap, naming the specific sources, branches, or tools that were checked and returned nothing (for example, `"checked in main and open PRs, with no threshold defined yet in the Compliance spec"`), together with the **DRI** of the answer.
_Avoid_: Vague "unknown", silent omission

**In progress**:
Work that has started and is partial, stating both what exists and what is still missing.

**Planned**:
Decided or proposed, and unstarted, naming who proposed or approved it.
_Avoid_: In mind, to do

**Open**:
Unknown so far, or waiting on a decision from a named owner, with the null documented.
_Avoid_: Unclear, TBD
