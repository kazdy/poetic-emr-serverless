from pyspark.sql import SparkSession
from lib import config, transformer

def run(config_path: str):
    configuration = config.get_config(config_path)
    spark = SparkSession.builder.getOrCreate()

    df = spark.read.json(configuration["source"])
    df = transformer.transform(df)
    df.write.mode("overwrite").parquet(configuration["destination"])

    spark.stop()

