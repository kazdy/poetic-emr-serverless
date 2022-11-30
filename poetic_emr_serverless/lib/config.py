from yaml import safe_load
from cloudpathlib import AnyPath

def get_config(path: str) -> dict[str,str]:
    path = AnyPath(path)
    with path.open('r') as file:
        config = safe_load(file)
        return config
