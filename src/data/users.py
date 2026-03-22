import os
from pathlib import Path
# TODO: [START] uncomment when testing, until junit tests are implemented in this repo
#
# TODO: [END] uncomment when testing, until junit tests are implemented in this repo

from ..dev_modules.data_source import convert_to_dict

PROJECT_ROOT = Path(os.getenv('VIRTUAL_ENV')).parent.absolute()
FILENAME = f"{PROJECT_ROOT}/src/data/users.json"

data = convert_to_dict(FILENAME)

def get_users(index=None):
    if index:
        transformed_data = {
            item["id"]: {k: v for k, v in item.items() if k != "id"}
            for item in data
        }
        return transformed_data

    return data
