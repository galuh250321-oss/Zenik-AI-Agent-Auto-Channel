"""Dry-run budget gate. NOT a production financial control: no SQL persistence.

This module prevents duplicate reservations in one process and is useful for
domain tests. Real money MUST use transactional PostgreSQL and provider-side caps.
"""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from threading import RLock


class BudgetExceeded(ValueError):
    pass


class InvalidReservation(ValueError):
    pass


def _amount(value: int | str | Decimal) -> Decimal:
    if isinstance(value, float) or isinstance(value, bool):
        raise InvalidReservation("Use integer IDR or Decimal, never floating point.")
    try:
        amount = Decimal(value)
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise InvalidReservation("Invalid IDR amount.") from exc
    if not amount.is_finite() or amount < 0 or amount != amount.to_integral_value():
        raise InvalidReservation("IDR amount must be a nonnegative whole number.")
    return amount


@dataclass(frozen=True)
class Reservation:
    job_key: str
    channel_id: str
    reserved_idr: Decimal
    status: str = "reserved"
    actual_idr: Decimal = Decimal(0)


class BudgetGuard:
    def __init__(
        self,
        monthly_cap_idr: int = 4_000_000,
        channel_caps_idr: dict[str, int] | None = None,
    ) -> None:
        self._lock = RLock()
        self.cap = _amount(monthly_cap_idr)
        self.channel_caps = {k: _amount(v) for k, v in (channel_caps_idr or {}).items()}
        self._reservations: dict[str, Reservation] = {}

    def _total_exposure(self) -> Decimal:
        return sum(
            (r.reserved_idr if r.status == "reserved" else r.actual_idr)
            for r in self._reservations.values()
            if r.status != "released"
        )

    def _channel_exposure(self, channel_id: str) -> Decimal:
        return sum(
            (r.reserved_idr if r.status == "reserved" else r.actual_idr)
            for r in self._reservations.values()
            if r.channel_id == channel_id and r.status != "released"
        )

    def reserve(self, *, job_key: str, channel_id: str, amount_idr: int) -> Reservation:
        if not job_key.strip() or not channel_id.strip():
            raise InvalidReservation("job_key and channel_id are required.")
        amount = _amount(amount_idr)
        with self._lock:
            existing = self._reservations.get(job_key)
            if existing is not None:
                if existing.channel_id != channel_id or existing.reserved_idr != amount:
                    raise InvalidReservation("Conflicting idempotency key.")
                return existing
            if self._total_exposure() + amount > self.cap:
                raise BudgetExceeded("Monthly budget exceeded.")
            channel_cap = self.channel_caps.get(channel_id)
            if channel_cap is not None and self._channel_exposure(channel_id) + amount > channel_cap:
                raise BudgetExceeded("Channel budget exceeded.")
            record = Reservation(job_key=job_key, channel_id=channel_id, reserved_idr=amount)
            self._reservations[job_key] = record
            return record

    def commit(self, job_key: str, actual_idr: int) -> Reservation:
        actual = _amount(actual_idr)
        with self._lock:
            previous = self._reservations.get(job_key)
            if previous is None or previous.status != "reserved":
                raise InvalidReservation("A pending reservation is required.")
            if actual > previous.reserved_idr:
                raise BudgetExceeded("Actual spend exceeds reservation; requires escalation.")
            result = Reservation(
                job_key=job_key, channel_id=previous.channel_id,
                reserved_idr=previous.reserved_idr, status="committed", actual_idr=actual,
            )
            self._reservations[job_key] = result
            return result

    def release(self, job_key: str) -> Reservation:
        with self._lock:
            previous = self._reservations.get(job_key)
            if previous is None or previous.status != "reserved":
                raise InvalidReservation("Only pending reservations may be released.")
            result = Reservation(
                job_key=job_key, channel_id=previous.channel_id,
                reserved_idr=previous.reserved_idr, status="released",
            )
            self._reservations[job_key] = result
            return result

    def snapshot(self) -> dict[str, int]:
        with self._lock:
            committed = sum((r.actual_idr for r in self._reservations.values()
                             if r.status == "committed"), Decimal(0))
            reserved = sum((r.reserved_idr for r in self._reservations.values()
                            if r.status == "reserved"), Decimal(0))
            return {
                "cap_idr": int(self.cap),
                "committed_idr": int(committed),
                "reserved_idr": int(reserved),
                "available_idr": int(self.cap - committed - reserved),
            }
