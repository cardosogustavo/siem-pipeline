#!/bin/bash

PARQUET_OUTPUT="./spark_streaming/output"
CHECKPOINT_DIR="./spark_streaming/checkpoint"
TOPIC_NAME="siem_logs"
KAFKA_BROKER="kafka:9092"

echo "Resetting pipeline..."

# 1. Apagar arquivos parquet e checkpoints, depois recriar a pasta parquet
echo "Cleaning spark output data..."
rm -rf ${PARQUET_OUTPUT:?}/*
rm -rf ${CHECKPOINT_DIR:?}/*

echo "Re-creating output/parquet folder"
mkdir -p /spark_streaming/output/parquet

# 2 deletar tópico kafka
echo "Removing Kafka topic: $TOPIC_NAME"
docker exec kafka \
    /bin/kafka-topics --bootstrap-server $KAFKA_BROKER --delete --topic $TOPIC_NAME

# 3 recriar o tópico
echo "Recreating kafka topic: $TOPIC_NAME"
docker exec kafka \
    /bin/kafka-topics --bootstrap-server $KAFKA_BROKER --create --topic $TOPIC_NAME --partitions 1 --replication-factor 1

echo "[+] Pipeline restored"