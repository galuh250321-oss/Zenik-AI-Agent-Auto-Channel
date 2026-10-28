from fastapi.testclient import TestClient

from services.api.app.main import app


def test_health_and_channels() -> None:
    client = TestClient(app)
    assert client.get("/health").json() == {"status": "ok", "mode": "dry-run", "phase": "0"}
    response = client.get("/api/v1/channels")
    assert response.status_code == 200
    assert len(response.json()) == 4
    assert all("min_duration_seconds" in c for c in response.json())


def test_no_publish_endpoint_exposed_in_phase_zero() -> None:
    client = TestClient(app)
    assert client.post("/api/v1/episodes/123/publish").status_code == 404
