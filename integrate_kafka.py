
from confluent_kafka import Producer, Consumer

def integrate_kafka():
    """Set up Kafka producer and consumer."""
    print("Setting up Kafka integration...")
    producer = Producer({'bootstrap.servers': 'localhost:9092'})
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'models_group',
        'auto.offset.reset': 'earliest'
    })
    print("Kafka producer and consumer initialized.")
    return producer, consumer