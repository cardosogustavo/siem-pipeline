from data_simulator.simulator import generate_log
from kafka_producer.kafka_producer import run_producer


def main():
    # run kafka producer
    run_producer()

if __name__ == '__main__':
    main()