from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StringType, StructField, StructType

spark = SparkSession.builder.appName("KafkaStreamingExample").getOrCreate()

# Define schema of the incoming data
schema = StructType([StructField("id", StringType(), True), StructField("message", StringType(), True)])

# Read from Kafka
df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
    .option("subscribe", "topic_name")
    .load()
)

# Deserialize JSON from Kafka
df = df.selectExpr("CAST(value AS STRING) as json_string")
df = df.select(from_json("json_string", schema).alias("data")).select("data.*")

# Process the data
df.writeStream.outputMode("append").format("console").start().awaitTermination()

spark.stop()
