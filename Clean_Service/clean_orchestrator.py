


class CleanOrchestrator:
    def __init__(self, consumer, cleaner, publisher, logger):
        self.consumer = consumer
        self.cleaner = cleaner
        self.publisher = publisher
        self.logger = logger

    def handle_event(self,event):
        try:
            raw_data = event.get("raw_text", "")
            clean_text = self.cleaner.cleaner(raw_data)
            event['clean_text'] = clean_text
            self.logger.info(f"Cleaned message for image_id: {event.get('image_id')}")
            self.publisher.publish(event)
        except Exception as e:
            self.logger.error(f"Failed to handle event: {e}")

    def run(self):
        self.logger.info("Clean Orchestrator started running")
        self.consumer.start(self.handle_event)





