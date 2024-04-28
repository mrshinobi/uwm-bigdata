import sys

from pyspark import SparkConf, SparkContext

# Konfiguracja Sparka

text_file_path = sys.argv[1]
search_word = sys.argv[2]

print("#####", text_file_path)
print("#####", search_word)


appName = "SimpleApp"

conf = SparkConf().setAppName(appName).setMaster("local")
sc = SparkContext(conf=conf)

# Wczytanie danych bezpośrednio do RDD
text_rdd = sc.textFile(text_file_path)

# Filtracja i zliczanie linii zawierających 'a'
count_a = text_rdd.filter(lambda line: search_word in line.lower())
count_a_wynik = count_a.count()

# # Filtracja i zliczanie linii zawierających 'b'
# count_b = text_rdd.filter(lambda line: "b" in line).count()


# print(f"Lines with a: {count_a}, lines with b: {count_b}")
print(f"Lines with {search_word}: {count_a_wynik}")


#input("Press Enter to continue...")

# Zakończenie sesji Spark
sc.stop()
