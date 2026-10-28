# AI providers, tools, and coding choices

All names below are candidate adapters to verify against the actual authenticated provider model list, API contracts, commercial licensing and current pricing before purchase. Do NOT assume that a custom reseller model (including DeepSeek V4.1 Flash Uncensored) is officially available from DeepSeek or has a stable contract.

| Function | Primary candidate | Alternative | Work product |
|---|---|---|---|
| Content strategist, ideation | authorized low-cost DeepSeek-compatible chat endpoint | Gemini Flash / other cost-approved LLM | proposal JSON |
| Historical researcher | search/retrieval tool + LLM | second independent LLM | references, evidence ledger |
| Fact checker | deterministic source citation checks + separate LLM | human review when uncertain | claim verdicts |
| Story/script/storyboard | stronger writing LLM through router | fallbacks selected on price/quality | bilingual structured scenes |
| Localization | low-cost multilingual LLM | human edits | ID/EN adaptation, not literal dub |
| Child safety/editorial | heuristics + second model | human gate | safety report |
| Character & backgrounds | permitted image generation API | human-made, licensed original assets | character sheets and sets |
| Rigged animation | Godot 4, GDScript, imported 2D rigs | Blender Grease Pencil / 2D | genuinely moving scenes |
| Cinematic history | Blender Python + rigged assets, animated maps | Godot 3D | reproducible historical sequences |
| Exceptional shots | optional Runway/Kling or alternative approved video API | Blender procedural | selected short clips only |
| Narration / character voices | cost-qualified multilingual cloud TTS | ElevenLabs or licensed TTS provider | ID/EN speech |
| Lip sync | local/cloud CPU phoneme alignment + rig mouth shapes | dedicated service | timeline driven visemes |
| Music / effects | licensed commercial-use audio library | commissioned/original assets | legal audio |
| Editing / export | FFmpeg | Blender VSE | 1080p MP4, SRT, thumbnail |
| Operator messaging | Telegram Bot API | desktop push | proposal + approval |
| Publishing / insights | YouTube Data & Analytics APIs | manual Studio workflow | uploads, stats |
| Cloud | VPS CPU + object storage + ephemeral renderer | provider-specific GPU jobs | reliable jobs |

## Provider interface contract
All adapters implement estimate(input), validate_capability(input), run(input, idempotency_key), normalize_usage(result), and reconcile_usage(result). Include published model ID, currency, units, rate_version, provider request ID, retry policy and license metadata. Unknown estimates must require manual approval instead of quietly charging.

## Provider routing policy
- Cheap deterministic operations first: scripts, retrieval cache, FFmpeg, timeline math.
- Escalate LLM complexity only for writing/verification; use a second independent check on contested history.
- Check policy and cost cap BEFORE request; reserve worst-case spend, including allowed retries.
- Never fallback to an unapproved provider, or send private assets to a different provider without consent.
- Key storage via managed secret service; no runtime arbitrary code from LLM directly on render fleet. Model output is typed JSON validated against strict schemas and allowlisted commands.

## Animated film quality reality
A fully automated Godot/Blender pipeline requires original/rights-cleared rigs, reusable action library, facial animation, camera grammar, procedural staging, asset consistency checks, voice alignment, and QA. These are not bundled by merely installing Godot or Blender. Full-length quality must be benchmarked via 30–60 s pilots, then 5–7/10–12 min episode proof. Never claim fixed win rate, perfect photoreal historical accuracy, or guaranteed earnings.

## Development language and package boundaries
- apps/desktop: React 19-ish + Vite + TypeScript + Tauri v2; pin tested versions once bootstrap is installed.
- services/api: Python 3.12+, FastAPI, Pydantic v2, SQLAlchemy, Alembic (later).
- packages/core: domain state machine, budget ledger/admission, data schemas, provider contracts.
- workers: Python workers for research/voice/renders/upload; integration test fakes.
- infrastructure: Docker Compose locally for server, later managed PostgreSQL + Redis + S3.
- CI: Python pytest, type checks, eslint, Tauri check/build on Windows only after bootstrap and feature tests.

## Do not overbuy
Start without paid image/video APIs. First prove Telegram idea suggestions and dry-run budget and a small deterministic Godot animation. Add paid adapters one by one only after cost and rights review.
