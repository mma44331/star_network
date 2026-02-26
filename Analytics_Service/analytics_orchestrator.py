class AnalyticsOrchestrator:
    def __init__(self, consumer, analyzer, publisher, logger):
        self.consumer = consumer
        self.analyzer = analyzer
        self.publisher = publisher
        self.logger = logger

    def handle_event(self,event):
        try:
            raw_data = event.get("clean_text", "")
            analyze_text = self.analyzer.analyze(raw_data)
            event['top_10'] = analyze_text['top_10']
            event['list_of_weapons'] = analyze_text['list_of_weapons']
            event['score_filling'] = analyze_text['score_filling']

            self.logger.info(f"Analysed message for image_id: {event.get('image_id')}")
            self.publisher.publish(event)
        except Exception as e:
            self.logger.error(f"Failed to handle event: {e}")

    def run(self):
        self.logger.info("Analyzed Orchestrator started running")
        self.consumer.start(self.handle_event)

