import logging
from confluent_kafka import Producer
import time
import os

logging.basicConfig(level=logging.INFO)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})

logging.info("🔄 Kafka Producer Started...")

def send_message():
    try:
        producer.produce("ESM-topic", key="test", value="Hello from Python!", callback=delivery_report)
        producer.flush()
        logging.info("✅ Message sent to Kafka!")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")

def delivery_report(err, msg):
    if err is not None:
        logging.error(f"Delivery failed for record {msg.key()}: {err}")
    else:
        logging.info(f"Record {msg.key()} successfully produced to {msg.topic()} [{msg.partition()}]")

# Loop to send messages every 5 seconds
while True:
    send_message()
    time.sleep(5)
