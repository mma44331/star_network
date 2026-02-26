import json
from confluent_kafka import Consumer, KafkaError


class KafkaConsumer:
    def __init__(self,bootstrap_servers, topic_list, group_id, logger):
        self.consumer = Consumer({"bootstrap.servers":bootstrap_servers,
                                  "group.id":group_id,
                                  'auto.offset.reset': 'earliest'})
        self.topic_list = topic_list
        self.logger = logger


    def start(self,callback):
        self.consumer.subscribe(self.topic_list)
        self.logger.info(f"Subscribed to topic: {self.topic_list}")
        while True:
            msg = self.consumer.poll()
            if msg is None:
                self.logger.info("not found msg")
                continue
            if msg.error():
                if msg.error().code() != KafkaError._PARTITION_EOF:
                    self.logger.error(f"Consumer error: {msg.error()}")
                    continue
            callback(json.loads(msg.value().decode('utf-8')))
