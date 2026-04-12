# TODO: configure python interpreter in the test module; some issue as this is a separate module from the source code
import unittest
import logging
from python_flask_dev.packaging.incremental_versioning import IncrementalVersioning


# LOGGING
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class TestStringMethods(unittest.TestCase):
    # def test_manual(self):
    #     version = ""
    #     iv_manual = IncrementalVersioning("manual")
    #     # iv_manual.incremental_versioning()
    #     toml_data = iv_manual.get_toml_data()
    #     logger.info(f"########### toml_data: {toml_data}")
    #     pyproject_version = toml_data["project"].get("version")
    #     self.assertEqual(pyproject_version, version)

    def test_dynamic(self):
        version = "0.0.14"
        iv_dynamic = IncrementalVersioning("dynamic")
        # iv_dynamic.incremental_versioning()
        toml_data = iv_dynamic.get_toml_data()
        logger.info(f"########### toml_data: {toml_data}")

        # read from version.txt file
        with open("version.txt", "r") as f:
            pyproject_version = f.read().strip()

        self.assertEqual(pyproject_version, version)

    # def test_automatic(self):
    #     version = "0.0.14"
    #     iv_automatic = IncrementalVersioning("automatic")
    #     # iv_automatic.incremental_versioning()
    #     toml_data = iv_automatic.get_toml_data()
    #     logger.info(f"########### toml_data: {toml_data}")
    #     pyproject_version = toml_data["project"].get("version")
    #     self.assertEqual(pyproject_version, version)

if __name__ == "__main__":
    unittest.main()
