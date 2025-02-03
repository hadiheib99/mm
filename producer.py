from confluent_kafka import Producer
import time

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def send_message():
    producer.produce("models-topic", key="test", value="Hello from Python!")
    producer.flush()
    print("✅ Message sent to Kafka!")

print("🔄 Kafka Producer Started...")

# Keep the producer running
while True:
    send_message()
    time.sleep(5)  # Send a message every 5 seconds
