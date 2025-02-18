import logging
from handle_events import handle_events
from integrate_kafka import integrate_kafka
from kafka_consumer import create_kafka_consumer, consume_kafka_messages

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting main application...")
    try:
        # Kafka Integration
        producer, consumer = integrate_kafka()

        # Consume messages
        kafka_consumer = create_kafka_consumer("EPT-topic")
        consume_kafka_messages(kafka_consumer)

        # Process some events
        handle_events(["event1", "event2", "event3"])
    except Exception as e:
        logging.error(f"Application encountered an error: {e}")
    finally:
        logging.info("Application terminated.")