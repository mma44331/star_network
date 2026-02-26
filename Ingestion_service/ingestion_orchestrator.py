from pathlib import Path


class IngestionOrchestrator:
    def __init__(self, config, ocr_engine, metadata_extractor, mongo_client, kafka, logger):
        self.config = config
        self.ocr = ocr_engine
        self.meta = metadata_extractor
        self.mongo = mongo_client
        self.kafka = kafka
        self.logger = logger

    def process_image(self, path):
        image_id = self.meta.generate_image_id(path)
        metadata = self.meta.extract_metadata(path)
        raw_text = self.ocr.extract_text(path)

        success = self.mongo.send(path, image_id)
        if success:
            self.kafka.send_to_kafka(image_id,metadata,raw_text)
        self.logger.info(f"Successfully processed image {image_id}")

    def run(self):
        folder = Path(self.config.image_directory)
        for file_path in folder.iterdir():
            if file_path.is_file():
                self.process_image(file_path)