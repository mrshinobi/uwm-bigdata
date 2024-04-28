from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

spark = SparkSession.builder.appName("ExplodeSplitExample").getOrCreate()

# Example DataFrame with a string column
data = [("James, A, Smith",), ("Michael, Rose, Jones",)]
df = spark.createDataFrame(data, ["Name"])

# Splitting the 'Name' column into an array column
df_split = df.withColumn("NameArray", split(df["Name"], ", "))

# Exploding the 'NameArray' into multiple rows
df_exploded = df_split.withColumn("NameExploded", explode(df_split["NameArray"]))
df_exploded.show()

spark.stop()
