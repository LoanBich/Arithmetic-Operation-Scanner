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

    def recognize(self, image: Image.Image):
        # Process the image
        pixel_values = self.processor(images=image, return_tensors="pt").pixel_values
        generated_ids = self.model.generate(pixel_values)
        generated_text = self.processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )
        return generated_text[0]
