import logging
from confluent_kafka import Producer, Consumer
import os

logging.basicConfig(level=logging.INFO)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

def integrate_kafka():
    """Set up Kafka producer and consumer with error handling."""
    try:
        logging.info("Setting up Kafka integration...")
        producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})
        consumer = Consumer({
            'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'group.id': 'models_group',
            'auto.offset.reset': 'earliest'
        })
        logging.info("Kafka producer and consumer initialized.")
        return producer, consumer
    except Exception as e:
        logging.error(f"Failed to integrate Kafka: {e}")
        raise