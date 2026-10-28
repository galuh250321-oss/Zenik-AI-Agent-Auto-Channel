# Data model and state integrity (proposed)

Planned PostgreSQL entities and cardinality:
- users, sessions, roles, actor_scopes (RBAC)
- channels (per-user ownership, YouTube verified ID), channel_settings, oauth_credentials (encrypted provider references)
- story_masters -> localized_episodes, proposals, scripts, script_versions
- research_sources, historical_claims, claim_evidence, editorial_reviews
- character_assets, set_assets, rights_registry, scene_manifests, shots, render_assets
- jobs, job_attempts, job_outbox, idempotency_keys, qc_reports
- approval_decisions, review_links, youtube_uploads, publishing_events
- budgets, cost_reservations, actual_charges, transaction_ledger, provider_rates, expense_forecasts
- connector_states, webhook_events, audit_events, analytics_snapshots

## Required invariants
- channel_id present on scoped tables and included in authorization check before database queries.
- Only one successful production job for each episode/version/step/idempotency_key.
- Video cannot be published if final approved render hash differs from current output.
- Research claims link to evidence and citations or are explicitly marked dramatized/unverified.
- Budget reconciliation never mutates ledger history; record compensating transactions.
- YouTube upload stores OAuth verified channel id, upload ID, episode_version, submitted metadata hash; retries must not duplicate published videos.
- Telegram callbacks validated with expiration and one-time nonce; actions auditable.
- Object storage references use signed URLs and expire; raw public bucket access forbidden.

## Sequence (production)
POST suggestion request -> proposal queued -> stored proposal -> Telegram callback -> transaction captures approval -> outbox creates research job -> validated script version -> scene assets -> render jobs -> QC -> immutable preview -> final approval -> upload/resumable finalize -> status verify -> schedule/publish -> analytics snapshot.
