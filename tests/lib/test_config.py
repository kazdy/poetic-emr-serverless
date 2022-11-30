from poetic_emr_serverless.lib.config import get_config

def test_handle_config(spark):
    expected = {"source": "/source", "destination": "/destination"}

    actual = get_config("tests/data/config.yaml")
    
    assert expected == actual


