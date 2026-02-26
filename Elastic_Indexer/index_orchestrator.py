


class IndexOrchestrator:
    def __init__(self, consumer, es_client, logger):
        self.consumer = consumer
        self.es_client = es_client
        self.logger = logger

    def handle_event(self,event):
        try:
            image_id = event.get('image_id')
            self.es_client.upsert(event,image_id)
            self.logger.info(f"Endexser message for image_id: {event.get('image_id')}")
        except Exception as e:
            self.logger.error(f"Failed to handle event: {e}")

    def run(self):
        self.logger.info("Endexser Orchestrator started running")
        self.consumer.start(self.handle_event)





