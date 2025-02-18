import logging
from confluent_kafka import Producer

logging.basicConfig(level=logging.INFO)


def notify_kafka(producer, topic, message):
    """Send a notification message to Kafka with delivery report."""

    def delivery_report(err, msg):
        if err is not None:
            logging.error(f"Message delivery failed: {err}")
        else:
            logging.info(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    logging.info(f"Sending message to Kafka topic '{topic}': {message}")
    producer.produce(topic, value=message.encode('utf-8'), callback=delivery_report)
    producer.flush()