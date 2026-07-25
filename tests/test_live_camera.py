import cv2
import time

from camera.camera import Camera
from model.model import VisionModel
from speech.speech import Speaker
from guidance.navigation import NavigationGuide


def main():

    print("=" * 70)
    print("             VisionGuide - AI Navigation Assistant")
    print("=" * 70)

    print("\nLoading Vision Model...")
    vision = VisionModel()

    print("\nLoading Speaker...")
    speaker = Speaker()

    print("\nOpening Camera...")
    camera = Camera()

    print("\nLoading Navigation Module...")
    navigator = NavigationGuide()

    print("\nSystem Ready!")
    print("Press 'Q' to Quit.\n")

    capture_interval = 3
    last_capture = time.time()

    while True:

        frame = camera.get_frame()

        if frame is None:
            print("Unable to capture frame.")
            break

        cv2.imshow("VisionGuide Live", frame)

        current_time = time.time()

        if current_time - last_capture >= capture_interval:

            image_path = "assets/images/live.jpg"

            camera.save_frame(frame, image_path)

            print("\n" + "=" * 60)
            print("Capturing Scene...")
            print("=" * 60)

            try:

                response = vision.describe(image_path)

                print("\nAI Response:\n")
                print(response)

                data = navigator.parse(response)

                scene = data.get("scene", "")
                navigation = data.get("navigation", "")
                warning = data.get("warning", "")

                print("\n-------------------------------")
                print("Scene Description")
                print("-------------------------------")
                print(scene)

                print("\n-------------------------------")
                print("Navigation Guidance")
                print("-------------------------------")
                print(navigation if navigation else "None")

                print("\n-------------------------------")
                print("Warning")
                print("-------------------------------")
                print(warning if warning else "None")

                # Build text to speak
                speech_parts = []

                if scene:
                    speech_parts.append(scene)

                if navigation:
                    speech_parts.append(navigation)

                if warning:
                    speech_parts.append("Warning. " + warning)

                speech = ". ".join(speech_parts)

                if speech.strip():

                    print("\n========== SPEAKING ==========")
                    print(speech)
                    print("==============================")

                    speaker.speak(speech)

                else:
                    print("\nNothing to speak.")

            except Exception as e:

                print("\nError During Inference")
                print(e)

            last_capture = current_time

        key = cv2.waitKey(1)

        if key & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    print("\nVisionGuide Closed.")


if __name__ == "__main__":
    main()