from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PartitioningAndBucketing").getOrCreate()

# Sample data generation
data = [
    ("2023-01-01", "North", 1, 100),
    ("2023-01-01", "South", 2, 200),
    ("2023-01-02", "North", 3, 300),
    ("2023-01-02", "East", 4, 400),
]
columns = ["date", "region", "product_id", "amount"]
df = spark.createDataFrame(data, schema=columns)

df.write.partitionBy("date", "region").mode("overwrite").parquet("output/partitioned")

# Write data bucketed by 'product_id'
(df.write.bucketBy(4, "product_id").sortBy("product_id").mode("overwrite").saveAsTable("bucketed_sales"))
