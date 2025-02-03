from handle_events import handle_events
from connect_to_google_cloud import connect_to_google_cloud
from create_dockerfile import create_dockerfile
from integrate_kafka import integrate_kafka
from producer import create_kafka_producer, send_kafka_message
from kafka_consumer import create_kafka_consumer, consume_kafka_messages
from fetch_model_from_registry import fetch_model_from_registry
from manage_model_versions import promote_model_version

if __name__ == "__main__":
    # Connect to Google Cloud
    connect_to_google_cloud()

    # Create Dockerfile
    create_dockerfile()

    # Kafka Integration
    kafka_producer, delivery_report = create_kafka_producer()
    send_kafka_message(kafka_producer, delivery_report, "models-topic", "Test message from Python")

    kafka_consumer = create_kafka_consumer("models-topic")

    # Allow dynamic model stage selection with automatic default
    model_name = "example_model"
    user_stage = "Production"  # Automatically default to "Production" (no input required)

    print(f"Using model stage: {user_stage}")

    # Fetch model dynamically based on pre-set stage
    model = fetch_model_from_registry(model_name, stage=user_stage)

    if model:
        print(f"🎯 Model '{model_name}' in stage '{user_stage}' is ready to use.")
        send_kafka_message(kafka_producer, "models-topic",
                           f"Model '{model_name}' (Stage: {user_stage}) is ready for deployment.")
        promote_model_version(model_name, "Staging", "Production")
    else:
        print("⚠️ Model could not be loaded. Check registry and try again.")

    # Start consuming messages
    consume_kafka_messages(kafka_consumer)

    # Process some events
    handle_events(["event1", "event2", "event3"])