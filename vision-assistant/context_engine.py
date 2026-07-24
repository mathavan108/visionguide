from typing import Any, Dict


def build_context(user_profile: Dict[str, Any], session_data: Dict[str, Any]) -> Dict[str, Any]:
    """Construct a context object for the vision assistant."""
    return {
        "user": {
            "id": user_profile.get("id"),
            "preferences": user_profile.get("preferences", {}),
        },
        "session": session_data,
    }


def select_relevant_features(context: Dict[str, Any]) -> Dict[str, Any]:
    """Select contextually relevant features from the current session."""
    preferences = context["user"].get("preferences", {})
    return {
        "highlight_mode": preferences.get("highlight_mode", "standard"),
        "focus_areas": context["session"].get("focus_areas", []),
    }


def enrich_response(context: Dict[str, Any], response: str) -> str:
    """Enhance an assistant response based on the current context."""
    if context["user"].get("preferences", {}).get("tone") == "friendly":
        return f"Hey there! {response}"
    return response
