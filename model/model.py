from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import torch


class VisionModel:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print("Using device:", self.device)

        print("Loading Moondream 2...")

        self.model = AutoModelForCausalLM.from_pretrained(
            "vikhyatk/moondream2",
            trust_remote_code=True,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )

        self.model = self.model.to(self.device)

        self.tokenizer = AutoTokenizer.from_pretrained(
            "vikhyatk/moondream2",
            trust_remote_code=True
        )

        print("Model loaded successfully!")

    def describe(self, image_path):
        print("Opening image...")
        image = Image.open(image_path).convert("RGB")

        print("Encoding image...")
        enc_image = self.model.encode_image(image)

        print("Generating answer...")
        answer = self.model.answer_question(
            enc_image,
            "Describe what you see.",
            self.tokenizer
        )

        print("Done!")
        return answer