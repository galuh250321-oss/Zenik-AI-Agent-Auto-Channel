# Full animation pipeline and rendering proof plan

## Definition of full animation
The primary timeline must consist of deliberately animated characters/objects, staged actions, real facial expressions, mouth shapes, environment animation, animated maps and camera cuts. Simple Ken Burns pan over still images is not counted as meaningful full animation. It is acceptable for occasional explanatory archival images in history docs, explicitly labelled.

## Kids engine
Asset bible -> original character sheet -> vector/mesh parts -> standardized 2D skeletal rig -> movement/action library (idle, walk, run, gesture, sit, grab, interact) -> face and phoneme/viseme library -> script scene blocks -> animation timeline -> low-res animatic -> Godot Movie Maker export -> FFmpeg mix and H.264 MP4. Ensure silhouettes and expressions stay consistent from shot to shot.

## History engine
Evidence-based environment kit -> Blender geometry/rigged historical characters (no exact historical depiction claims without basis) -> procedural crowds/formation animation -> configurable map routes using Godot or Blender -> camera path lighting -> render passes -> FFmpeg composite. Map timeline must reflect verified boundaries and flag uncertainty. Keep violence contextual and non-graphic.

## Shot schema contract
shot_id, duration_frames, fps, renderer, character_asset_hashes, location_asset_id, pose_actions[{asset_id,start_frame,end_frame,blend}], camera_keyframes, dialogue_clip_ref, phoneme_timeline, effects[], historical_claim_refs[], estimated_gpu_seconds, resolution, source/license metadata. Strict schema validation and asset allowlisting; no arbitrary LLM-generated shell commands.

## Scene economics
Cache at scene and shot granularity: hash(project + rig + action timeline + audio alignment + render settings + engine version). On audio-only changes, reuse base image/animation where possible and rerender lip sync/mix selectively. Track seconds/frame, time cost, retries, audio cost, failures. Auto-quality scoring is advisory, not a substitute for human review.

## Localization
One approved master animation plus independent ID/EN script timing, TTS, viseme tracks, subtitles, intro/outro and thumbnail; adjust timing if translated voice cannot fit scene. Both releases require editorial approval and unique metadata. Avoid duplicated uploads without meaningful audience value.

## Pilot acceptance gates
- Pilot A: 30–60 s original animated kids scene with visible movement in >=90% of non-title shots; correct bilingual timing.
- Pilot B: 30–60 s historical scene with animated map, moving subjects, safe action and evidence ledger.
- Repeatable rendering with logs, valid MP4, captions and licensed audio; compare one-try, 2-try and 3-try economics.
- Measure cost of complete 5–7 minute kids and 10–12 minute history master episodes; do not declare budget feasible before tests.
- Final render target 1920x1080 H.264/AAC (adjust to hardware/provider constraints). Scene preview can use 720p.
