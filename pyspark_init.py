import pyspark.sql
from pyspark.sql import SparkSession
from pyspark.sql.functions import mean, max, min, count, corr, year, month

spark = SparkSession.builder.appName("firstApp").getOrCreate()
dataframe = spark.read.csv('./GOOG.csv', header=True, inferSchema=True)
print(dataframe.columns)
dataframe.printSchema()

for row in dataframe.head(10):
    print(row)

dataframe.describe().show()

from pyspark.sql.functions import format_number
description = dataframe.describe()
description.select(description["summary"],
                   format_number(description["Open"].cast("float"), 2).alias("Open"),
                   format_number(description["High"].cast("float"), 2).alias("High"),
                   format_number(description["Low"].cast("float"), 2).alias("Low"),
                   format_number(description["Close"].cast("float"), 2).alias("Close"),
                   description["Volume"].cast("int").alias("Volume")
                   ).show()


nDataframe = dataframe.withColumn("Open/Volume ratio", dataframe["Open"]/dataframe["Volume"])

nDataframe.show()
nDataframe.select("Open/Volume ratio").show()

dataframe.orderBy(dataframe["High"].desc()).show()

print(dataframe.orderBy(dataframe["High"].asc()).head(1)[0][0])

dataframe.select(mean("Open")).show()
dataframe.select(max("Close"), min("Close")).show()

print(dataframe.filter("Volume < 2000000").count())

result = dataframe.filter(dataframe["Volume"]<2000000)
result.select(count("Volume")).show()

print((dataframe.filter(dataframe["Open"] > 1000)).count()*1.0 / dataframe.count() * 100)

dataframe.select(corr("High", "Low")).show()
dataframe.select(corr("Volume", "Open")).show()

dataframe_year = dataframe.withColumn("Year", year(dataframe["Date"]))
dataframe_year.show()

max_year_df = dataframe_year.groupBy("Year").max()
max_year_df.select("Year","max(High)").show()

dataframe_month = dataframe.withColumn("Month", month("Date"))
dataframe_month.show()

average_months = dataframe_month.select("Month", "High").groupby("Month").mean()
average_months.select("Month","avg(High)").orderBy("Month").show()

# SQL
app = SparkSession.builder.appName("SQL").getOrCreate()
dataframe.createOrReplaceTempView("stock")
result = app.sql("SELECT * FROM stock")
print(result)
app.sql("SELECT COUNT(Open) FROM Stock").show()
