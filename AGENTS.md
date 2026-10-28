# Engineering agent instructions — Zenix AI Studio

## Mission
Deliver a cloud-first 4-channel animation studio, controlled by native Windows Tauri .exe and Telegram, with an IDR 4m monthly operating target. Treat user-defined scope in docs/ARCHITECTURE.md and docs/CHANNELS_AND_CONTENT.md as authoritative. Keep exact repository name Zenik-AI-Agent-Auto-Channel.

## Non-negotiable
- Never promise that 8 full-animation uploads/month are achievable within IDR 4m until real cloud rendering benchmarks verify it. Never substitute mostly-still-image videos without explicit consent.
- Protect child viewers, editorial originality, historical sources, licensed assets, YouTube audience classification and synthetic reconstruction disclosure.
- Do not push secrets or test with real paid APIs without explicit approval, a working persistent budget ledger and provider caps.
- All new provider integrations default to dry-run/off. Require explicit operator approval for outbound private assets and final publication.
- Preserve tenant/channel isolation on API, database, storage and OAuth tokens. Telegram callback authorization is mandatory.
- Follow typed provider adapters, cost preauthorization, source-backed historical evidence, idempotent jobs and immutable approved render hash.
- Running a build does not imply a functioning production pipeline; update docs/IMPLEMENTATION_STATUS.md after each milestone.

## Design conventions
- Python 3.12+ for FastAPI/worker and domain; Pydantic v2; pytest; stable, pinned production dependencies.
- React + TypeScript for desktop; Tauri v2 on Windows; NO browser dashboard as the operator UI. Dev tooling may use loopback.
- All LLM outputs must validate against typed JSON schemas; never execute raw shell snippets produced by AI.
- Feature flags default off for paid calls, external publication and access to private uploaded data.
- Implement tests for budget concurrency and idempotency, workflow approval gates, Telegram spoofing, OAuth identity and safe render commands before deployment.
- Keep cloud tasks outside GitHub Actions; Actions manual/small checks only, avoid unnecessary quota use.

## Build sequence
1. Verify Phase 0 tests/build (do not assume they pass).
2. Implement authenticated PostgreSQL budget, row locking, reservations, outbox and billing reconciliation.
3. Implement Telegram proposal webhook/callback verification and scheduler (dry run).
4. Add bounded LLM router/research/citations and compliant scripts.
5. Godot/Blender 30–60s animation prototypes; cost-per-minute measurements.
6. Audio, editing, YouTube OAuth + upload, analytics, Windows installer release.

## Definition of done for every PR
- Implementation + tests + updated relevant documentation
- No secrets and no user data in logs
- No paid external calls in CI
- Explicit test evidence and remaining TODOs
- For UI: one-window desktop and real working control behavior; label nonworking elements DEMO
