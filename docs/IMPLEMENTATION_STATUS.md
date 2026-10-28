# Implementation status — 2026-10-28

This is a point-in-time engineering status, NOT a product launch announcement.

| Component | Status | Evidence / limitations |
|---|---|---|
| 4 channel editorial profiles | Implemented as static code | packages/core/zenik_core/channels.py |
| Duration targets | Implemented as static code | 300–420 s kids, 600–720 s history |
| FastAPI read-only health and channels | Code written | services/api/app/main.py; tests added; runtime not yet CI-verified |
| Budget Guardian | In-memory demonstration | no SQL, multi-process lock, external billing, or actual cash enforcement |
| Domain workflow | Basic transition validator | not yet persisted or bound to user approvals |
| AI provider interface | Protocol defined | no live provider adapters; no API keys required |
| Desktop Tauri/React | Scaffold + preview UI written | not yet compiled/tested on Windows |
| Native installer | NSIS configuration written | NO .exe artifact built yet |
| Telegram bot | Planned | no token/webhook |
| Scheduled research & LLM writing | Planned | no scheduler or live calls |
| Godot/Blender full animation | Planned | no rig/assets/worker yet |
| TTS/audio/edit pipeline | Planned | no renderer/audio service |
| YouTube OAuth/upload | Planned | no credentials, account connection or upload |
| Real cloud deployment | Planned | no VPS/GPU/storage provisioned |
| Automated CI | Manual workflow provided | no claim it was executed |

## Next immediate verification
Execute manually: Python backend tests and frontend TypeScript build. Fix any failures and record commit SHA + passing output. Build Windows NSIS only after prerequisites are installed and frontend build passes. Next actual feature PR: transactional PostgreSQL Budget Guardian and Telegram dry-run proposal approval.

## Zero-cost safety
No paid APIs, YouTube upload or Telegram sends are invoked by the Phase 0 server or desktop UI. Tauri UI budget slider is only a visual demo and cannot cap external provider bills.
