import argparse
from poetic_emr_serverless.main import run

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_path", help="path to config file", required=True)
    args = parser.parse_args()

    run(args.config_path)


