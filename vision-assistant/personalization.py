import json
from pathlib import Path

PROFILE_PATH = Path(__file__).parent / "user_profile.json"


def load_user_profile(path: Path = PROFILE_PATH) -> dict:
    """Load the user profile from JSON."""
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_user_profile(profile: dict, path: Path = PROFILE_PATH) -> None:
    """Save the user profile to JSON."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)


def enhance_personalization(profile: dict, preferences: dict) -> dict:
    """Update a user profile with additional preferences."""
    updated = profile.copy()
    updated.setdefault("preferences", {}).update(preferences)
    return updated


def get_personalized_settings(profile: dict) -> dict:
    """Return personalization settings derived from the profile."""
    return profile.get("preferences", {})
