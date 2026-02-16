# Useful Skills from lyfX

A collection of [Claude Code](https://claude.com/claude-code) skills and agents developed and battle-tested at [lyfX.ai](https://lyfx.ai). These turn Claude into a specialized agent for specific business and development workflows.

## What are skills?

Skills are `SKILL.md` files that give Claude Code domain expertise. Drop one into `.claude/skills/` and Claude automatically knows when and how to use it. No API setup, no plugins -- just a markdown file with structured instructions.

Learn more: [Claude Code Skills documentation](https://code.claude.com/docs/en/skills)

## What are sub-agents?

Agents are markdown files that define specialized sub-agents Claude can launch for focused tasks. Drop one into `.claude/agents/` and Claude can spawn it as a parallel worker with its own context window, tools, and skills. Agents are ideal for tasks like code review, where you want a dedicated reviewer that doesn't pollute your main conversation context.

Learn more: [Claude Code Sub-Agents documentation](https://code.claude.com/docs/en/sub-agents#use-the-agents-command)

## Available Agents

### `code-reviewer`

Structured code review agent that checks for quality, security, design health, and convention compliance. Understands core design principles (Single Responsibility, DRY, Law of Demeter, Open-Closed, etc.) and produces categorized findings (Critical / Warning / Passed) with line numbers and fix suggestions.

**Features:**

- General quality checks (naming, duplication, error handling, secrets)
- Python-specific checks (type hints, docstrings, context managers)
- Design principle violations from _Software Design_ by Ronald Mak
- Large codebase strategy using the `/rlm` skill for parallel scanning
- CLI command review (when paired with the `reviewing-cli-command` skill)

**Used by:** The `/ai-dev-workflow` skill launches this agent in Step 7 (Code Review & Hardening).

> **Attribution:** Based on the code-reviewer agent from the [Agent Skills with Anthropic](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/) course by DeepLearning.AI ([source](https://github.com/https-deeplearning-ai/sc-agent-skills-files/blob/main/L6/.claude/agents/code-reviewer.md)), modified with design health checks, large codebase strategy, and RLM integration. The original repository does not specify a license.

## Available Skills

### `/market-research`

Conduct structured market research with project-based organization. Guides Claude through a four-phase workflow: scope validation, data collection, analysis, and final deliverable.

**Includes:**

- SKILL.md -- workflow and project structure
- `references/methodology.md` -- deliverable format, source quality hierarchy, citation standards, forecast guidelines
- `assets/brief_template.md` -- structured template for scoping new research projects

**What you get:** Professional market research documents with inline citations, source quality tiers, and structured deliverables (executive summary, market overview, segment analysis, trends).

### `/linkedin-posts`

Draft and refine LinkedIn posts while keeping your authentic voice. Manages version history so you can iterate with Claude across sessions.

**Includes:**

- SKILL.md -- style guidelines, versioning convention, workflow

**What you get:** Posts that sound like you, not like AI. Conversational tone, scannable structure, curiosity-driven hooks. Each draft gets versioned (v2, v3...) so you can track iterations.

### `/lyfx-corporate-design`

Corporate design guidelines for lyfX.ai -- shared here as an example of how to encode brand identity into a skill. **Use this as inspiration for creating your own corporate design skill**, not as a template to copy directly.

**Includes:**

- SKILL.md -- color palette, typography, text hierarchy, button styling, CSS variables
- `assets/` -- logo variants (dark, white, favicon)

**What you get:** Consistent brand application across all visual material Claude creates -- documents, websites, presentations, UI designs.

### `/ai-dev-workflow`

Disciplined AI-assisted development workflow with 7 steps and 4 human gates. Makes Claude act as a structured pair programmer that enforces middle-out design, maintains living context files, runs design principle checks during decomposition, and includes a code review hardening step before shipping.

We'd been working this way for a while, but a [tweet from Eric Raymond](https://x.com/esrtweet/status/2019391670609940746) articulated the pattern so well that it inspired us to formalize our workflow into a reusable skill.

**Includes:**

- SKILL.md -- middle-out design workflow with 7 steps and 4 human gates
- `assets/design_notes_template.md` -- template for the living design brief
- `assets/code-reviewer-agent.md` -- bundled template for the code-reviewer agent (used in Step 7)
- `assets/reviewing-cli-command-skill.md` -- optional CLI review checklist for Typer commands
- `references/plan_mode.md` -- integration guide for Claude Code plan mode

**What you get:** Structured development sessions where Claude drafts specs, proposes decompositions (validated against design principles), and implements one component at a time -- stopping at human gates for validation. Step 7 runs parallel code review agents before shipping to catch cross-cutting issues like N+1 queries, naming inconsistencies, and architectural coupling.

### `/rlm`

Process large codebases (100+ files) using the Recursive Language Model pattern. Instead of reading every file into context (which causes context rot), this skill orchestrates parallel sub-agents that each handle a small slice of the codebase and report back summaries.

**Includes:**

- SKILL.md -- the RLM protocol (Index, Map, Reduce) with Native and Strict modes
- `scripts/rlm.py` -- helper script for indexing, searching, and chunking files

**What you get:** The ability to analyze, review, or search entire codebases without degrading Claude's reasoning quality. Pairs well with the `code-reviewer` agent for large-scale code reviews.

> **License notice:** This skill is adapted from [BowTiedSwan's rlm-skill](https://github.com/BowTiedSwan/rlm-skill), which does not currently specify a license. We've attributed the original work and adapted the implementation for Claude Code's tool system. If you use this skill, be aware that the upstream licensing status is unresolved. We encourage BowTiedSwan to add an explicit open-source license to their repository.

## Installation

### Installing skills

Copy any skill folder into your project's `.claude/skills/` directory:

```bash
cp -r skills/market-research /path/to/your/project/.claude/skills/
```

Or into your global skills for use across all projects:

```bash
cp -r skills/market-research ~/.claude/skills/
```

### Installing agents

Copy agent files into your global `.claude/agents/` directory:

```bash
mkdir -p ~/.claude/agents
cp agents/code-reviewer.md ~/.claude/agents/
```

### Symlink alternative

If you prefer to stay in sync with this repo:

```bash
git clone https://github.com/andremoreira73/Useful-Skills-from-lyfX.git
ln -s $(pwd)/Useful-Skills-from-lyfX/skills/market-research ~/.claude/skills/market-research
ln -s $(pwd)/Useful-Skills-from-lyfX/agents/code-reviewer.md ~/.claude/agents/code-reviewer.md
```

## Customization

These skills and agents are meant to be adapted to your workflow:

- **market-research**: Edit `references/methodology.md` to match your deliverable format and source preferences. Customize `assets/brief_template.md` for your research scope.
- **linkedin-posts**: Update the style guidelines in SKILL.md to match your voice and tone.
- **lyfx-corporate-design**: Replace the entire skill with your own brand's colors, fonts, and assets.
- **ai-dev-workflow**: Adjust the human gates, component spec format, design principles checklist, or project file conventions in SKILL.md to match your team's development rhythm. The bundled `code-reviewer-agent.md` template can be customized with project-specific review criteria.
- **rlm**: Adjust the `EXCLUDE_DIRS` in `scripts/rlm.py` to match your project's directory structure. Tune `chunk_size` for your context window needs.
- **code-reviewer**: Add project-specific checks, adjust the design principles that matter for your codebase, or add language-specific sections beyond Python.

## About lyfX.ai

[lyfX.ai](https://lyfx.ai) is a data and AI experts. We built these skills to streamline our own business workflows with Claude Code, and we're sharing them in the hope that others find them useful.

## License

MIT -- use however you like.
