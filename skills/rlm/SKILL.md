---
name: rlm
description: Process large codebases (>100 files) using the Recursive Language Model pattern. Treats code as an external environment, using parallel background agents to map-reduce complex tasks without context rot. Use when asked to "analyze codebase", "scan all files", deal with a "large repository", or "find usage of X across the project".
---

# Recursive Language Model (RLM) Skill

> Adapted from the [RLM skill by BowTiedSwan](https://github.com/BowTiedSwan/rlm-skill)
> for the Claude Code CLI environment.
>
> **License notice:** The original repository does not specify a license.
> This adaptation is provided with attribution; upstream licensing status is unresolved.

## Core Philosophy

**"Context is an external resource, not a local variable."**

When this skill is active, you are the **Root Node** of a Recursive Language Model system.
Your job is NOT to read every file yourself, but to orchestrate sub-agents that read code
in parallel and report back summaries.

## Protocol: The RLM Loop

### Phase 1: Choose Your Engine

| Engine          | Use Case                                                | Tool                                                    |
| --------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| **Native Mode** | General codebase traversal, finding files, structure.   | `Glob`, `Grep`, `Bash`                                  |
| **Strict Mode** | Dense data analysis (logs, CSVs, massive single files). | `python3 ~/.claude/skills/rlm/scripts/rlm.py`           |

### Phase 2: Index & Filter (The "Peeking" Phase)

**Goal**: Identify relevant data without loading it into your main context.

1. **Native**: Use `Glob` for file patterns, `Grep` with `output_mode: "files_with_matches"` for content.
2. **Strict**: Use `python3 ~/.claude/skills/rlm/scripts/rlm.py peek "query"`.

### Phase 3: Parallel Map (The "Sub-Query" Phase)

**Goal**: Process chunks in parallel using fresh agent contexts.

1. **Divide**: Split the work into atomic units (one file or chunk per agent).
   - **Strict Mode**: `python3 ~/.claude/skills/rlm/scripts/rlm.py chunk --pattern "*.log"` -> JSON chunks.
2. **Spawn**: Use the **Task tool** to launch parallel sub-agents.
   - Launch 3-5+ agents in parallel for broad tasks.
   - Give each agent **one specific file or chunk** and a focused question.
   - Use `subagent_type="Explore"` for read-only analysis, `subagent_type="general-purpose"` if the agent needs to write.
   - Set `run_in_background=true` for true parallelism.

```
Example — launch in a single message with multiple Task tool calls:

Task(subagent_type="Explore", run_in_background=true,
     prompt="Read src/api/routes.ts. Extract all endpoints and their @Auth decorators.")
Task(subagent_type="Explore", run_in_background=true,
     prompt="Read src/api/users.ts. Extract all endpoints and their @Auth decorators.")
...
```

### Phase 4: Reduce & Synthesize (The "Aggregation" Phase)

**Goal**: Combine results into a coherent answer.

1. **Collect**: Read background agent outputs via the `Read` tool on `output_file` paths,
   or use `TaskOutput` to retrieve results.
2. **Synthesize**: Look for patterns, consensus, or specific answers in the aggregated data.
3. **Refine**: If the answer is incomplete, perform a second RLM recursion on the missing pieces.

## Critical Instructions

1. **NEVER** read more than 3-5 files into your main context at once.
2. **ALWAYS** prefer the Task tool for reading/analyzing files when count > 1.
3. **Use `rlm.py`** for programmatic slicing of large files that Grep can't handle well.
4. **Python is your Memory**: If you need to track state across 50+ files, write a Python
   script (or use `rlm.py`) to scan them and output a summary.

## Example Workflow: "Find all API endpoints and check for Auth"

**Wrong Way (Monolithic)**:
- Read `src/api/routes.ts`, then `src/api/users.ts`, then ... (context fills up, reasoning degrades)

**RLM Way (Recursive)**:
1. **Filter**: `Grep(pattern="@Controller", output_mode="files_with_matches")` -> 20 files.
2. **Map**: Launch 20 Task agents in parallel (background), each extracting endpoints + auth decorators from one file.
3. **Reduce**: Collect all 20 outputs. Compile into a single table. Identify missing auth.

## Recovery Mode

If Task tool agents are unavailable or failing:
1. Fall back to **Iterative Python Scripting**.
2. Write a Python script that loads each file, runs a regex/AST check, and prints results to stdout.
3. Read the script's stdout via Bash.
