spark-submit --master "local[4]" --name "Test" nazwa_skryptu --parametr1 wartosc1 --parametr2 wartosc2


spark-submit nazwa_skryptu.py

# mozliwe argumenty spark-submit
  --deploy-mode client \  # cluster
  --executor-memory 2G \
  --driver-memory 2G \
  --num-executors 2 \
  --executor-cores 2 \
  --driver-cores 2 \
  --conf "spark.executor.extraJavaOptions=-XX:+PrintGCDetails -XX:+PrintGCTimeStamps" \



# uruchomienie dla klasy
spark-submit
  --class YourMainClass \
  --master local[4] \
  --deploy-mode client \
  --executor-memory 2G \
  your-spark-app.jar

