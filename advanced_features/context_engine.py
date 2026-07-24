from pathlib import Path
from typing import Dict, List

from .personalization import PersonalizationEngine

SUPPORTED_OBJECTS = [
    "person",
    "chair",
    "door",
    "table",
    "wall",
    "stairs",
    "empty path",
]

ENVIRONMENT_KEYWORDS = {
    "corridor": "Proceed straight.",
    "classroom": "Navigate carefully between desks.",
    "office": "Move deliberately and watch for office furniture.",
    "outdoor": "Walk carefully and stay alert.",
    "staircase": "Take the staircase with caution and use the handrail.",
    "doorway": "Approach the doorway and proceed through it safely.",
}

OBJECT_PROMPTS = {
    "person": "Person ahead.",
    "chair": "Chair ahead.",
    "door": "Door ahead.",
    "table": "Table ahead.",
    "wall": "Wall ahead.",
    "stairs": "Stairs ahead.",
    "empty path": "Path ahead.",
}


def normalize_text(text: str) -> str:
    """Normalize text for simple keyword matching."""
    return text.lower().strip()


def extract_objects(scene_description: str) -> List[str]:
    """Extract supported objects from a scene description."""
    normalized = normalize_text(scene_description)
    found_objects = [obj for obj in SUPPORTED_OBJECTS if obj in normalized]
    return found_objects


def extract_environment(scene_description: str) -> str:
    """Recognize the environment from the scene description."""
    normalized = normalize_text(scene_description)
    for keyword in ENVIRONMENT_KEYWORDS:
        if keyword in normalized:
            return keyword
    return ""


def determine_obstacle_priority(objects: List[str]) -> List[str]:
    """Order scene objects so obstacles appear first for rule-based guidance."""
    priority = ["wall", "stairs", "person", "chair", "table", "door", "empty path"]
    return [obj for obj in priority if obj in objects]


def load_user_profile(profile_path: Path | str = None) -> Dict[str, str]:
    """Load a complete user profile using the personalization engine."""
    engine = PersonalizationEngine(profile_path=profile_path) if profile_path else PersonalizationEngine()
    return engine.profile


def choose_navigation_action(objects: List[str], preferred_direction: str) -> str:
    """Choose a navigation action based on scene objects and preferred direction."""
    ordered_objects = determine_obstacle_priority(objects)
    direction = "right" if preferred_direction.lower() == "right" else "left"

    if not ordered_objects:
        return "No obstacles detected; proceed along the empty path."

    if ordered_objects == ["empty path"]:
        return "The path is clear; continue forward."

    primary_obstacle = ordered_objects[0]
    prompt = OBJECT_PROMPTS.get(primary_obstacle, "Obstacle ahead.")

    if primary_obstacle in {"wall", "stairs"}:
        return f"{prompt} Move slightly {direction}."
    if primary_obstacle == "person":
        return f"{prompt} Move slightly {direction} and maintain distance."
    if primary_obstacle in {"chair", "table"}:
        return f"{prompt} Move slightly {direction}."
    if primary_obstacle == "door":
        return f"{prompt} Move slightly {direction} toward it."

    return f"{prompt} Move slightly {direction}."


def combine_guidance(environment: str, object_guidance: str) -> str:
    """Combine environment guidance with object-level navigation advice."""
    environment_guidance = ENVIRONMENT_KEYWORDS.get(environment, "")
    if environment_guidance and object_guidance:
        return f"{environment_guidance} {object_guidance}"
    return environment_guidance or object_guidance


def generate_guidance(scene_description: str, user_profile: Dict[str, str] = None) -> str:
    """Generate personalized navigation guidance from a scene description."""
    if user_profile is None or "preferred_direction" not in user_profile:
        user_profile = load_user_profile()

    environment = extract_environment(scene_description)
    objects = extract_objects(scene_description)
    preferred_direction = user_profile.get("preferred_direction", "right")

    object_guidance = choose_navigation_action(objects, preferred_direction)
    return combine_guidance(environment, object_guidance)


if __name__ == "__main__":
    sample_scene = "There is a chair ahead."
    sample_profile = {"preferred_direction": "right"}
    print(generate_guidance(sample_scene, sample_profile))
