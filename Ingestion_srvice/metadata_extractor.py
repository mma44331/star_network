import uuid
import os
from PIL import Image
from pathlib import Path

class MetadataExtractor:
    def __init__(self, logger):
        self.logger = logger

    def generate_image_id(self, image_path):
        image_id = Path(image_path.stem)
        self.logger.info(f"Generated image_id: {image_id}")
        return image_id

    def extract_metadata(self, image_path):
        self.logger.info(f"Extracting metadata for {image_path}")
        img = Image.open(image_path)
        return {
            "size_bytes": os.path.getsize(image_path),
            "dimensions": {"width": img.width, "height": img.height},
            "format": img.format
        }