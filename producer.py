import json
import random
import time
from datetime import datetime as dt
from kafka import KafkaProducer
from data_generator import generate_message

# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode("utf-8")

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = serializer
)

if __name__ == '__main__':
    while True:
        # Generate a message
        dummy_message = generate_message()

        # Send message to topic
        print(f'Producing message @ {dt.now()} | Message = {str(dummy_message)}')
        producer.send('messages', dummy_message)

        # Sleep for a random time
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)

