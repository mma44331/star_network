import logging
from elasticsearch_client import ElasticsearchClient
from indexer_config import IndexerConfig
from index_orchestrator import IndexOrchestrator
from kafka_consumer import KafkaConsumer
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ELASTICSEARCH_SERVICE")


config = IndexerConfig()
group_id = "all_topics"
index_name = "tweet_images"
consumer = KafkaConsumer(config.bootstrap_servers,config.topics,group_id,logger)
elasticsclient = ElasticsearchClient(config.es,index_name,logger)
orchestrator = IndexOrchestrator(consumer,elasticsclient,logger)


def main():
    orchestrator.run()

if __name__ == "__main__":
    main()

