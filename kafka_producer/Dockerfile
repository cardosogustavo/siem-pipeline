FROM python:3.13-alpine

WORKDIR /app
ENV PYTHONPATH="/app"

COPY data_simulator /app/data_simulator
COPY kafka_producer/kafka_producer.py .

RUN pip install faker kafka-python

CMD ["python3", "kafka_producer.py"]