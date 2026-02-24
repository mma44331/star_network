import pytesseract
from PIL import Image

class OCREngine:
    def __init__(self, tesseract_path, logger):
        self.logger = logger
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    def extract_text(self, image_path):
        self.logger.info(f"Extracting text from {image_path}")
        img = Image.open(image_path).convert("L")
        img = img.crop((img.width * 0.10, 0, img.width, img.height))
        img = img.resize((img.width * 10, img.height * 10))
        return pytesseract.image_to_string(img).strip()