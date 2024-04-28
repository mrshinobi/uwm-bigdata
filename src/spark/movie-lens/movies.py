from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, FloatType, StructType, StructField
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("MovieLens Recommender System") \
    .getOrCreate()

# Define schemas for the datasets
schema_ratings = StructType([
    StructField("userId", IntegerType(), True),
    StructField("movieId", IntegerType(), True),
    StructField("rating", FloatType(), True),
    StructField("timestamp", IntegerType(), True)
])

schema_users = StructType([
    StructField("userId", IntegerType(), True),
    StructField("gender", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("occupation", IntegerType(), True),
    StructField("zipCode", StringType(), True)
])

schema_movies = StructType([
    StructField("movieId", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("genres", StringType(), True)
])

# Load the data
ratings = spark.read.csv("../../../data/ml-1m/ratings.dat", schema=schema_ratings, sep="::")
users = spark.read.csv("../../../data/ml-1m/users.dat", schema=schema_users, sep="::")
movies = spark.read.csv("../../../data/ml-1m/movies.dat", schema=schema_movies, sep="::")

# ALS model setup
als = ALS(
    userCol="userId",
    itemCol="movieId",
    ratingCol="rating",
    coldStartStrategy="drop",
    nonnegative=True,
    implicitPrefs=False,
    rank=10,
    maxIter=10,
    regParam=0.1
)

# Train the model
model = als.fit(ratings)

# Evaluate the model by computing the RMSE on the test data
predictions = model.transform(ratings)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))

# Generate top 10 movie recommendations for all users
userRecs = model.recommendForAllUsers(10)
userRecs.show()

# Generate top 10 user recommendations for all movies
movieRecs = model.recommendForAllItems(10)
movieRecs.show()

# Stop Spark Session
spark.stop()
