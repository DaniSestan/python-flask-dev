import json

def get_serialized_data(filepath):
    with open(filepath) as json_file:
        return json.load(json_file)