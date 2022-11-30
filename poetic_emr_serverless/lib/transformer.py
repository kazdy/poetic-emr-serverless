from pyspark.sql import DataFrame

def transform(df: DataFrame) -> DataFrame:
    df = df.withColumnRenamed("firstname", "name")
    return df
    