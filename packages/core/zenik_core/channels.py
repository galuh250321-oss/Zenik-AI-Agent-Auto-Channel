"""Channel-specific editorial profiles; real YouTube IDs are configured later."""

from typing import Literal

from pydantic import BaseModel, Field


class ChannelProfile(BaseModel):
    id: str
    name: str
    category: Literal["kids_manners", "history"]
    language: Literal["id", "en"]
    audience: str
    min_duration_seconds: int = Field(ge=1)
    max_duration_seconds: int = Field(ge=1)
    made_for_kids_default: bool
    visual_style: str


CHANNELS: dict[str, ChannelProfile] = {
    "moral-id": ChannelProfile(
        id="moral-id", name="Moral & Adab Indonesia", category="kids_manners",
        language="id", audience="anak 4–10 tahun",
        min_duration_seconds=300, max_duration_seconds=420,
        made_for_kids_default=True, visual_style="original rigged 2D animated cartoon",
    ),
    "moral-en": ChannelProfile(
        id="moral-en", name="Good Manners & Values", category="kids_manners",
        language="en", audience="children ages 4–10",
        min_duration_seconds=300, max_duration_seconds=420,
        made_for_kids_default=True, visual_style="original rigged 2D animated cartoon",
    ),
    "history-id": ChannelProfile(
        id="history-id", name="Sejarah Nusantara", category="history",
        language="id", audience="remaja dan dewasa",
        min_duration_seconds=600, max_duration_seconds=720,
        made_for_kids_default=False, visual_style="cinematic animated history",
    ),
    "history-en": ChannelProfile(
        id="history-en", name="Epic History", category="history",
        language="en", audience="teenagers and adults",
        min_duration_seconds=600, max_duration_seconds=720,
        made_for_kids_default=False, visual_style="cinematic animated history",
    ),
}
