from pyspark.sql import SparkSession

# Inicjalizacja SparkSession
spark = SparkSession.builder.appName("BucketingExample").getOrCreate()

# Przykładowe dane
data = [("Alice", 21), ("Bob", 22), ("Catherine", 30), ("David", 27), ("Eleanor", 33)]
columns = ["Name", "Age"]

# Tworzenie DataFrame
df = spark.createDataFrame(data, schema=columns)

# Zapisywanie DataFrame z bucketing na podstawie kolumny 'Age'
df.write.bucketBy(4, "Age").sortBy("Age").format("parquet").saveAsTable("bucketed_table")
