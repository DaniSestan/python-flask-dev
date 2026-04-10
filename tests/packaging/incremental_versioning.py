# TODO: resolve some issue with version key in the project table
import unittest
import logging
import requests
import tomllib
import tomli_w
import argparse
from python_flask_dev.packaging import incremental_versioning as iv
import os
from pathlib import Path


# LOGGING
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
version = "0.0.0"

def get_toml_data():
    with open(f"pyproject.toml", "rb") as f:
        toml_data = tomllib.load(f)

    return toml_data

class TestStringMethods(unittest.TestCase):
    def test_manual(self):
        global version
        versioning = "manual"
        iv.incremental_versioning(versioning)
        toml_data = get_toml_data()
        logger.info(f"########### toml_data: {toml_data}")
        pyproject_version = toml_data["project"]["version"]
        self.assertEqual(pyproject_version, version)

    def test_dynamic(self):
        global version
        versioning = "dynamic"
        iv.incremental_versioning(versioning)
        toml_data = get_toml_data()
        logger.info(f"########### toml_data: {toml_data}")
        pyproject_version = toml_data["project"]["version"]
        self.assertEqual(pyproject_version, version)

    def test_automatic(self):
        global version
        versioning = "automatic"
        iv.incremental_versioning(versioning)
        toml_data = get_toml_data()
        logger.info(f"########### toml_data: {toml_data}")
        pyproject_version = toml_data["project"]["version"]
        self.assertEqual(pyproject_version, version)

if __name__ == "__main__":
    data = get_toml_data()
    # logger.info(f"############: {data}")

    version = "0.0.5"
    unittest.main()
