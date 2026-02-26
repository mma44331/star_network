import os
from dotenv import load_dotenv

class IngestionConfig:
    def __init__(self):
        load_dotenv()
        self.image_directory = os.getenv('IMAGE_DIRECTORY', './tweet_images')
        self.kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
        self.mongo_loader_url = os.getenv('MONGO_LOADER_URL', 'http://localhost:8001')
        self.tesseract_path = os.getenv('TESSERACT_PATH', r'C:\Program Files\Tesseract-OCR\tesseract.exe')
        self.topic_raw = os.getenv('TOPIC_RAW',"raw")

    def validate(self):
        if not os.path.exists(self.image_directory):
            raise FileNotFoundError(f"Directory {self.image_directory} not found")