from flask import Flask
import pandas as pd
import logging
import builtins
# modify the import statement to be able to import the CustomError class in this module when this module is imported outside of the dev_modules package:
from custom_exceptions import CustomError
from importing_modules import get_imported_project_module
# ce = get_imported_project_module("custom_error", add_to_import_system=True)


app = Flask(__name__)
logger = logging.getLogger(__name__)

# Note that either the dict or the filepath can be a data source
def get_filtered_key_vals(key, key_val_format, dictionary = None, json_filepath = None):
    data = dictionary if dictionary else pd.read_json(json_filepath).to_dict()

    if key_val_format in dir(builtins):
        if key_val_format == "dict":
            return data.get(key)
        elif key_val_format == "list":
            return list(data.get(key).values())
        # TODO: add diff data types here
        else:
            err_msg = f"The selected format, {key_val_format}, is not a supported data type"
            raise CustomError(err_msg, 401)
            # raise ce.CustomError(err_msg, 401)
    else:
        err_msg = f"The selected format, {key_val_format}, is not a builtin Python data type"
        raise CustomError(err_msg, 401)
        # raise ce.CustomError(err_msg, 401)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    filepath = "sample_data/users.json"
    data = get_filtered_key_vals("username", "dict", json_filepath=filepath)
    logger.info(f"Data: {data}")
    app.run(debug=True)
