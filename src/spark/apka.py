from pyspark.sql import SparkSession

YOUR_SPARK_HOME = "/Users/katana/bin/spark-3.5.0-bin-hadoop3"

text_file = f"{YOUR_SPARK_HOME}/README.md"

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

text_df = spark.read.text(text_file).cache()

count_a = text_df.filter(text_df.value.contains("a")).count()
count_b = text_df.filter(text_df.value.contains("b")).count()

print(f"Lines with a: {count_a}, lines with b: {count_b}")

spark.stop()
