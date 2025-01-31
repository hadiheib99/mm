from confluent_kafka import Consumer

def create_kafka_consumer(topic):
    """Create and return a Kafka consumer."""
    print(f"Initializing Kafka consumer for topic '{topic}'...")
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'models_group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([topic])
    return consumer

def consume_kafka_messages(consumer):
    """Consume messages from Kafka topic."""
    print("Listening for messages...")
    while True:
        msg = consumer.poll(1.0)
        print("Received a message")
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        print(f"Received message: {msg.value().decode('utf-8')}")
        consumer.commit()