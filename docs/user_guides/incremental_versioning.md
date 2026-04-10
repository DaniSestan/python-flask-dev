# Incremental Versioning

Using this package, you can make incremental changes to a python project set up with pyproject.toml without having to manually or dynamically update the version number with each PyPi repository push.

### Overview on the build process
#### Create the package
- Include the 'standard' python project files
- Create a config.py file in the content root of your project:
[//]: # TODO: import this in a different pkg, then run this from config.py
  ```
  from python_flask_dev.packaging import incremental_versioning as iv
  
  
  VERSIONING = "manual" || "dynamic" || "automatic"

  if __name__ == "__main__":
    iv.incremental_versioning(VERSIONING)
  ```
- [Optional] Importing this package in config.py takes the pie slice on manually configuring a project with pyproject.toml 
  - In the pyproject.toml file, specify the requirements for the build process:
   
  _Manually setting the version number:_
    
   ```
   [project]
   version = "0.0.9"
   ```
       
   _Dynamically setting the version number:_
   ```
   [project]
   dynamic = ["version"]

   [tool.setuptools.dynamic]
   version = {file = "version.txt"}
   ```
- [Recommended] The PEP standard recommends the following for setting up projects through pyproject.toml without a setup.py file
- Required pkgs for the build process:
  ```
  [build-system]
  requires = ["setuptools >= 77.0.3"]
  build-backend = "setuptools.build_meta"
  ```
- List pkgs required for building and uploading the distro archive files:
  ```
    dependencies = [
        "build==1.4.0",
        "twine==6.2.0"
    ]
  ```
- List the path of the package directory:
  ```
  [tool.setuptools.packages.find]
  package-dir = {"" = "src"}
  ```
- Create a `version.txt` file
### Create distro archives
- Create a package within the project directory
- Generate dist pkgs, which are the pkg archives uploaded to the pkg index to be installed by pip:
    - Install the pkgs:
      `pip install -e .`
    - Run the script to customize any build config settings prior to building pkg distro:
      `python3 config.py`
    - Build the distribution archives:
      `python3 -m build`

The files created in this process are the tar.gz file (the src distro) .whl file (the built distro). Note that it's best practice to always install a src distro, as part of the build process.

#### Upload the distro archives

- Once you have registered a [PyPI](https://pypi.org/) or [TestPyPI](https://test.pypi.org/) account, create an API token, with the scope set to 'Entire account'.
- Install the Twine pkg necessary to upload all the archives under `dist`:
- Run the twine cmd to upload the `dist` archives:
    - PyPI:
      `python3 -m twine upload dist/*`
    - TestPyPI:
      `python3 -m twine upload --repository testpypi dist/*`

- Note the pkg name generated from the build process; the easiest option to locate it is from the pkg url endpoint; e.g. https://test.pypi.org/project/example-package-SHELLCO-ADMIN/0.0.1/

#### Install the package
- Install the pkg from TestPyPI: `pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-SHELLCO-ADMIN`
    - If the package is being upgraded: `pip install --index-url https://test.pypi.org/simple/ --no-deps --upgrade example-package-SHELLCO-ADMIN`
- Test if the installation was successful: `pip list`

### Additional links
- https://packaging.python.org/tutorials/packaging-projects/
- https://www.youtube.com/watch?v=h6oa_FwzFwU