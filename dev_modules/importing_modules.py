# imports modules within the project
import os
import sys
import importlib.util
from pathlib import Path

# TODO: write down the process steps of how to configure the project - NOTE: NO modifying the project path

# - create a venv: python -m venv venv
# activate the venv: source venv/bin/activate
# create a pyproject.toml file; add the file to the technical documentation folder, you can use this as a template
# create a setup.py file with a list of the required pkgs
# TODO: there is some issue with the setuptools pkg; this is specified in the project build config in the pyproject.toml file - however it's possible that it needs to be installed prior to installing the pkgs listed in the setup file - that kind of seems like a circular issue
# install the pkgs, setting the 'editable' flag in the pip command: pip install -e .

project_root = Path(os.getenv('VIRTUAL_ENV')).parent.absolute()
virtual_env = Path(os.getenv('VIRTUAL_ENV'))
python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"

# Import modules from a specified path
def get_imported_project_module(module_name, add_to_import_system = False):
    custom_modules_data = {"mod": "./dev_modules/mod.py", "custom_error": "./dev_modules/custom_exceptions.py"}
    abs_mod_path = Path(f"./{custom_modules_data.get(module_name)}")
    module_spec = importlib.util.spec_from_file_location(module_name, abs_mod_path)
    if module_spec is not None:
        # Create the module object from the spec
        custom_module = importlib.util.module_from_spec(module_spec)

        # Optionally add the module to sys.modules so it's treated as a normal import
        if add_to_import_system:
            sys.modules[module_name] = custom_module

        module_spec.loader.exec_module(custom_module)

        # # Now you can use it like a regular module
        # custom_module.some_function()
        return custom_module
    else:
        print(f" Could not find or create a spec for {abs_mod_path}")
        return None

# Note that, typically, this is not recommended for python projects
def modify_venv_pythonpath(pkg_path, absolute_path=False):
    site_pkgs_pth_file = f"{virtual_env}/lib/{python_version}/site-packages/{Path(project_root).name}.pth"
    print("site_pkgs_pth_file: ", site_pkgs_pth_file)
    with open(site_pkgs_pth_file, "w") as f:
        path = pkg_path if absolute_path else f"{project_root}/{pkg_path}"
        f.write(path)

