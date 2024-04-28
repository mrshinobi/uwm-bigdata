from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def main():
    sc = SparkContext(appName="PythonStreamingFileWriter")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 1)  # Batch interval of 1 second

    # create a DStream that connects to localhost:9999
    lines = ssc.socketTextStream("localhost", 9999)
    print(lines)

    # processing the lines
    lines.foreachRDD(lambda rdd: rdd.foreachPartition(save_to_file))

    ssc.start()
    ssc.awaitTermination()


def save_to_file(partition):
    with open("output.txt", "a") as file:
        for record in partition:
            file.write(record)


if __name__ == "__main__":
    main()
