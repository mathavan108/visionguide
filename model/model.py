from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import torch


class VisionModel:
    def __init__(self):
        print("Loading Moondream 2...")

        self.model = AutoModelForCausalLM.from_pretrained(
            "vikhyatk/moondream2",
            trust_remote_code=True,
            torch_dtype=torch.float32
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            "vikhyatk/moondream2",
            trust_remote_code=True
        )

        print("Model loaded successfully!")

    def describe(self, image_path):
        image = Image.open(image_path).convert("RGB")

        enc_image = self.model.encode_image(image)

        answer = self.model.answer_question(
            enc_image,
            "Describe what you see.",
            self.tokenizer
        )

        return answer