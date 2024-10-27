import re

from optimum.onnxruntime import ORTModelForVision2Seq
from PIL import Image
from transformers import TrOCRProcessor


class MathRecognizer:
    def __init__(self):
        # Load the model and processor
        self.processor = TrOCRProcessor.from_pretrained("breezedeus/pix2text-mfr")
        self.model = ORTModelForVision2Seq.from_pretrained(
            "breezedeus/pix2text-mfr", use_cache=False
        )

    def recognize(self, image: Image.Image) -> str:
        # Process the image
        pixel_values = self.processor(images=image, return_tensors="pt").pixel_values
        generated_ids = self.model.generate(pixel_values)
        generated_text = self.processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )

        return generated_text[0]

    def clean_operation(self, operation_text: str) -> str:
        # Convert commas to periods for decimal representation
        clean_operation = operation_text.replace(",", ".")  # Convert comma to period
        clean_operation = re.sub(
            r"[^0-9+\-*/().^.]", "", clean_operation
        )  # Allow valid characters only
        clean_operation = clean_operation.replace(
            "^", "**"
        )  # Replace with Python exponentiation operator
        return clean_operation
