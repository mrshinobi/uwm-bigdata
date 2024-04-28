from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicjalizacja Spark Session
spark = SparkSession.builder.appName("MovieLens ALS Recommender").getOrCreate()

# Wczytanie danych
data = spark.read.csv("ratings.csv", header=True, inferSchema=True)
data = data.select(col("userId").cast("integer"), col("movieId").cast("integer"), col("rating").cast("float"))

# Podział danych na zestaw treningowy i testowy
(train, test) = data.randomSplit([0.8, 0.2])

# Konfiguracja modelu ALS
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating", coldStartStrategy="drop")

# Trenowanie modelu
model = als.fit(train)

# Predykcja na danych testowych
predictions = model.transform(test)

# Ewaluacja modelu
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print(f"Root-mean-square error = {rmse}")

# Generowanie rekomendacji
# Dla każdego użytkownika wygeneruj top 10 rekomendowanych filmów
userRecs = model.recommendForAllUsers(10)
userRecs.show()

# Dla każdego filmu wygeneruj top 10 użytkowników, którzy powinni go zobaczyć
movieRecs = model.recommendForAllItems(10)
movieRecs.show()

spark.stop()
