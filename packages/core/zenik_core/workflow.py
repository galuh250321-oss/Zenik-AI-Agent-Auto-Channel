"""Explicit domain state machine, deliberately without side effects."""

from enum import StrEnum


class Stage(StrEnum):
    DRAFT_IDEA = "draft_idea"
    PROPOSED = "proposed"
    IDEA_APPROVED = "idea_approved"
    RESEARCHED = "researched"
    SCRIPT_READY = "script_ready"
    STORYBOARD_READY = "storyboard_ready"
    ASSETS_READY = "assets_ready"
    ANIMATING = "animating"
    EDITING = "editing"
    QC = "qc"
    PREVIEW_READY = "preview_ready"
    FINAL_APPROVED = "final_approved"
    UPLOAD_PENDING = "upload_pending"
    UPLOADED = "uploaded"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    ANALYZED = "analyzed"
    NEEDS_REVISION = "needs_revision"
    FAILED_RETRYABLE = "failed_retryable"
    FAILED_FINAL = "failed_final"
    CANCELED = "canceled"


ORDER = [
    Stage.DRAFT_IDEA, Stage.PROPOSED, Stage.IDEA_APPROVED, Stage.RESEARCHED,
    Stage.SCRIPT_READY, Stage.STORYBOARD_READY, Stage.ASSETS_READY,
    Stage.ANIMATING, Stage.EDITING, Stage.QC, Stage.PREVIEW_READY,
    Stage.FINAL_APPROVED, Stage.UPLOAD_PENDING, Stage.UPLOADED,
    Stage.SCHEDULED, Stage.PUBLISHED, Stage.ANALYZED,
]


def can_advance(current: Stage, next_stage: Stage) -> bool:
    """Basic forward graph; no automatic approval or skipping gates."""
    try:
        index = ORDER.index(current)
    except ValueError:
        return False
    if index + 1 < len(ORDER) and ORDER[index + 1] == next_stage:
        return True
    if current in (Stage.PROPOSED, Stage.SCRIPT_READY, Stage.QC, Stage.PREVIEW_READY):
        return next_stage == Stage.NEEDS_REVISION
    if current not in (Stage.PUBLISHED, Stage.ANALYZED):
        return next_stage in (Stage.CANCELED, Stage.FAILED_RETRYABLE, Stage.FAILED_FINAL)
    return False
