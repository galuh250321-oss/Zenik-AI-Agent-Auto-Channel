# Architecture — Zenix AI Studio

Version: 0.1 design baseline (2026-10-28). All integrations are planned until explicitly marked implemented. This is a design specification, not evidence that animation automation is complete.

## Goals and non-goals

- One native Windows Tauri v2 installer (.exe via NSIS), not a browser/localhost dashboard for the operator.
- Full-cloud workers continue with desktop turned off; Telegram provides mobile approvals.
- Four logically isolated YouTube channels, two story families (kids manners and teen/adult history), localized ID/EN.
- Minimum viable automation: suggest ideas -> approve -> research -> scripts -> storyboard -> asset/render -> QC -> preview -> approve -> YouTube scheduled publication -> analytics.
- Operational spend target <= IDR 4,000,000/month, enforce *our own paid-job admission control*; no claim of guaranteed external provider hard cap.
- Full movement rather than static-image slideshow. Rigged characters, camera moves, 2D effects, maps and 3D scene animation; generative video as optional premium fallback.
- Accurate historical sources, original characters, kids-safety and YouTube policy checks.
- Never store paid credentials or OAuth refresh tokens in desktop webview or GitHub.

Not in Phase 0: full model-driven rigging, perfect consistent animation, production auth, real OAuth, automatic publication, production accounting, scene-level render engine. See ROADMAP.

## System boundaries

1. Desktop (Tauri + React + TypeScript): login, multi-channel dashboards, AI chat director, proposal review, character library, storyboard/timeline preview, render queue, cost center, connectors. Local app holds short-lived session tokens only; no private filesystem scanning.
2. Cloud API (FastAPI): authorized requests, channel settings, content proposals, approval events, budgets, jobs, asset metadata, analytics. Owns policy decisions.
3. Durable state (PostgreSQL): channels, episodes, versions, sources, approvals, jobs, per-provider expenses, budgets, upload records and audit trail. Migrations via Alembic.
4. Queue (Redis + Celery/RQ or Arq, selected after profiling): idempotent stage jobs; retries and dead-letter handling; manual pause/cancel. Never store authoritative ledger only in Redis.
5. Scheduler (cloud): channel-specific cadence, cost-aware daily ideation, analytics gathering, retries, webhook health monitoring.
6. AI Router: typed provider adapters and fallback for text, image, TTS and optional video. A claimed model name is only a configuration target until its API/model listing and commercial rights are verified.
7. Render workers: Godot 2D rigged cartoon pipeline; Blender 3D history pipeline; FFmpeg encoding; optional per-shot generative video. Render workers may use cloud CPU or metered GPU as demanded.
8. Object storage (S3-compatible): source assets, approved character sheets, scene manifests, audio/video outputs, thumbnails; signed short-lived preview links.
9. Telegram Bot: notification and authorized inline callbacks; signed/expiring action payload linked to server-side state. Telegram is control, not a secret database.
10. YouTube: per-channel OAuth credentials stored encrypted server side; upload initially private or unlisted where permitted; publish/schedule only after explicit approval and availability checks. Channel selection must be verified before upload.

## End-to-end episode state machine

DRAFT_IDE -> PROPOSED -> IDEA_APPROVED -> RESEARCHED -> SCRIPT_READY -> STORYBOARD_READY -> ASSETS_READY -> ANIMATING -> EDITING -> QC -> PREVIEW_READY -> FINAL_APPROVED -> UPLOAD_PENDING -> UPLOADED -> SCHEDULED -> PUBLISHED -> ANALYZED.

Reject/revise paths: any editorial stage can transition to NEEDS_REVISION, then rerun only affected downstream steps. Any technical stage may become FAILED_RETRYABLE or FAILED_FINAL; cancellations become CANCELED. Publication transitions MUST be idempotent (provider video ID and idempotency key). Transitions require server authorization and immutable audit events; never let the client set an arbitrary status.

## Request flows

### Proposal
Scheduler checks pacing, channel profile and remaining budget; research worker produces candidate outline + reference links + originality comparison; content safety screens; persist proposal; Telegram sends title, hook, synopsis, genre, target duration, source confidence and estimated render spend. An approval callback with expiring nonce authorizes ONE idea.

### Production
Generate structured scene manifest with schema validation. Reference image, character bible, expressions, pose library, audio track, language-specific subtitle/lipsync and licensed assets. Run low-cost animatic preview before expensive render. Budget service reserves estimated maximum per billable step, then executes, reconciles actual charge, alerts on discrepancies and releases unused funds. If reservation fails stop paid job before API call.

### History
Evidence retrieval -> citation record -> independent verification -> controversy/uncertainty tagging -> script; historical dialogue invented for storytelling marked dramatization. Material disputes must require manual editorial check. No unsupported claims silently inserted.

### Final review
QC checks silence/clipping, wrong subtitles, visual continuity, historical references, child-safety, disclosure, licensing, correct channel selection, privacy/metadata, Made for Kids determination, non-graphic depiction of war. Operator approves exact immutable render hash, channel and schedule. On revised content approval invalidates.

### Publishing
Store confirmed YouTube channel ID from OAuth connection. Upload through backend with resumable protocol, idempotent retries, valid audience/synthetic media labels when required. Fail closed if account mapping or approvals invalid. Record returned video ID and status. Avoid double uploads on unknown response.

## Isolation and identity

channel_id is a required key on all episodes, character assets, prompts, credentials, jobs, budgets, uploads and audit events. Every DB query and object-storage path is scoped by authorized tenant/channel. Two languages can share master_episode_id and permitted base animation assets, but localized script/audio/metadata are separately reviewed and independently publishable. Do not assume mere dubbing ensures YouTube eligibility.

## Suggested API groups (versioned)

- GET /health; GET /api/v1/channels
- POST /api/v1/ideas/suggest; GET /api/v1/ideas; POST /api/v1/ideas/{id}/approve|revise|reject
- POST /api/v1/episodes; GET /api/v1/episodes/{id}; GET /api/v1/episodes/{id}/timeline
- POST /api/v1/episodes/{id}/render; GET /api/v1/jobs/{id}; POST /api/v1/jobs/{id}/cancel
- POST /api/v1/episodes/{id}/final-approval; POST /api/v1/episodes/{id}/publish
- GET /api/v1/budget; GET /api/v1/analytics; POST /api/v1/integrations/{provider}/connect
- POST /api/v1/telegram/webhook (validated secret header; callbacks verified)

Only health and read-only channel profiles are implemented in Phase 0; actual endpoints require auth and persistence.

## Reliability and visibility

- Structured logs with trace_id, episode_id, scene_id, provider, cost_estimate, actual cost, retry count, but NO secrets or raw private prompts.
- Queue jobs with deterministic idempotency keys, per-provider rate limits, deadlines, timeout policy, exponential backoff, circuit breakers, provider health checks.
- Cost alerts at 50/75/85/95/100%, and suspension of billable jobs when projected + reserved + charged exceeds cap.
- Save per-scene hashes, versioned prompts, seed, renderer version and model ID for reproducibility.
- Unit, API contract, state-machine, authorization, budget race, connector sandbox, scene render and end-to-end tests in CI.
- GitHub Actions reserved for lint, security scan, build and small tests; not an always-on renderer or long GPU tasks.

## Related docs

AI_AND_TOOLS.md; ANIMATION_PIPELINE.md; DATA_MODEL.md; BUDGET_AND_FINOPS.md; SECURITY_AND_POLICY.md; ROADMAP.md; GETTING_STARTED.md; REFERENCES.md.
