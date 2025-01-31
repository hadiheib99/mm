from confluent_kafka import Producer

def create_kafka_producer():
    """Create and return a Kafka producer."""
    print("🔄 Initializing Kafka producer...")
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    def delivery_report(err, msg):
        if err:
            print(f"❌ Message delivery failed: {err}")
        else:
            print(f"✅ Message delivered to {msg.topic()} [{msg.partition()}]")

    return producer, delivery_report

def send_kafka_message(producer, delivery_report, topic, message):
    """Send a message to Kafka topic with error logging."""
    print(f"📩 Sending message to Kafka topic '{topic}': {message}")
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.flush()
