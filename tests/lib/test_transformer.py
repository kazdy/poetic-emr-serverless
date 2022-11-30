import pytest
from poetic_emr_serverless.lib.transformer import transform
from chispa.schema_comparer import assert_schema_equality_ignore_nullable

from pyspark.sql.types import *

def test_transform(spark, test_data):
    input_schema = StructType([StructField("firstname", StringType()), StructField("age", StringType())])
    sc = spark.sparkContext
    input_df = spark.read.option("inferSchema","true").json(sc.parallelize([test_data]))

    actual_df = transform(input_df)
    expected_schema = StructType([StructField("age", StringType()), StructField("name", StringType())])
    assert_schema_equality_ignore_nullable(expected_schema, actual_df.schema)