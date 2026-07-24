from model.model import VisionModel
from speech.speech import Speaker

print("Loading Vision Model...")
vision = VisionModel()

print("Loading Speaker...")
speaker = Speaker()

print("Analyzing Image...")

description = vision.describe("assets/images/test.jpg")

print("\nDescription:")
print(description)

speaker.speak(description)