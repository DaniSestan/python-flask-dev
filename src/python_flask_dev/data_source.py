# TODO: coffee finish this create data_source pkg to avoid import error
import argparse
import pandas as pd
import os
from pathlib import Path
# from ..custom_exceptions import CustomError

# ENV VARS
PROJECT_ROOT = Path(os.getenv('VIRTUAL_ENV')).parent.absolute()

# ENV VARS SET FROM PARSER
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename')      # option that takes a value
args = parser.parse_args()
FILENAME = args.filename if args.filename else f"{PROJECT_ROOT}/data/users.json"

class DataSource:
    def __init__(self, filename=FILENAME):
        self.filename = filename

    def get_accepted_filetypes(self):
        return ['json', 'csv']

    def convert_to_dict(self):
        accepted_filetypes = ['json', 'csv']
        filetype = Path(self.filename).suffix

        if filetype == "json":
            return pd.read_json(self.filename).to_dict()
        elif filetype == "csv":
            return pd.read_csv(self.filename).to_dict()
        # else:
        #     err_msg = f"Accepted filetypes: {str(accepted_filetypes)}"
        #     raise CustomError(err_msg, 401)
