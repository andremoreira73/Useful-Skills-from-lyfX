---
name: market-research
description: Conduct structured market research for strategic decisions. Use when the user needs market analysis, competitive intelligence, or business research with formal deliverables.
---

# Market Research Assistant

## Project Structure

Each research project gets its own folder under `market_research/`:

```
market_research/
├── [project-name]/
│   ├── briefs/          # Research briefs and scope documents
│   ├── sources/         # Raw data, notes, PDFs, references
│   ├── outputs/         # Final deliverables
│   └── README.md        # Project overview (optional)
└── state.md             # Active and completed projects
```

## Workflow

### Phase 1: Scope Validation
1. User provides research request (free-form or using the brief template)
2. If free-form, prompt user to complete the brief template sections. Copy [assets/brief_template.md](assets/brief_template.md) into the project's `briefs/` folder and fill it in. See [references/methodology.md](references/methodology.md) for methodology details
3. Create project folder: `market_research/[project-name]/`
4. Save brief to `briefs/YYYY-MM-DD-topic.md`
5. Present scope summary and **pause for user approval** before proceeding

### Phase 2: Data Collection
1. Create todo list with specific research tasks
2. Work through sources systematically, saving raw notes to `sources/`
3. Flag any information gaps or limitations encountered
4. Proceed to Phase 3 when data collection is sufficient

### Phase 3: Analysis & Synthesis
1. Analyze collected data against research questions
2. Identify patterns, validate/invalidate hypotheses
3. Draft findings in deliverable format -- see [references/methodology.md](references/methodology.md) for deliverable structure, source hierarchy, citation requirements, and forecast standards
4. **Pause for user review** of draft if requested

### Phase 4: Final Deliverable
1. Produce final output in `outputs/YYYY-MM-DD-topic.md`
2. Update [[market_research/state]] with project completion
3. Archive sources appropriately

## Links

- [[market_research/state]] - Active and completed projects
- [assets/brief_template.md](assets/brief_template.md) - Standard research brief template
- [references/methodology.md](references/methodology.md) - Deliverable format, source hierarchy, citation rules
