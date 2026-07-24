from model.model import VisionModel

print("Creating Vision Model...")

model = VisionModel()

print("Calling describe()...")

result = model.describe("assets/images/test.jpg")

print("\n========================")
print("Description:")
print(result)
print("========================")