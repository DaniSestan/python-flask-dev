# imports modules within the project
import os
import sys
import importlib.util
from pathlib import Path


project_root = Path(os.getenv('VIRTUAL_ENV')).parent.absolute()
virtual_env = Path(os.getenv('VIRTUAL_ENV'))
python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"

# Import modules from a specified path
def get_imported_project_module(module_name, absolute_module_path, add_to_import_system = False):
    abs_mod_path = Path(absolute_module_path)
    module_spec = importlib.util.spec_from_file_location(module_name, Path(absolute_module_path))
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

