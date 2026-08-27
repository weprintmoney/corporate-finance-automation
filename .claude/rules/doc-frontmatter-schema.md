---
owner: hannahstulberg
---

# Doc Frontmatter Schema

When you create any new non-CLAUDE.md doc under `product-development/` or `team/`, populate frontmatter per this schema. Do not duplicate fields already encoded by the folder location or by `product-development/feature-index.yaml`. Per-doc-type detail (call duration, customer health, experiment result, severity, metric_key, etc.) belongs in the body, not in frontmatter.

## Core fields (every doc)

| Field | Notes |
|---|---|
| `title` | Human-readable title. Lets tools render lists without parsing the H1. |
| `status` | One of `draft`, `active`, `approved`, `shipped`, `archived`, `superseded`. Default `active`. |
| `owner` | GitHub handle. Single accountable person. |
| `created` | `YYYY-MM-DD`. Immutable. |
| `last_updated` | `YYYY-MM-DD`. Bump on edit. |

## Author (when distinct from owner)

| Field | Notes |
|---|---|
| `author` | GitHub handle. Person who drafted. `owner` may be a different long-term steward. |

## Source links (whichever apply)

Use placeholder URLs (with a per-doc unique slug) when the real URL is not yet known.

| Field | When used |
|---|---|
| `google_doc_url` | PRDs, RFCs, plans, strategy, onboarding, sales/process docs, launch emails, meeting docs, metric/schema definitions |
| `slides_url` | Slide decks (launch announcements, all-hands) |
| `figma_url` | PRDs / design docs with a paired Figma file |
| `granola_url` | Call transcripts, meeting transcripts |
| `linear_url` | Anything tracked as a Linear issue/project (account folders, launches, investigations) |
| `slack_thread_url` | Decision threads, launch announcements |

## What is NOT in frontmatter (intentionally)

- `doc_type`, `product_area`, `role`, `feature`, `tags` — encoded by folder path or by `feature-index.yaml`.
- `reviewers`, `target_release`, `related_prd`/`related_rfc`/`related_plan` — live in `feature-index.yaml`.
- Per-doc-type content fields: `call_date`, `duration_minutes`, `meeting_type`, `attendees`, `champion`, `health`, `arr`, `hypothesis`, `result`, `experiment_id`, `severity`, `metric_key`, `refresh_cadence`, `table`, `upstream_sources`, etc. — body content, not metadata.

## Examples

### PRD

```yaml
---
title: Custom Domains PRD
status: draft
owner: hannahstulberg
author: hannahstulberg
created: 2026-03-08
last_updated: 2026-03-22
google_doc_url: https://docs.google.com/document/d/custom-domains-prd-PLACEHOLDER/edit
figma_url: https://figma.com/file/custom-domains-PLACEHOLDER
linear_url: https://linear.app/forge/project/custom-domains-PLACEHOLDER
---
```

### Call transcript

```yaml
---
title: Crestview Financial — Call Transcript 2026-03-14
status: active
owner: hannahstulberg
created: 2026-03-14
last_updated: 2026-03-14
granola_url: https://app.granola.ai/meetings/crestview-financial-2026-03-14-PLACEHOLDER
---
```

### Account context

```yaml
---
title: Stackline — Account Context
status: active
owner: hannahstulberg
created: 2026-02-01
last_updated: 2026-05-01
linear_url: https://linear.app/forge/project/stackline-PLACEHOLDER
---
```

### Metric definition

```yaml
---
title: Custom Domains — Metrics Definition
status: active
owner: caseynguyen
created: 2026-03-10
last_updated: 2026-03-22
google_doc_url: https://docs.google.com/document/d/custom-domains-metrics-PLACEHOLDER/edit
---
```

### Onboarding guide

```yaml
---
title: Engineering Onboarding Guide
status: active
owner: alexrivera
created: 2025-09-01
last_updated: 2026-03-01
google_doc_url: https://docs.google.com/document/d/onboarding-engineering-PLACEHOLDER/edit
---
```
