# Updated handle_events.py
import logging

logging.basicConfig(level=logging.INFO)

def handle_events(events):
    """Process events with structured logging."""
    for event in events:
        logging.info(f"Processing event: {event}")