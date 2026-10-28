from zenik_core.workflow import Stage, can_advance


def test_approvals_cannot_be_skipped() -> None:
    assert can_advance(Stage.DRAFT_IDEA, Stage.PROPOSED)
    assert not can_advance(Stage.DRAFT_IDEA, Stage.RESEARCHED)
    assert can_advance(Stage.PROPOSED, Stage.IDEA_APPROVED)
    assert not can_advance(Stage.QC, Stage.UPLOAD_PENDING)
    assert can_advance(Stage.PREVIEW_READY, Stage.FINAL_APPROVED)
    assert can_advance(Stage.PREVIEW_READY, Stage.NEEDS_REVISION)
    assert not can_advance(Stage.PUBLISHED, Stage.DRAFT_IDEA)
