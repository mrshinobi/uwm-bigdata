from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType

spark = SparkSession.builder.appName("UDFExample").getOrCreate()


# UDF definition
def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32


temp_udf = udf(celsius_to_fahrenheit, DoubleType())


# Sample DataFrame
df = spark.createDataFrame([(0,), (30,), (100,)], ["Celsius"])

df_with_fahrenheit = df.withColumn("Fahrenheit", temp_udf(df["Celsius"]))
df_with_fahrenheit.show()

spark.stop()
