from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, TimestampType

# define o schema dos logs
log_schema = StructType() \
    .add("timestamp", TimestampType()) \
    .add("user", StringType()) \
    .add("ip_address", StringType()) \
    .add("event_type", StringType()) \
    .add("status", StringType()) \
    .add("location", StringType()) \
    .add("device", StringType()) \
    .add("file_accessed", StringType()) \
    .add("anomalous", StringType()) \

def main():
    spark = SparkSession.builder \
        .appName("KafkaSparkLogProcessor") \
        .master("local[*]") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("WARN")

    # reading from kafka. the server must be the container name
    df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "siem_logs") \
        .option("startingOffsets", "latest") \
        .load()
    
    # casting columns "value" from byutes to string and then JSON
    logs = df.selectExpr("CAST(value AS STRING) as json_str") \
        .select(from_json(col("json_str"), log_schema).alias("data")) \
        .select("data.*")
    
    # saves in parquet FS
    query = logs.writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/app/spark_streaming/checkpoint") \
        .option("path", "/app/spark_streaming/output/parquet") \
        .outputMode("append") \
        .start()

    query.awaitTermination()


if __name__ == "__main__":
    main()