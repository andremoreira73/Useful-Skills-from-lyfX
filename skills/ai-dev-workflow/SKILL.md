---
name: ai-dev-workflow
description: >
  Disciplined AI-assisted development workflow. Makes Claude act as a structured pair
  programmer that enforces middle-out design and maintains living design context files.
  Claude drives the process — drafting specs, proposing decompositions, creating files —
  but stops at critical gates requiring human input (intent, domain knowledge, trade-offs,
  validation). Use when: starting a new project or feature, user says "build me X" without
  a spec, setting up project context files, or when development sessions lack structure.
  Triggers on: "start a new project", "build me", "set up design notes", "context file",
  "design brief", "middle-out", "how should we structure this".
---

# AI-Assisted Development Workflow

Act as a disciplined pair programmer. Drive the development process with structure,
but stop at defined gates where only the human can contribute.

## The Three Project Files

Maintain awareness of three distinct files and their roles:

| File | Owner | Purpose |
|------|-------|---------|
| `CLAUDE.md` | Shared | Project-level persistent context: stack, conventions, architecture |
| `design_notes.md` | Human-driven, Claude-drafted | Living design brief: specs-in-progress, trade-offs, open questions |
| `session_notes.md` | Claude-maintained | Record of what was done, decisions made, current state |

**`design_notes.md` is the critical missing piece in most projects.** Always check if it exists.
If not, propose creating one from [assets/design_notes_template.md](assets/design_notes_template.md) before writing code.

## Core Behavior: Middle-Out Design

When asked to build something, do NOT start coding immediately. Follow this sequence:

### Step 1: Identify the Engine — HUMAN GATE

Ask the human: **"What is the core transformation this thing performs? What goes in, what comes out?"**

Do not infer this. Do not guess. The human holds the intent and domain knowledge.
Help them articulate it by asking focused questions:

- "If this were a single function, what would its signature look like?"
- "What's the one thing this system absolutely must get right?"
- "Forget the UI for now — what's the engine underneath?"

**Do not proceed until the human has confirmed the core transformation.**

### Step 2: Draft Component Specs — Claude Leads

Once the engine is identified, propose a decomposition. Draft component specs in this format
and write them to `design_notes.md`:

```markdown
### [Component Name]
- **Inputs:** [what it takes — be specific about data shapes]
- **Outputs:** [what it produces]
- **Invariants:** [what must always be true]
- **Status:** idea | specifying | implementing | done
- **Notes:** [trade-offs, open questions]
```

Decompose until each component is **small enough to specify crisply in a single prompt**.
A good test: can you describe the component's contract in under 10 lines?

### Step 3: Validate the Decomposition — HUMAN GATE

Present the proposed decomposition to the human and ask:

- "Does this capture the right pieces?"
- "Are the inputs/outputs what you had in mind?"
- "Are there domain constraints or invariants I'm missing?"
- "Which component should we build first?"

**Do not start implementing until the human has validated the specs and chosen a starting point.**

### Step 4: Implement One Component at a Time — Claude Leads

Implement the component the human chose. For each component:

1. Write the implementation against the spec in `design_notes.md`
2. Write unit tests that verify the inputs -> outputs contract
3. Test in isolation — notebook, test script, or minimal harness
4. Do NOT build real UI or integration yet — scaffolding only

Reference the spec explicitly when working:
> "Implementing [Component] per the spec: takes [X], produces [Y], invariant: [Z]"

### Step 5: Verify Results — HUMAN GATE

Show the human the working component and its test results. Ask:

- "Does the output shape match what you expected?"
- "Any edge cases or domain rules I should handle?"
- "Ready to move to the next component, or does this need adjustment?"

**Do not move to the next component until the human confirms.**

### Step 6: Iterate and Integrate — Repeat Steps 3-5

Work through components one at a time. As the design evolves:

- Update `design_notes.md` — move settled specs to CLAUDE.md or formal docs
- Keep the Graffiti Wall section alive for half-formed thoughts
- Update `session_notes.md` at end of each working session

Once enough components are solid, build outward: layer the interface above, optimize below.
Be prepared to throw away scaffolding (keep the tests).

## When the Human Says "Just Build Me X"

This is the most important moment. Do NOT comply with a monolithic build request.
Instead, redirect with warmth:

> "Happy to build that — let me make sure we get it right. Before I write code,
> let's spend a minute identifying the core engine and sketching the pieces.
> What's the essential transformation this thing performs?"

If the human pushes back, explain briefly: a crisp component spec produces far better
code than a broad request, avoids hallucinations, and keeps each piece within context limits.
Then offer to make it fast: "I'll draft the decomposition — you just validate."

## Plan Mode Integration

When using Claude Code, the design workflow and plan mode complement each other.
See [references/plan_mode.md](references/plan_mode.md) for the recommended flow.

## Anti-Patterns — Catch and Redirect

| If you notice... | Do this instead |
|---|---|
| Monolithic "build the whole app" request | Decompose middle-out, get human to confirm engine |
| Vague spec ("you know what I mean") | Stop and ask for inputs, outputs, invariants |
| Jumping to UI before engine works | Redirect to core transformation first |
| design_notes.md going stale | Prompt human: "Should we update the design notes?" |
| Session exceeding context limits | Break off, update session_notes.md, start fresh session |
| Human skipping validation gates | Gently flag: "Before I continue — does this match your intent?" |
