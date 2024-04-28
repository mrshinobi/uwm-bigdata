from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp


def main():
    # initialize a SparkSession
    spark = SparkSession.builder.appName("StructuredStreamingFileWriter").getOrCreate()

    # define the input DataFrame from the connected stream
    lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

    # add a timestamp to each incoming line
    enriched_lines = lines.withColumn("received_time", current_timestamp())

    # setup the query to write the results to the file system
    query = (
        enriched_lines.writeStream.outputMode("append")
        .format("csv")
        .option("path", "output")
        .option("checkpointLocation", "checkpoint")
        .trigger(processingTime="1 second")
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":
    main()
