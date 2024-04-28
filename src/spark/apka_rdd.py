from pyspark import SparkConf, SparkContext

# Konfiguracja Sparka
YOUR_SPARK_HOME = "/Users/katana/bin/spark-3.5.0-bin-hadoop3"
text_file = f"{YOUR_SPARK_HOME}/README.md"
appName = "SimpleApp"

conf = SparkConf().setAppName(appName).setMaster("local")
sc = SparkContext(conf=conf)

# Wczytanie danych bezpośrednio do RDD
text_rdd = sc.textFile(text_file)

# Filtracja i zliczanie linii zawierających 'a'
count_a = text_rdd.filter(lambda line: "a" in line)
count_a_wynik = count_a.count()

# Filtracja i zliczanie linii zawierających 'b'
count_b = text_rdd.filter(lambda line: "b" in line).count()


print(f"Lines with a: {count_a}, lines with b: {count_b}")

input("Press Enter to continue...")

# Zakończenie sesji Spark
sc.stop()
