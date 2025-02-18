import logging
from confluent_kafka import Consumer
import os

logging.basicConfig(level=logging.INFO)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

def create_kafka_consumer(topic):
    """Create and return a Kafka consumer with error handling."""
    try:
        logging.info(f"Initializing Kafka consumer for topic '{topic}'...")
        consumer = Consumer({
            'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'group.id': 'models_group',
            'auto.offset.reset': 'earliest'
        })
        consumer.subscribe([topic])
        return consumer
    except Exception as e:
        logging.error(f"Failed to create Kafka consumer: {e}")
        raise

def consume_kafka_messages(consumer):
    """Consume messages from Kafka topic with structured logging and graceful exit."""
    logging.info("Listening for messages...")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logging.error(f"Consumer error: {msg.error()}")
                continue
            logging.info(f"Received message: {msg.value().decode('utf-8')}")
            consumer.commit()
    except KeyboardInterrupt:
        logging.info("Consumer stopped by user.")
    finally:
        consumer.close()