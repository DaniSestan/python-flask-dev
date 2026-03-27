import os
import sys
import importlib.util
from pathlib import Path
import site


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
VIRTUAL_ENV = Path(os.getenv('VIRTUAL_ENV'))

# opt for module in the local project directory, or module installed in the venv

def get_imported_project_module(module_name, module_path = None,  is_pkg_installation_required = False, add_to_import_system = False):

    if is_pkg_installation_required:
        module_path = f"{site.getsitepackages()[0]}/{module_name}"
    else:
        if module_path == None:
            raise Exception("ERROR: Module path is required for an installed package")

    # Create the module object from the spec
    module_spec = importlib.util.spec_from_file_location(module_name, Path(module_path))
    # Load the module
    custom_module = importlib.util.module_from_spec(module_spec)

    # Optionally add the module to sys.modules so it's treated as a normal import
    if add_to_import_system:
        sys.modules[module_name] = custom_module

    module_spec.loader.exec_module(custom_module)

    # The module  is callable: `custom_module.some_function()`
    return custom_module

# Note that, typically, this is not recommended for python projects
# absolute_path; is_package_installed; module_name;
def modify_venv_pythonpath(*, absolute_pkg_path = None, installed_pkg_name = None):
    if absolute_pkg_path:
        pkg_path = absolute_pkg_path
    elif installed_pkg_name:
        pkg_path = f"{site.getsitepackages()[0]}/{installed_pkg_name}"
    else:
        raise Exception("ERROR: absolute_pkg_path or installed_pkg_name is required")

    # Create/write to a .pth file, listing the path of the package to import:
    site_dir = site.getsitepackages()[0]
    logger.info(f"site_dir: {site_dir}")
    site_pkgs_pth_file = f"{site_dir}/{module_name}.pth"
    pkg_path = f"{site_dir}/{module_name}"
    try:
        with open(site_pkgs_pth_file, 'r') as file:
            lines = [line.strip() for line in file]
    except Exception as e:
        logger.error(e)
        lines = []

    # TODO: [START] - testing comment
    logger.info(f"lines: {lines}")
    # TODO: [END] - testing comment

    if pkg_path not in lines:
        with open(site_pkgs_pth_file, 'a') as file:
            if pkg_path not in lines:
                file.write(pkg_path + '\n')

    # Add the package:
    known_paths = set(sys.path)
    logger.info(f"known_paths: {known_paths}")
    site.addpackage(site_dir, "example_package_SHELLCO_ADMIN.pth", known_paths)
    logger.info(os.listdir(site_dir))

logger.info(f"##### sys.path: {sys.path}")
module_name = "example_package_SHELLCO_ADMIN"
# modify_venv_pythonpath(module_name)
# modify_venv_pythonpath(installed_pkg_name=module_name)
modify_venv_pythonpath(absolute_pkg_path="/home/dani/Work/Work-Projects/sample-projects/my_simple_test/src/example_package_SHELLCO_ADMIN")
logger.info(f"##### sys.path: {sys.path}")
