import logging
from analytics_config import AnalyticsConfig
from analytics_orchestrator import AnalyticsOrchestrator
from kafka_publisher import KafkaPublisher
from kafka_consumer import KafkaConsumer
from text_analyzer import TextAnalyzer
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ANALYZER_SERVICE")


config = AnalyticsConfig()
group_id = f"{config.topic_clean}_clean"
publisher = KafkaPublisher(config.bootstrap_servers,config.topic_analytics,logger)
consumer = KafkaConsumer(config.bootstrap_servers,config.topic_clean,group_id,logger)
analyzer = TextAnalyzer(logger)
orchestrator = AnalyticsOrchestrator(consumer,analyzer,publisher,logger)


def main():
    orchestrator.run()

if __name__ == "__main__":
    main()

