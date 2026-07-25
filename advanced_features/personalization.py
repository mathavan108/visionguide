import copy
import json
from datetime import datetime
from pathlib import Path


class PersonalizationEngine:
    """Manage a user's navigation profile with persistence and simple updates."""

    DEFAULT_PROFILE = {
        "preferred_direction": "right",
        "walking_speed": "normal",
        "frequent_locations": [],
        "obstacle_history": {},
        "guidance_history": [],
        "last_updated": None,
    }

    def __init__(self, profile_path: Path | str = None) -> None:
        """Initialize the engine and load the user profile."""
        self.profile_path = Path(profile_path or Path(__file__).parent / "user_profile.json")
        self.profile = self.load_profile()

    def _default_profile(self) -> dict:
        """Return a fresh default profile dictionary."""
        return copy.deepcopy(self.DEFAULT_PROFILE)

    def load_profile(self) -> dict:
        """Load the profile from JSON, creating the file with defaults if needed."""
        if not self.profile_path.exists():
            default_profile = self._default_profile()
            default_profile["last_updated"] = self._current_timestamp()
            self._write_profile(default_profile)
            return default_profile

        with self.profile_path.open("r", encoding="utf-8") as profile_file:
            profile = json.load(profile_file)

        # Ensure the profile has all required fields with safe defaults.
        defaults = self._default_profile()
        for key, default_value in defaults.items():
            profile.setdefault(key, default_value)

        return profile

    def save_profile(self) -> None:
        """Save the current profile state to the JSON file."""
        self.profile["last_updated"] = self._current_timestamp()
        self._write_profile(self.profile)

    def update_location(self, location: str) -> None:
        """Record a new frequently visited location if it is not already stored."""
        if location and location not in self.profile["frequent_locations"]:
            self.profile["frequent_locations"].append(location)
            self.save_profile()

    def update_obstacle(self, obstacle: str) -> None:
        """Increase the obstacle count and save the updated profile."""
        if not obstacle:
            return

        self._increment_obstacle_count(obstacle)
        self.save_profile()

    def _increment_obstacle_count(self, obstacle: str) -> None:
        """Increment the count for a specific obstacle in history."""
        history = self.profile["obstacle_history"]
        history[obstacle] = history.get(obstacle, 0) + 1

    def update_guidance(self, message: str) -> None:
        """Append a guidance message to the history."""
        self.profile["guidance_history"].append(message)
        self.save_profile()

    def set_preferred_direction(self, direction: str) -> None:
        """Update the user's preferred walking direction."""
        self.profile["preferred_direction"] = direction
        self.save_profile()

    def get_preferred_direction(self) -> str:
        """Return the user's preferred walking direction."""
        return self.profile.get("preferred_direction", self.DEFAULT_PROFILE["preferred_direction"])

    def _write_profile(self, profile_data: dict) -> None:
        """Write the profile dictionary to the JSON file."""
        with self.profile_path.open("w", encoding="utf-8") as profile_file:
            json.dump(profile_data, profile_file, indent=2)

    @staticmethod
    def _current_timestamp() -> str:
        """Return the current timestamp in ISO format."""
        return datetime.utcnow().isoformat() + "Z"
