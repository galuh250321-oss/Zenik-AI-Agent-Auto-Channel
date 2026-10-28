# Implementation roadmap — gated, no invented completion

## Phase 0 (this commit): repo foundation
- [x] Architecture and engineering plan, channel profiles, budget targets, security constraints
- [x] Initial Python FastAPI skeleton, in-memory BudgetGuard demo, unit tests, channel registry
- [x] Windows React/Tauri prototype skeleton (build not yet verified on GitHub Actions)
- [ ] Cloud credentials, real AI calls, Telegram bot, production DB, rendering, YouTube upload: **NOT implemented**

## Phase 1: reliable backend, Telegram, budget persistence
- [ ] PostgreSQL schema + Alembic; database atomic budget reservations and ledger; per-channel/total caps
- [ ] Auth, RBAC and secret storage; job state machine, idempotency and worker outbox; tests for race conditions
- [ ] Telegram webhook with verified chat ID, signed callbacks, proposal approval/rejection, preview links
- [ ] Scheduler suggests channel-specific ideas in DRY RUN; operator sees four distinct channel feeds
- [ ] Show real cloud costs and provider-side hard/prepaid limits before any spending

Gate: approve a fake idea from Telegram -> authenticated persisted workflow -> zero paid external API calls -> audit trail and tests.

## Phase 2: AI research/writing and policy checks
- [ ] Verified provider adapters with typed JSON results, usage and cost estimates, cache, fallback, circuit breaker
- [ ] History evidence/search/citations/claim verification and ambiguity escalation
- [ ] Kids editorial/safety review, originality checking, ID/EN localization and human editorial approval
- [ ] Storyboard timeline JSON schema and one low-cost animated previsualization

Gate: 4 distinct channel scripts with linked research, no unsupported authority claims, and budget reservation.

## Phase 3: practical animation
- [ ] Original character bible, rig/pose/mouth animation assets and reusable Godot 2D scene template
- [ ] Blender/animated-map history template with reusable environment and crowd movement
- [ ] FFmpeg compositor, bilingual audio/subtitles/thumbnail generator; caching and scene-level rerender
- [ ] Two 30–60 second proof-of-concept animations, measure quality, fps, GPU minutes, provider costs
- [ ] Full 5–7 minute child master and full 10–12 minute historical master, independently assessed

Gate: real MP4 quality and per-minute costs support realistic operating plan. Budget target is revised based on evidence if not.

## Phase 4: desktop, YouTube and analytics
- [ ] Full Tauri native desktop UI, chat director, channel isolation, storyboards, spend dashboards, release checklist
- [ ] OAuth per YouTube channel, encrypted storage, resumable uploads, private-stage verification, scheduling, disclosure metadata
- [ ] API project auditing/compliance; staged publishing approval and analytics feedback loop
- [ ] Windows signed installer release workflow; versioning, rollback, smoke tests; no installer build on every commit by default

Gate: one complete approved master in two languages, published to verified channel IDs without double uploads, cost ledger reconciled.

## Phase 5: operations
- [ ] Schedule 4 masters / 8 localized uploads monthly, degrade gracefully if budgets constrain
- [ ] Alerts, analytics learning, provenance/report exports, backups and audits
- [ ] Expand beyond four channels only after repeatability and financial viability are demonstrated

## Priority of the next PR
P1: PostgreSQL transactional ledger + authenticated Telegram proposal approval + integration tests. No third-party paid calls until these safeguards pass.
