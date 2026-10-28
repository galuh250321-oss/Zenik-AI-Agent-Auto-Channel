"""Contract only; Phase 0 never makes paid provider calls."""

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class ProviderEstimate:
    provider: str
    model: str
    estimated_max_idr: int
    rate_version: str


@dataclass(frozen=True)
class ProviderResult:
    provider_request_id: str
    content: dict[str, Any]
    metered_cost_idr: int | None


class Provider(Protocol):
    def estimate(self, payload: dict[str, Any]) -> ProviderEstimate: ...
    def run(self, payload: dict[str, Any], *, idempotency_key: str) -> ProviderResult: ...
