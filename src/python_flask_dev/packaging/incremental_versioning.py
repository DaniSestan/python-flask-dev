import logging
import requests
import tomllib
import tomli_w
import argparse


# ENV VARS
PYPI_BASE_URL = "https://pypi.org/simple/"

# LOGGING
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class IncrementalVersioning:
    def __init__(self, versioning):
        self.versioning = versioning
        self.toml_data = self.get_toml_data()

    def get_toml_data(self):
        # Read project data from pyproject.toml
        with open("pyproject.toml", "rb") as f:
            toml_data = tomllib.load(f)

        return toml_data

    def get_pypi_repository_data(self):
        # Retrieve latest version from PyPI API data
        toml_data = self.get_toml_data()
        project_name = toml_data["project"]["name"]
        pypi_project_url = f"{PYPI_BASE_URL}{project_name}"
        resp = requests.get(pypi_project_url, headers={"Accept": "application/vnd.pypi.simple.v1+json"}).json()

        project_versions = resp["versions"]
        project_versions_sorted = sorted(project_versions, key=lambda x: list(map(int, x.split('.'))), reverse=True)
        project_latest_version = project_versions_sorted[0]

        return {"project_name": project_name, "pypi_project_url": pypi_project_url, "project_versions": project_versions, "project_latest_version": project_latest_version}

    def update_pyproject_config(self, toml_data):
        with open("pyproject.toml", "wb") as f:
            tomli_w.dump(toml_data, f)

    def set_version_manually(self):
        toml_data = self.get_toml_data()

        if "version" not in toml_data["project"]:
            toml_data["project"]["version"] = ""
            self.update_pyproject_config(toml_data)

        try:
            if "version" in toml_data["project"]["dynamic"]:
                toml_data["project"]["dynamic"].remove("version")
                self.update_pyproject_config(toml_data)
        except Exception as e:
            logging.info(f"######## ERROR: {e}; 'dynamic' is not a project table key in pyproject.toml; however, it is not required to set the version number manually.")

        logging.info(f"################ toml_data: {toml_data['project']}")
        logging.info("Manual versioning selected. Please update the version number in pyproject.toml manually.")

    def set_version_dynamically(self):
        toml_data = self.get_toml_data()

        if "version" in toml_data["project"]:
            del toml_data["project"]["version"]
            self.update_pyproject_config(toml_data)

        if "version" not in toml_data["project"]["dynamic"]:
            toml_data["project"]["dynamic"].append("version")
            self.update_pyproject_config(toml_data)

        logging.info("Dynamic versioning selected. Please set the version number in the 'version.txt' file.")

    def set_version_automatically(self):
        toml_data = self.get_toml_data()

        project_name, pypi_project_url, project_versions, project_latest_version = self.get_pypi_repository_data().values()

        # Change the version number
        project_versioning_list = project_latest_version.split(".")
        # TODO: int to string
        project_versioning_list[2] = f"{int(project_versioning_list[2]) + 1}"
        logger.info(f"######## project_versioning_list: {project_versioning_list}")
        new_project_version = '.'.join(project_versioning_list)
        logger.info(f"######## new_project_version: {new_project_version}")

        # Write the new version number
        toml_data["project"]["version"] = new_project_version
        if "version" in toml_data["project"]["dynamic"]:
            toml_data["project"]["dynamic"].remove("version")
        self.update_pyproject_config(toml_data)
        logging.info(f"Automatic versioning selected. Version number updated to {new_project_version} in pyproject.toml.")

    def incremental_versioning(self):
        versioning = self.versioning
        toml_data = self.get_toml_data()

        # if "version" not in toml_data["project"]:
        #     toml_data["project"]["version"] = ""
        #     update_pyproject_config(toml_data)

        if "dynamic" not in toml_data["project"]:
            toml_data["project"]["dynamic"] = []
            self.update_pyproject_config(toml_data)

        logging.info(f"######## pypi_project_url: {f"{PYPI_BASE_URL}{toml_data["project"]["name"]}"}")
        logging.info(f"######## Project: {self.get_pypi_repository_data()['project_name']}")
        logging.info(f"######## Version: {self.get_pypi_repository_data()['project_latest_version']}")

        if versioning == "manual":
            self.set_version_manually()
        elif versioning == "dynamic":
            self.set_version_dynamically()
        elif versioning == "automatic":
            self.set_version_automatically()
        else:
            logging.info(f"######versioning: {versioning}")
            logging.info("Defaulting to manual versioning. Options: 'automatic', 'dynamic', 'manual'")
            self.set_version_manually()

if __name__ == "__main__":
    pass
    # TODO: [START] comment as needed if testing this
    # v = "foo_bar_baz"
    # v = "manual"
    # v = "dynamic"
    # v = "automatic"
    # iv = IncrementalVersioning(v)
    # iv.incremental_versioning()
    # TODO: [END] comment as needed if testing this
