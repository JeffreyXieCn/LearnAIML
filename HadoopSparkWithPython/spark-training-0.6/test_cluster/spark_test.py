import sys
from pyspark.context import SparkContext

jobName="Spark test"
sc = SparkContext(appName=jobName)

numbers = sc.parallelize([1, 2, 3, 4, 5, 6])
print(numbers.filter(lambda x: x % 2 == 0).collect())
