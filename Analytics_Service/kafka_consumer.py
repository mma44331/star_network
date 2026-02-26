import json

from confluent_kafka import Consumer, KafkaError


class KafkaConsumer:
    def __init__(self,bootstrap_servers, topic_name, group_id, logger):
        self.consumer = Consumer({"bootstrap.servers":bootstrap_servers,
                                  "group.id":group_id,
                                  'auto.offset.reset': 'earliest'})
        self.topic_name = topic_name
        self.logger = logger


    def start(self,callback):
        self.consumer.subscribe([self.topic_name])
        self.logger.info(f"Subscribed to topic: {self.topic_name}")
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                self.logger.info("msg")
                continue
            if msg.error():
                if msg.error().code() != KafkaError._PARTITION_EOF:
                    self.logger.error(f"Consumer error: {msg.error()}")
                    continue
            callback(json.loads(msg.value().decode('utf-8')))
