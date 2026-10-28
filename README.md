# Zenix AI Studio — Auto Channel

Cloud-first AI animation studio with a native Windows desktop controller, Telegram approvals, and four separate YouTube channels. **Status: architecture + Phase 0 starter only; NOT production-ready.**

## Scope
- Moral & Adab ID / EN: 5–7 minute animated episodes.
- History ID / EN: 10–12 minute animated documentaries for teens and adults.
- Pilot target: 4 original stories/month localized to 8 uploads (subject to real render cost and quality tests).
- Monthly operating ceiling: **IDR 4,000,000** with budget reservation, per-channel allocations, provider limits, and fail-closed paid jobs.
- Full-cloud execution, optional Tauri desktop monitoring, Telegram ideation/approval, human approval before publishing.

## Start here
1. Read [full architecture](docs/ARCHITECTURE.md), [AI/tools](docs/AI_AND_TOOLS.md), [budget model](docs/BUDGET_AND_FINOPS.md), and [roadmap](docs/ROADMAP.md).
2. Follow [developer setup](docs/GETTING_STARTED.md).
3. Read [security and policy controls](docs/SECURITY_AND_POLICY.md) before connecting real accounts or spending money.

## Implementation state
Phase 0 includes an API skeleton, configuration-driven channel registry, cost reservation demo, tests, and desktop prototype scaffolding. It does **not** yet render animation, call AI providers, persist a production ledger, connect YouTube OAuth, or publish content. Those are tracked in the roadmap.

## Important safety
Never commit API keys, OAuth refresh tokens, Google service credentials, Telegram bot tokens, user uploads, or rendered assets. Production must use secret management, authenticated access, scoped permissions, and provider-side billing caps where possible.

## License
No license granted until one is explicitly chosen. For internal evaluation only.
