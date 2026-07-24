import cv2

from model.model import VisionModel
from speech.speech import Speaker

print("Loading Vision Model...")
vision = VisionModel()

print("Loading Speaker...")
speaker = Speaker()

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera")
    exit()

print("Capturing image...")

ret, frame = camera.read()

if ret:
    cv2.imwrite("assets/images/live.jpg", frame)

    print("Analyzing image...")

    description = vision.describe("assets/images/live.jpg")

    print("\nDescription:")
    print(description)

    speaker.speak(description)

camera.release()