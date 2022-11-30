import pytest
from pyspark import SparkConf
from pyspark.sql import SparkSession


def test_spark_conf() -> SparkConf:
    return (
        SparkConf()
        .set("spark.speculation", False)
        .set("spark.sql.shuffle.partitions", "1")
        .set("spark.ui.enabled", "false")
    )


@pytest.fixture(scope='session')
def spark():
    yield (
        SparkSession.builder
        .master("local")
        .appName("poetic-tests")
        .config(conf=test_spark_conf())
        .getOrCreate()
    )

@pytest.fixture(scope='session')
def test_data():
    return {"firstname": "Daniel", "age": "29"}