# Security, privacy, and YouTube platform controls

## Threat model
Attackers can forge Telegram callbacks, steal leaked bot/OAuth tokens, inject hostile webpage content into research, swap preview assets, access another channel, manipulate render input into arbitrary command execution, or cause unexpected cloud spend.

## Controls
- Encrypt service credentials and OAuth refresh tokens at rest using cloud secret manager/KMS; do not place tokens in Git, README, screenshots, browser localStorage or model prompts.
- Backend auth is mandatory before connecting real accounts; least-privilege scopes and server-side channel identity binding. OAuth flow uses state and PKCE where supported; verified redirect URI; revoke/disconnect support.
- Telegram webhook secret header, allowed Telegram user IDs, callback nonce/expiry, per-action audit and rate limiting. Reject callbacks from unauthorized chats.
- Web search results and retrieved archives are untrusted data, not instructions. Strip executable prompts from context; cite source URLs, keep review history.
- Render worker runs as unprivileged container with restricted mounts/network, resource limits and allowlisted tools. Never execute arbitrary LLM shell commands.
- User-uploaded assets: content-type validation, file size limits, malware scan, transcoding, license/provenance tags. Outbound personal/private file transfer requires explicit permission.
- Segment kids assets and account tokens by channel; multi-channel RBAC checked on every request.
- Limit public previews with signed expirations; preview videos may include watermark and should never be indexed.
- Logging must redact credentials and personal data. Keep auditable budget events and security alerts.
- Use encrypted HTTPS connections, backups and recovery drills; no untrusted packages or floating dependency versions in production.

## Policy gates
- Evaluate Made for Kids designation per release (both child channel profiles likely require it); follow current YouTube rules, local child privacy duties and upload metadata.
- Evaluate altered/synthetic media disclosure for realistic historical recreation.
- Originality and reused-content checks: localizations should adapt narration, cultural context, packaging and editorial choices; no guarantees of monetization.
- Historical violent scenes require educational context and age-safety review; avoid graphic gore.
- All music, visuals and voice likenesses require verified commercial rights, attribution rules and record of license.
- YouTube API quota, OAuth verification and project audit may restrict automatic public publishing. Offer manual fallback rather than circumventing gates.
- Developer should check current YouTube developer policies again before production launch, not assume past documentation stays current.

## Hard stops
No auto-publish without final approval in default mode. No paid provider calls when estimated cost unavailable, budget enforcement offline, or no provider-side spend visibility. No automatic uploads with unverified channel binding. No secrets sent to unapproved AI models.
