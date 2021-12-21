# Databricks notebook source
def generate_data2(table_name="my_data"):
  df = spark.range(0,10)
  df.write.format("delta").mode("overwrite").saveAsTable(table_name)

# COMMAND ----------

# another release trigger one more change
# changes for code2 to trigger one more change v1
# changes for code2 to trigger one more change v2
