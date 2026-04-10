## Python Flask Dev

## Table of contents

1. Project description
2. Project setup
3. Contributing guidelines
4. Project documentation
5. Links to support resources
6. Terms of use

## Project description

### What kind of software is this?

Package containing modules with 'helper' functions to support the development of Python Flask applications.

__________________

### Who can use this app?

Python Flask App Developer

__________________

### Project overview

Language(s): [Python](https://www.python.org/)

Framework(s): [Python Flask Framework](https://flask.palletsprojects.com/en/stable/)

Style guide(s):
[Python PEP 8](https://www.python.org/dev/peps/pep-0008)

## Project setup

### Pre-requisites

Before using {Project name}, install necessary pkgs:

* [PKG_NAME](https://www.python.org/downloads/)
* [...]

### Requirements

GitHub will automatically not push any tokens.

However, to commit any changes the .gitignore file must include any files that contain credentials.

If the Markdown Changelog Generator is used, it needs to include  'changelog_generator.toml' because it lists your GitHub repo's PAT (Personal Access Token). 

#### Install Python Flask Dev

1. Install the [PyPi package](https://pypi.org/project/python-flask-dev)
`pip install python-flask-dev`

#### Configure Python Flask Dev

1. Configure any changes as needed, if cloning the project source code.

#### Run Python Flask Dev

1. Import any 'helper' functions throughout your project code; refer to the description on each module for more information.

#### Troubleshoot Python Flask Dev

1. No known issues at this time: P/T, leave a PR with comments or fork off to resolve them in a separate repository. (:

_____________________

#### Using this project

###### Incremental versioning


_____________________

### Recommendations

* When working through a smaller project such as a program or a software application, a Changelog is recommended.

Changelog entries typically follow a basic format that includes information about the code that was added to enhance a project, removed for any purpose, and modified to resolve errors.

Changelog entries are entered in the CHANGELOG file once code is committed to the main branch:

### [VERSION #] - [TIMESTAMP]

#### [ADDED || REMOVED || FIXED]

\<DESCRIPTION\>

___

### Version Control Process
I. **Create a Feature Branch**
Any code updates for a version change -- [Major].[Minor].[Patch] -- should be on a separate branch, referred to as a 'feature' branch.

Once work on the branch is completed, a pull-request can be created to merge the branch into `dev`, a staging/pre-release branch, where those changes are tested.

Once the staging branch is tested, stable code can be merged into `main` a production/release branch.

________________
##### Maintaining repos

###### Branch Naming Conventions

`<VERSION-RELEASE-#>/<FEATURE_NAME>/<CONTRIBUTOR>`

- `<VERSION-RELEASE-#>`: Refer to [SemVer](https://semver.org/) for details

- `<FEATURE_NAME>`: Descriptive title for the feature

- `<CONTRIBUTOR>`: GitHub account name, e.g., https://github.com/<NAME>

IV. **Documenting changes**

Maintaining a CHANGELOG file is always recommended for a quick overview of how the project is progressing.
1. Checkout main locally.
2. From a terminal session, run the commands to use the GitHub ChangeLog Generator.
3. Commit the CHANGELOG file to the remote branch.

`changelog-generator-md`

## Project documentation

### Standard project docs are located in the `{PROJECT_ROOT}` folder.

- README
- LICENSE
- CHANGELOG
    - Refer to the Project dependencies section of the README for more information on generating a CHANGELOG file

## Links

* [<LINK>](<URL>): <LINK_DESC>
* [...]

## Terms of use

Python Flask Dev is licensed under [MIT](https://commons.wikimedia.org/wiki/Template:X11)
