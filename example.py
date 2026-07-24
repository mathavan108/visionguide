"""Example script demonstrating the advanced personalization system."""

from advanced_features.context_engine import extract_objects, generate_guidance
from advanced_features.personalization import PersonalizationEngine


def main() -> None:
    # Load the user profile through the personalization engine.
    engine = PersonalizationEngine()
    print("Loaded user profile:")
    print(engine.profile)
    print()

    # Define three different scene descriptions to simulate navigation.
    scene_descriptions = [
        "A chair is ahead in the corridor with a clear path to the right.",
        "A person is standing near a door in the classroom.",
        "An outdoor area with a table and an empty path nearby.",
    ]

    # Simulate navigation for each scene description.
    for idx, scene in enumerate(scene_descriptions, start=1):
        print(f"Scene {idx}: {scene}")

        # Generate adaptive guidance using the current profile.
        guidance = generate_guidance(scene, engine.profile)
        print(f"Guidance: {guidance}")

        # Update obstacle history from detected objects in the scene.
        objects = extract_objects(scene)
        for obstacle in objects:
            engine.update_obstacle(obstacle)

        # Update location history with a sample location name for this scene.
        location_name = f"Scene {idx} location"
        engine.update_location(location_name)

        print()

    # Save the profile explicitly to persist any final changes.
    engine.save_profile()

    # Print the updated profile after all scenes have been processed.
    print("Updated user profile:")
    print(engine.profile)


if __name__ == "__main__":
    main()
