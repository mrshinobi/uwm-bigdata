from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row, SparkSession

# Inicjalizacja SparkSession
spark = SparkSession.builder.appName("ALSExample").getOrCreate()

# Wczytywanie danych. Załóżmy, że ratings.dat jest oddzielony dwukropkami (UserID::MovieID::Rating::Timestamp)

file_path = "../../../data/ml-1m/ratings.dat"
lines = spark.read.text(file_path).rdd
parts = lines.map(lambda row: row.value.split("::"))
ratingsRDD = parts.map(lambda p: Row(userId=int(p[0]), movieId=int(p[1]), rating=float(p[2]), timestamp=int(p[3])))

# Konwersja RDD do DataFrame
ratings = spark.createDataFrame(ratingsRDD)

# Podział danych na zestaw treningowy i testowy
(training, test) = ratings.randomSplit([0.8, 0.2])

# Konfiguracja i trening modelu ALS
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating", coldStartStrategy="drop")
model = als.fit(training)

# Ewaluacja modelu na zestawie testowym
predictions = model.transform(test)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))

# Generowanie rekomendacji dla wszystkich użytkowników
userRecs = model.recommendForAllUsers(10)  # Dla każdego użytkownika generuje 10 rekomendacji filmów
userRecs.show()

spark.stop()
