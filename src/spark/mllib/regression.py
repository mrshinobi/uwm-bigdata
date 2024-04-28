from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("LinearRegressionExample").getOrCreate()

# Sample data
data = [(1.0, 3.0), (2.0, 6.0), (3.0, 9.0), (4.0, 12.0), (5.0, 15.0)]

# Create a DataFrame
columns = ["feature", "label"]
df = spark.createDataFrame(data, schema=columns)

# Prepare data
vectorAssembler = VectorAssembler(inputCols=["feature"], outputCol="features")
vector_df = vectorAssembler.transform(df)
vector_df = vector_df.select(["features", "label"])

# Split the data into train and test sets
train_df, test_df = vector_df.randomSplit([0.8, 0.2], seed=42)

# Define a linear regression model
lr = LinearRegression(featuresCol="features", labelCol="label")

# Train the model
lr_model = lr.fit(train_df)

# Make predictions
predictions = lr_model.transform(test_df)

# Evaluate the model
evaluator = RegressionEvaluator(predictionCol="prediction", labelCol="label", metricName="rmse")
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE) on test data = {rmse}")

# Stop Spark session
spark.stop()
