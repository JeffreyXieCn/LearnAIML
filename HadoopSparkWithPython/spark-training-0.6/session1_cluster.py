import sys

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <tree file>')
    sys.exit(1)

from pyspark.context import SparkContext

sc = SparkContext.getOrCreate()

filename = sys.argv[1]
print(f'Filename: {filename}')

def read_data_file(filename):
    import csv
    # Load the text file as an RDD, where each element is a line
    rdd = sc.textFile(filename)
    # Use Python's CSV reader to map every line of the text file to a Python list
    trees = rdd.mapPartitions(lambda x: csv.reader(x))
    return trees

trees = read_data_file(filename)

n = trees.filter(lambda x: x[6])\
          .map(lambda x: (x[6], 1))\
          .reduceByKey(lambda x, y: x+y)\
          .sortBy(lambda x: x[1], ascending=False)\
          .take(10)

print(f'List of 10 parks with the highest number of treated trees: {n}')