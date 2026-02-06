# Market Research Methodology Reference

## Table of Contents

- Research Brief Template
- Deliverable Format
- Source Quality Hierarchy
- Forecast Standards
- Limitations Acknowledgment
- Output Guidelines
- Inline Citation Requirements

## Research Brief Template

When starting new research, ensure these sections are defined:

```markdown
## Objective
[What decision will this research inform?]

## Scope
- **Categories/Segments**: [What specific areas to cover]
- **Geographic Focus**: [Countries/regions]
- **Time Horizon**: [Historical period + forecast horizon if applicable]

## Data Sources to Investigate
[Specific platforms, databases, organizations]

## Research Questions
### Market Structure
[Questions about size, players, dynamics]

### Buyer/Customer Behavior
[Questions about motivations, patterns, segments]

### Trends & Forecasts
[Questions about direction, drivers, projections]

## Deliverable Requirements
[Specific format, depth, or focus areas]
```

## Deliverable Format

All outputs follow this structure:

### 1. Executive Summary (1 page max)
- Key findings (3-5 bullets)
- Strategic implications
- Confidence assessment

### 2. Market Overview
For each geographic market:
- Market size estimates (with source and year)
- Key players and market share where available
- Regulatory/structural factors

### 3. Segment Analysis
Ranking by relevant metric (define which: volume, value, growth rate, etc.)

### 4. Behavioral Analysis
Evidence-based insights on buyer/customer motivations

### 5. Trends & Forecasts
- Historical trends (with data points)
- Forward-looking projections (with source, methodology note, date of forecast)
- Key drivers and uncertainties

### 6. Sources & Methodology
- Full source list with links
- Methodology notes
- Information gaps flagged

## Source Quality Hierarchy

Prioritize sources in this order:

| Tier | Source Type | Examples |
|------|-------------|----------|
| 1 | Industry reports & databases | Statista, IBISWorld, Euromonitor, Grand View Research |
| 2 | Trade associations & manufacturer data | Industry associations, company annual reports, investor presentations |
| 3 | Trade press & specialized publications | Industry magazines, trade news sites, conference proceedings |
| 4 | General news & other | Business news, LinkedIn articles, forums |

Always note the tier when citing. Prefer Tier 1-2 for quantitative claims.

## Forecast Standards

When including forecasts:
- **Source**: Who made this forecast?
- **Date**: When was it published?
- **Methodology note**: Brief indication if available (e.g., "based on historical CAGR" or "expert panel consensus")
- **Confidence framing**: Use language like "Industry analysts project..." rather than stating as fact

Present forecasts pragmatically. They are useful directional indicators even when imprecise - don't over-caveat, just attribute properly.

## Limitations Acknowledgment

Be explicit about access constraints:
- Cannot access paywalled databases directly (user may need to provide excerpts)
- Cannot make live calls or access real-time pricing APIs
- Cannot verify information that requires account login
- Web search provides publicly available information only

When a limitation affects research quality, note it in the deliverable and suggest how the user might fill the gap manually.

## Output Guidelines

- **Readability**: Use clear headings, white space, and bullet points. Avoid dense walls of text.
- **Tables**: Use for comparisons, rankings, and data summaries
- **No plots**: Text and tables only
- **Actionable**: Frame findings in terms of "so what" for strategic decisions

## Inline Citation Requirements (CRITICAL)

**Every factual claim must include an inline source link.** Do not just list sources at the end - the reader must be able to verify each claim immediately.

**Required inline citations for:**
- Market size figures: "The market is valued at $4.0B ([IntelMarketResearch](url))"
- Growth rates and CAGRs
- Market share estimates
- Vendor claims and features
- Regional data
- Forecasts and projections
- Any quantitative data point

**Format:**
- Use markdown links inline: `text ([Source Name](url))`
- For multiple sources: `text ([Source 1](url1), [Source 2](url2))`
- In tables, add source column or footnotes with links

**Example:**
```
BAD:  "The market is valued at $4.0 billion in 2025."
GOOD: "The market is valued at $4.0 billion in 2025 ([IntelMarketResearch](https://example.com/report))."
```

The Sources & Methodology section at the end is still required for full reference, but inline links are mandatory throughout.
