from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def main():
    sc = SparkContext(appName="PythonStreamingReceiver")
    ssc = StreamingContext(sc, 1)  # 1 second window

    lines = ssc.socketTextStream("localhost", 9999)
    lines.pprint()

    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    main()
