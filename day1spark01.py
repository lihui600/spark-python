from pyspark.shell import sc

data = sc.parallelize(range(1,101))
data.reduce(lambda x, y: x+y)
