import pprint as pp
import argparse
import pandas as pd
import os
from pathlib import Path
from custom_exceptions import CustomError

# TODO: [START] uncomment when testing, until junit tests are implemented in this repo
# ENV VARS
PROJECT_ROOT = Path(os.getenv('VIRTUAL_ENV')).parent.absolute()

# ENV VARS SET FROM PARSER
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename')      # option that takes a value

args = parser.parse_args()
FILENAME = args.filename if args.filename else f"{PROJECT_ROOT}/data/users.json"
# FILENAME = args.filename
# TODO: [END] uncomment when testing, until junit tests are implemented in this repo

def convert_to_dict(filename=FILENAME):
    accepted_filetypes = ['json']
    filetype = filename.split(".")[1]

    if filetype == "json":
        dataframe = pd.read_json(filename)
        return dataframe.to_dict()
    # TODO: CSV
    else:
        err_msg = f"Accepted filetypes: {str(accepted_filetypes)}"
        raise CustomError(err_msg, 401)
