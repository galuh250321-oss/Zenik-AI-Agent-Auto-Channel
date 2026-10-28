from zenik_core.channels import CHANNELS


def test_channel_isolation_duration_and_locales() -> None:
    assert set(CHANNELS) == {"moral-id", "moral-en", "history-id", "history-en"}
    for item in CHANNELS.values():
        assert item.min_duration_seconds < item.max_duration_seconds
    for id_ in ("moral-id", "moral-en"):
        assert (CHANNELS[id_].min_duration_seconds, CHANNELS[id_].max_duration_seconds) == (300, 420)
        assert CHANNELS[id_].made_for_kids_default
    for id_ in ("history-id", "history-en"):
        assert (CHANNELS[id_].min_duration_seconds, CHANNELS[id_].max_duration_seconds) == (600, 720)
        assert not CHANNELS[id_].made_for_kids_default
