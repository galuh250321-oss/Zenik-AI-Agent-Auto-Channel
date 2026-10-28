# Local development and first steps

This starter is deliberately DRY RUN and free of paid API calls. The backend can run locally for developer testing, while the eventual operator UI will be a native Windows .exe and cloud workers will run on deployment infrastructure.

## Backend (Python 3.12+)
From repository root:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
uvicorn services.api.app.main:app --reload --port 8000
```

Read http://127.0.0.1:8000/health and http://127.0.0.1:8000/api/v1/channels in development. Production operators will not use a localhost dashboard; backend HTTP is only developer/server plumbing.

## Desktop prototype (Node 22+, Rust stable, Tauri prerequisites)
```bash
cd apps/desktop
npm install
npm run build
npm run tauri:dev
# Native Windows output, after successful prerequisite check:
npm run tauri:build
```

The initial UI intentionally displays an offline architecture preview and does NOT automatically connect to any cloud endpoint or store secrets. If the initial Tauri scaffold fails build, diagnose versions/prerequisites before enabling CI packaging.

## Next implementation sequence
1. Deploy PostgreSQL/Redis and a private development API.
2. Implement authenticated tenant/channel settings and atomic budget ledger in DB; add integration tests.
3. Create Telegram bot with BotFather, place token ONLY in secret manager, verify authorized chat ID and webhook secret; DRY RUN callbacks first.
4. Add one approved low-cost text provider adapter using a test key + server spend cap.
5. Build first storyboard and 30–60 s deterministic Godot render before purchasing generative video credits.
6. Connect YouTube OAuth with verified channel IDs, initially upload private with final human approval.
7. Profile actual cost per animation minute and raise output target only when budget gate passes.

## Repository workflow
Create focused branches, open PRs, require tests and code review. Keep main stable. GitHub Actions should run fast tests without paid API credentials by default, and Windows packaging only on a manual trigger or release tag to avoid unnecessary Actions minutes.

## Secrets
Copy .env.example to a local .env file for development, never commit the result. This starter does not read or use tokens yet.

## Build status
No production deployment, valid YouTube OAuth, autonomous animation engine, signed installer, or provider verification is claimed by this starter.
