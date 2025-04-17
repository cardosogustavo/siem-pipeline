from kafka import KafkaProducer
import json
import time
import random
from data_simulator.simulator import generate_log
from kafka.errors import NoBrokersAvailable

# kafka conf
KAFKA_TOPIC = "siem_logs"
KAFKA_BROKER = "kafka:9092"


def wait_for_kafka(bootstrap_servers, timeout=60):
    start = time.time()
    while True:
        try:
            print("Trying connection to kafka...")
            # start producer
            producer = KafkaProducer(
                bootstrap_servers=bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode("utf-8")
            )
            print("Kafka available!")
            return producer
        except NoBrokersAvailable:
            if time.time() - start > timeout:
                raise TimeoutError("Kafka not ready on time!")
            print("Kafka still not ready, trying again in 5 seconds...")
            time.sleep(5)

# waits for kafka to be ready
producer = wait_for_kafka(KAFKA_BROKER)

def run_producer():
    try:
        print(f"Sending logs to topic '{KAFKA_TOPIC}'... (ctrl+C to stop)")
        while True:
            log = generate_log(anomalous=random.random() < 0.1)
            producer.send(KAFKA_TOPIC, value=log)
            print(f"Sent: {log}")
            time.sleep(2) # every 2 sec
    except KeyboardInterrupt:
        print("\nStopping producer.")
    finally:
        producer.flush()
        producer.close()

if __name__ == "__main__":
    run_producer()