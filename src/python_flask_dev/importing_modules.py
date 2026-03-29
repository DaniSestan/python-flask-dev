import os
import sys
import importlib.util
from pathlib import Path
import site
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_imported_project_module(module_name, module_path = None, add_to_import_system = False):
    logger.info(f"##### module_path: {module_path}")
    # Create the module object from the spec
    module_spec = importlib.util.spec_from_file_location(module_name, Path(module_path))
    logger.info(f"##### module_spec: {module_spec}")
    # Load the module
    custom_module = importlib.util.module_from_spec(module_spec)

    # Optionally add the module to sys.modules so it's treated as a normal import
    if add_to_import_system:
        sys.modules[module_name] = custom_module

    module_spec.loader.exec_module(custom_module)

    # The module  is callable: `custom_module.some_function()`
    return custom_module

# Note that, typically, this is not recommended for python projects; Modules located within the directory that is added to the search path can be imported.
def modify_venv_pythonpath(*, pth_filename = "imported-project-modules.pth", absolute_pkg_path = None, installed_pkg_name = None):
    site_dir = site.getsitepackages()[0]
    logger.info(f"########## site_dir: {site_dir}")

    if absolute_pkg_path:
        pkg_path = absolute_pkg_path
    elif installed_pkg_name:
        pkg_path = f"{site_dir}/{installed_pkg_name}"
    else:
        raise Exception("ERROR: absolute_pkg_path or installed_pkg_name is required")

    # Create/write to a .pth file, listing the path of the package to import:
    site_pkgs_pth_filepath = f"{site_dir}/{pth_filename}"
    try:
        with open(site_pkgs_pth_filepath, 'r') as file:
            lines = [line.strip() for line in file]
    except Exception as e:
        logger.error(e)
        lines = []

    logger.info(f"########## pkg_path: {pkg_path}")
    logger.info(f"########## lines: {lines}")

    if pkg_path not in lines:
        with open(site_pkgs_pth_filepath, 'a') as file:
            if pkg_path not in lines:
                logger.info(f"########## writing to site-pkgs .pth; pkg_path: {pkg_path}")
                file.write(pkg_path + '\n')

    # Add the package:
    known_paths = set(sys.path)
    logger.info(f"########## known_paths: {known_paths}")
    site.addpackage(site_dir, site_pkgs_pth_filepath, known_paths)
    if pkg_path in os.listdir(site_dir):
        logger.info(f"########## `{pkg_path}` package added to the Python packages search system path")
