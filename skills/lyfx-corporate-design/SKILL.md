---
name: lyfx-corporate-design
description: lyfX.ai corporate design guidelines for consistent brand identity. Use when creating documents, websites, presentations, UI designs, or any visual material for lyfX.ai. Covers logo usage, color palette, typography, text hierarchy, and button styling.
---

# lyfX.ai Corporate Design

Apply these guidelines when creating any visual material for lyfX.ai.

## Logo

Two variants available in `assets/`:

- **logo-dark.png** - Dark logo for light backgrounds
- **logo-white.png** - White logo for dark backgrounds
- **favicon.png** - Favicon/app icon

The logo consists of a molecular node icon + "lyfX.ai" wordmark (the "X" has a gradient).

## Color Palette

### Primary Color - Violet

| Variant | HEX       | RGB          |
| ------- | --------- | ------------ |
| Light   | `#9133eb` | 145, 51, 235 |
| Dark    | `#611c94` | 97, 28, 148  |

### Secondary Color - Soft Mint

| Variant | HEX       | RGB           |
| ------- | --------- | ------------- |
| Light   | `#9ef2cc` | 158, 242, 204 |
| Dark    | `#4ac2ab` | 74, 194, 171  |

### Accent Colors

| Color           | HEX (dark/light)      | RGB (dark)   |
| --------------- | --------------------- | ------------ |
| Light Coral     | `#e54059` / `#f0807a` | 229, 64, 89  |
| Apricot         | `#ed783d` / `#f5a670` | 237, 120, 61 |
| Cornflower Blue | `#5245e5` / `#6e8aeb` | 82, 69, 229  |

### Base Colors

| Color            | HEX       | RGB           | Use                       |
| ---------------- | --------- | ------------- | ------------------------- |
| Dark Purple Grey | `#453d45` | 69, 61, 69    | Text on light backgrounds |
| Light Grey       | `#f0f0f0` | 240, 240, 240 | Light backgrounds         |
| White            | `#ffffff` | 255, 255, 255 | Backgrounds, text on dark |

## Typography

**Google Fonts required:**

- **Maven Pro** (Semibold) - Headlines & buttons
- **Inter** (Medium, Extrabold, Medium Italic) - Body text

### Text Hierarchy

**Light backgrounds:**
| Element | Font | Size | Color |
|---------|------|------|-------|
| H1 | Maven Pro Semibold | 36pt | Violet `#9133eb` |
| H2 | Maven Pro Semibold | 24pt | Violet `#9133eb` |
| H3 | Maven Pro Semibold | 18pt | Dark Purple Grey `#453d45` |
| Body | Inter Medium | 10pt | Dark Purple Grey `#453d45` |
| Emphasis | Inter Extrabold | 10pt | Dark Purple Grey `#453d45` |
| Note/small | Inter Medium | 8pt | Dark Purple Grey `#453d45` |

**Dark backgrounds:**
| Element | Font | Size | Color |
|---------|------|------|-------|
| H1 | Maven Pro Semibold | 36pt | Soft Mint `#9ef2cc` |
| H2 | Maven Pro Semibold | 24pt | Soft Mint `#9ef2cc` |
| H3 | Maven Pro Semibold | 18pt | White `#ffffff` |
| Body | Inter Medium | 10pt | White `#ffffff` |
| Emphasis | Inter Extrabold | 10pt | White `#ffffff` |
| Note/small | Inter Medium | 8pt | White `#ffffff` |

Sizes are relative - maintain proportions across applications.

## Buttons

| Background                | Button Color        | Text Color                 |
| ------------------------- | ------------------- | -------------------------- |
| Light (white, light grey) | Violet `#9133eb`    | White                      |
| Dark (violet, dark grey)  | Soft Mint `#4ac2ab` | Dark Purple Grey `#453d45` |

Use rounded corners for buttons.

## CSS Variables

```css
:root {
  /* Primary */
  --lyfx-violet: #9133eb;
  --lyfx-violet-dark: #611c94;

  /* Secondary */
  --lyfx-mint: #9ef2cc;
  --lyfx-mint-dark: #4ac2ab;

  /* Accents */
  --lyfx-coral: #e54059;
  --lyfx-coral-light: #f0807a;
  --lyfx-apricot: #ed783d;
  --lyfx-apricot-light: #f5a670;
  --lyfx-blue: #5245e5;
  --lyfx-blue-light: #6e8aeb;

  /* Base */
  --lyfx-text: #453d45;
  --lyfx-bg-light: #f0f0f0;
  --lyfx-white: #ffffff;

  /* Typography */
  --font-heading: "Maven Pro", sans-serif;
  --font-body: "Inter", sans-serif;
}
```
