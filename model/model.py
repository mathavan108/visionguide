from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import torch


class VisionModel:

    def __init__(self):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        print(f"Using device: {self.device}")
        print("Loading Moondream 2...")

        self.model = AutoModelForCausalLM.from_pretrained(
            "vikhyatk/moondream2",
            trust_remote_code=True,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        ).to(self.device)

        self.tokenizer = AutoTokenizer.from_pretrained(
            "vikhyatk/moondream2",
            trust_remote_code=True
        )

        print("Vision model loaded successfully.")

    def describe(self, image_path):

        image = Image.open(image_path).convert("RGB")

        encoded_image = self.model.encode_image(image)

        prompt = """
You are VisionGuide, an intelligent AI assistant helping a blind person navigate safely.

Carefully observe the image before answering.

Your job is to first understand the entire scene and then provide navigation guidance.

Follow these rules:

1. Describe only important objects.
2. Mention where they are located.
3. Ignore decorations and unimportant items.
4. Mention only objects affecting walking.
5. Mention approximate distance (Near, Medium, Far).
6. Mention whether the walking path is clear.
7. If there is danger, explain it.
8. Keep the answer short and natural.

Respond exactly in this format.

Scene:
(Describe the surroundings.)

Navigation:
(Tell the blind person exactly how to move.)

Warning:
(None if safe, otherwise explain the danger.)
"""

        answer = self.model.answer_question(
            encoded_image,
            prompt,
            self.tokenizer
        )

        return answer.strip()