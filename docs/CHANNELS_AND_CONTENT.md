# Channel profiles and editorial separation

## The four channels

| Channel ID | Editorial brand (working name) | Audience | Language | Duration | Content |
|---|---|---|---|---|---|
| moral-id | Moral & Adab Indonesia | children approximately 4–10 | Indonesian | 5–7 min | original everyday stories, empathy, honesty, respect, helpfulness |
| moral-en | Good Manners & Values | children approximately 4–10 | English | 5–7 min | culturally adapted original stories and social-emotional learning |
| history-id | Sejarah Nusantara | teens/adults | Indonesian | 10–12 min | kingdoms, wars, historical figures, civilizations |
| history-en | Epic History | teens/adults | English | 10–12 min | world empires, conflict, historical strategy and civilizations |

## Channel persona data (future database)
channel_id, verified_youtube_channel_id, content_vertical, locale, target_audience, made_for_kids_default, preferred_visual_style, narration_voice_id, recurring_characters, scene_library, age_safety_profile, script_template_version, historical_source_policy, proposal_cadence, production_priority, monthly_subcap_idr, approved_release_schedule, publishing_enabled, last_upload_id.

## Story family vs distinct releases
master_story has one editorial thesis and shared animation assets; localizations become independent scripts, audio, captions, thumbnails, metadata and approvals. Do not auto-upload mirrored low-value content; enforce meaningful localization and originality review. Disclose synthetic/realistic reconstructions where platform requires.

## Kids editorial guard
Age-appropriate, non-threatening, constructive themes; human approve final cut, avoid manipulative engagement, frightening characters, violent punishment, inappropriate product placements and licensed character copying. Mark Made for Kids based on actual intended audience and YouTube criteria, not channel title alone.

## History editorial guard
Every material historical assertion must link to one or more identifiable sources, marked confidence, counter-evidence where relevant; contested claim approval; differentiate dramatization from recorded evidence. Action scenes depict violence contextually, avoid gratuitous gore, no ideological glorification. Use geography/epoch-aware maps with uncertainty notes.

## Ideation signals
Collect channel-owned analytics and YouTube public search only in allowed quota/ToS bounds, plus evergreen editorial calendars. Never promise that a trend is currently popular without checked evidence. Store prior episode themes/fingerprints to prevent formulaic duplication.

## Telegram proposal contract
{ proposal_id, channel_id, title, logline, genre, hook, synopsis, scene_outline, key_message, target_duration_seconds, language, sources[], historical_confidence, kid_safety_flags[], estimated_cost_idr, estimated_completion_class, possible_localizations[], expiry_at }.
Callbacks: VIEW, APPROVE_IDEA, REQUEST_REVISION, REJECT, APPROVE_FINAL, PAUSE. Verify chat sender, action token, state, channel mapping, deadline and nonce server side. Telegram messages never carry OAuth credentials.

## Frequency
Pilot: 4 masters/month, localized to 8 uploads. Proposal suggestions can be sent more often than publishing. Pausing one channel must not cause another to spend its budget.
