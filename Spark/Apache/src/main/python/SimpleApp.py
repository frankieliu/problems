"""SimpleApp.py"""
from pyspark.sql import SparkSession

logFile = "README.md"  # Should be some file on your system
appName="Simple Application"

spark = SparkSession.builder.appName(appName).getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
