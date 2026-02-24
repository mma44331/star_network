class DownloadOrchestrator:
    def __init__(self, config, copy_handler, logger):
        self.config = config
        self.handler = copy_handler
        self.logger = logger

    def run(self):
        self.logger.info("Data Loader process started")
        self.config.validate()
        self.handler.copy_images(self.config.source_path, self.config.image_directory)
        self.logger.info("Data Loader process finished")