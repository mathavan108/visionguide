from model.model import VisionModel

model = VisionModel()

result = model.describe("assets/images/test.jpg")

print("\nDescription:")
print(result)