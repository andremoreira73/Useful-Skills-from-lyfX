# Useful Skills from lyfX

A collection of [Claude Code](https://claude.com/claude-code) skills developed and battle-tested at [lyfX.ai](https://lyfx.ai). These skills turn Claude into a specialized agent for specific business workflows.

## What are skills?

Skills are `SKILL.md` files that give Claude Code domain expertise. Drop one into `.claude/skills/` and Claude automatically knows when and how to use it. No API setup, no plugins -- just a markdown file with structured instructions.

Learn more: [Claude Code Skills documentation](https://code.claude.com/docs/en/skills)

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

## Installation

### Option 1: Copy individual skills

Copy any skill folder into your project's `.claude/skills/` directory:

```bash
cp -r skills/market-research /path/to/your/project/.claude/skills/
```

Or into your global skills for use across all projects:

```bash
cp -r skills/market-research ~/.claude/skills/
```

### Option 2: Clone and symlink

```bash
git clone https://github.com/andremoreira73/Useful-Skills-from-lyfX.git
ln -s $(pwd)/Useful-Skills-from-lyfX/skills/market-research ~/.claude/skills/market-research
```

## Customization

These skills are meant to be adapted to your workflow:

- **market-research**: Edit `references/methodology.md` to match your deliverable format and source preferences. Customize `assets/brief_template.md` for your research scope.
- **linkedin-posts**: Update the style guidelines in SKILL.md to match your voice and tone.
- **lyfx-corporate-design**: Replace the entire skill with your own brand's colors, fonts, and assets.

## About lyfX.ai

[lyfX.ai](https://lyfx.ai) is a data and AI consultancy. We built these skills to streamline our own business workflows with Claude Code, and we're sharing them in the hope that others find them useful.

## License

MIT -- use however you like.
