# Budget Guardian — IDR 4,000,000/month

## Strict goal vs practical limits
Budget Guardian is an admission control for costs it can observe and authorize, NOT a guarantee that outside vendors cannot bill above IDR 4m. Provider subscriptions, queued credits, currency FX, tax, failed requests, delayed metering, cloud resources outside our controller, and disputed invoices can exceed an internal threshold. Configure real provider-side prepaid funds, hard stops, quota caps and anomaly alarms wherever available.

## Target allocations (planning figures, not observed quotes)
| Category | IDR |
|---|---:|
| Always-on CPU VPS, database and scheduler | 350000 |
| Research, writing, AI verification | 250000 |
| Image and character assets | 400000 |
| Multilingual voice/music/SFX | 300000 |
| On-demand Godot/Blender render compute | 1350000 |
| Optional paid video clips | 700000 |
| Storage, backups, bandwidth | 200000 |
| FX, tax, retry and unexpected charges reserve | 450000 |
| TOTAL | 4000000 |

Do not confuse monthly operating budget with one-time coding, expensive creation of original rigs/asset packs, external licensing fees, and ongoing development labor; quote these separately.

## Production target
- 4 channels; 2 unique moral stories + 2 unique history stories monthly.
- Localize to ID and EN -> 8 uploads/month if time and budget allow.
- Moral episodes 5–7 min; history episodes 10–12 min.
- 30–38 minutes of base/master animation for 60–76 minutes of published content. Actual language cut timing can differ.
- When render cost exceeds cap: reduce episode count, defer fancy clips or reuse approved animations; DO NOT silently shorten target duration or turn most content into still-image slideshow.

## Reservation ledger design (production)
PostgreSQL tables: budgets(scope: month, channel/provider, cap), transactions(RESERVE|COMMIT|RELEASE|ADJUST, currency, fx_rate, amount_idr, job_key, provider_ref, timestamp), spending_alerts.
1. Lock the relevant budget row with SELECT ... FOR UPDATE under SERIALIZABLE/appropriate isolation or optimistic compare-and-swap.
2. Compute committed + active reservations + new worst-case reservation; block if above total/channel/provider caps.
3. Store reservation and idempotency key transactionally; enqueue only after commit (transactional outbox).
4. On definitive provider result, reconcile actual amount and release remainder. If unknown, hold funds and mark requires_reconciliation.
5. Refund only using verifiable provider data; retries consume separate reservations; never double-charge the same idempotency key.
6. Fixed monthly accounting timezone Asia/Jakarta. Keep past months immutable and report currency conversion sources.
7. Prepaid/limit settings at each provider; auto-disable queue on credential/accounting anomalies.

## Channel caps (starting heuristic)
Moral ID/EN family: 1.2m combined; History ID/EN family: 2.3m combined; shared infrastructure + reserve: 0.5m, but category caps also apply. This distribution competes with category allocations; production must enforce a single global cap and avoid double-counting shared resources. Adjust based on real per-scene tests. Do not use these as additional free budget.

## Alerts
- 50%: summary; 75%: advisory; 85%: high priority Telegram; 95%: stop optional generative clips; 100%: no new billable work.
- Display charged / reserved / forecast / outside-controller subscriptions separately.
- Operator can lower caps immediately; raising the cap requires explicit confirmation and audit record.
- Paid jobs always fail closed if budget service or FX-rate source is unavailable.

## Phase 0 demo code
In-memory BudgetGuard illustrates reserve/commit/release behavior and is NOT concurrent, persistent, authenticated or suitable to protect actual money. Production requires atomic SQL implementation and billing integration before any paid provider adapter is enabled.
