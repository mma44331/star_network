import json
from confluent_kafka import Producer


class KafkaPublisher:
    def __init__(self,bootstrap_servers, topic_name, logger):
        self.topic_name = topic_name
        self.logger =logger
        self.producer = Producer({"bootstrap.servers":bootstrap_servers})


    def publish(self, event_id, event):
        message = {"event_id": event_id,
                   "event": event}
        json_data = json.dumps(message, default=str).encode("utf-8")
        self.producer.produce(self.topic_name, json_data)
        self.producer.flush()
        self.logger.info(f"Published event for {event_id} to Kafka topic {self.topic_name}")

