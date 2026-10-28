import pytest

from zenik_core.budget import BudgetExceeded, BudgetGuard, InvalidReservation


def test_reserve_commit_and_remaining_cap() -> None:
    g = BudgetGuard(4_000_000)
    g.reserve(job_key="shot-001", channel_id="moral-id", amount_idr=150_000)
    assert g.snapshot()["reserved_idr"] == 150_000
    g.commit("shot-001", 70_000)
    assert g.snapshot() == {
        "cap_idr": 4_000_000, "committed_idr": 70_000,
        "reserved_idr": 0, "available_idr": 3_930_000,
    }


def test_total_cap_fail_closed_and_idempotent() -> None:
    g = BudgetGuard(100_000)
    first = g.reserve(job_key="a", channel_id="history-id", amount_idr=70_000)
    assert g.reserve(job_key="a", channel_id="history-id", amount_idr=70_000) is first
    with pytest.raises(BudgetExceeded):
        g.reserve(job_key="b", channel_id="history-id", amount_idr=30_001)
    with pytest.raises(InvalidReservation):
        g.reserve(job_key="a", channel_id="history-id", amount_idr=60_000)


def test_per_channel_cap_and_release() -> None:
    g = BudgetGuard(100_000, {"moral-id": 20_000})
    g.reserve(job_key="a", channel_id="moral-id", amount_idr=18_000)
    with pytest.raises(BudgetExceeded):
        g.reserve(job_key="b", channel_id="moral-id", amount_idr=3_000)
    g.release("a")
    assert g.snapshot()["available_idr"] == 100_000


@pytest.mark.parametrize("invalid", [-1, 1.1, "NaN", "Infinity", "2.5", True])
def test_invalid_amount_rejected(invalid) -> None:
    g = BudgetGuard()
    with pytest.raises(InvalidReservation):
        g.reserve(job_key="x", channel_id="moral-id", amount_idr=invalid)


def test_actual_cannot_exceed_reserved() -> None:
    g = BudgetGuard(10_000)
    g.reserve(job_key="r", channel_id="history-id", amount_idr=3_000)
    with pytest.raises(BudgetExceeded):
        g.commit("r", 3_001)
    assert g.snapshot()["reserved_idr"] == 3_000
