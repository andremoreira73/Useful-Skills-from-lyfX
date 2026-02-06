# Integration with Claude Code Plan Mode

The design workflow and plan mode operate at different levels and complement each other:

- **design_notes.md** answers *what* to build and *why* (strategic, persistent, human-driven)
- **Plan mode** answers *how* to implement it (tactical, ephemeral, Claude-driven)

## Recommended flow in Claude Code

1. Complete Steps 1-3 of the workflow (identify engine, draft specs, human validates)
2. For each component, suggest the developer enters plan mode (`Shift+Tab` twice)
3. Reference the spec directly: *"Plan the implementation of [Component] per the spec in design_notes.md"*
4. Developer reviews the tactical plan (files to touch, order of changes) -- editable via `Ctrl+G`
5. Developer exits plan mode -> Claude executes the plan
6. Return to Step 5 of the workflow (verify results -- HUMAN GATE)

## Why this matters

Plan mode mechanically restricts Claude to read-only tools during planning -- it *cannot* write
code until the developer approves. This enforces the separation between design and implementation
that this workflow prescribes, but at the tactical level. The skill handles strategic gates
(intent, specs, validation); plan mode handles tactical gates (which files, what order, approve execution).

## When the developer is NOT using Claude Code

If working in claude.ai or another interface without plan mode, the skill's human gates serve as
the only safeguard. Be extra disciplined about stopping at gates and presenting proposed
changes before implementing them.
