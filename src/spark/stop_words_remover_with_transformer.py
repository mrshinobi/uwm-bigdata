import pyspark.sql.functions as F
from pyspark.ml.feature import StopWordsRemover
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StopWordsRemover").getOrCreate()

stop = ["<stop_words>"]


df = spark.createDataFrame([("hello",), ("world",), ("test",), ("hi",), ("hello world",)], ["name"])

df = df.withColumn("tokens", F.split("name", "\\s+"))

remover = StopWordsRemover(stopWords=stop, inputCol="tokens", outputCol="stop")

result = remover.transform(df).select("name", F.array_join("stop", " ").alias("stop"))

result.show()
