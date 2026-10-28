# Backend contracts and event routing (implementation specification)

Only /health and GET /api/v1/channels currently exist. Everything below is planned and should NOT be treated as implemented.

## Auth
Cloud API: short-lived access token with channel RBAC and server-side refresh token handling; operator session/device management; CSRF/state protection on OAuth redirects; auditable approvals. Telegram calls require verified webhook secret and allowlisted user/chat IDs.

## Suggested endpoint contracts
- POST /api/v1/ideas/suggest {channel_ids, proposal_count, month} => 202 job ID; requires auth.
- GET /api/v1/ideas?channel_id=... => paginated proposals with source/evidence references.
- POST /api/v1/ideas/{id}/decision {decision: approve|revise|reject, revision_text?, expected_version, action_nonce} => audit ID.
- POST /api/v1/episodes/{id}/plan => structure/storyboard; validates budget forecast.
- POST /api/v1/episodes/{id}/render {version, preset, approval_id} => 202 job ID only after budget RESERVE.
- GET /api/v1/jobs/{id} => status, cost estimate/reserved/actual, active shot/attempt.
- POST /api/v1/episodes/{id}/approval {render_sha256, channel_id, decision, approved_metadata_hash} => immutable approved release.
- POST /api/v1/episodes/{id}/upload {approval_id, publish_at?} => 202 job ID, resumable upload and verification.
- GET /api/v1/budget?month=YYYY-MM => booked/reserved/charged/outside-system, caps and forecast.
- POST /api/v1/telegram/webhook => Telegram update authenticated by X-Telegram-Bot-Api-Secret-Token.

## Provider request schema
{provider, model_id, task_type, input_refs, policy_flags, max_cost_idr, idempotency_key, rate_version, deadline_at, retry_allowance}. Responses {request_id, model_id, output_refs, usage_units, cost_actual_or_pending, confidence, license_data, error_type}.

## Job envelope
{job_id, tenant_id, channel_id, episode_id, content_version, stage, attempts, correlation_id, idempotency_key, reserved_budget_txn_id, initiated_by, started_at, deadline_at, metadata_hash}. Do not accept free-form shell commands from untrusted workers.

## Durable events (outbox)
idea.proposed, idea.approved, script.ready, research.needs_review, budget.reserved, budget.blocked, shot.rendered, qc.failed, preview.ready, episode.final_approved, youtube.uploaded, youtube.published, episode.canceled. Each has schema_version, event_id, timestamp and correlation_id. Consumer deduplicates event IDs.

## Publication proof
Required fields: verified_channel_id, OAuth subject scope, episode_version, video SHA256, human approval with same SHA256, title/description hash, disclosure flags, audience designation, intended schedule, uploader trace ID, platform video ID. Nonmatching version or deleted approval => reject.

## Failure semantics
Timeout before provider result: do NOT release reservation automatically; mark disputed and reconcile. Job retries are idempotent and bounded. Ambiguous YouTube upload response: query platform for known upload/video identity before uploading again. Fail closed if telemetry or auth incomplete.
