import json

from confluent_kafka import Producer


class Kafkapublisher:
    def __init__(self,bootstrap_servers,topic,logger):
        self.producer = Producer({"bootstrap.servers":bootstrap_servers})
        self.topic = topic
        self.logger = logger

    def send_to_kafka(self,image_id,meta_data,raw_text):
        message = {"image_id":image_id,
                   "meta_data": meta_data,
                   "raw_text": raw_text}
        json_data = json.dumps(message,default=str).encode("utf-8")
        self.producer.produce(self.topic,json_data)
        self.producer.flush()
        self.logger.info(f"Published metadata for {image_id} to Kafka topic {self.topic}")
