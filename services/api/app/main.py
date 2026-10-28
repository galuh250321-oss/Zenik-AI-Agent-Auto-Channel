"""Phase 0 read-only developer API. No live integrations or paid calls."""

from fastapi import FastAPI
from zenik_core.channels import CHANNELS, ChannelProfile

app = FastAPI(
    title="Zenix AI Studio (Phase 0)",
    version="0.1.0",
    description="Read-only development endpoints. Authentication is required before enabling writes.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "dry-run", "phase": "0"}


@app.get("/api/v1/channels", response_model=list[ChannelProfile])
def list_channels() -> list[ChannelProfile]:
    """Public, non-secret example channel profiles only."""
    return list(CHANNELS.values())
