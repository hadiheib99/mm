def notify_kafka(producer, topic, message):
    """Send a notification message to Kafka."""
    print(f"Sending message to Kafka topic '{topic}': {message}")
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()