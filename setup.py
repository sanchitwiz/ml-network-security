'''
The setup.py file is used to specify the configuration for packaging and distributing a Python project. It typically includes metadata about the project, such as its name, version, author, and description, as well as information about dependencies and entry points for command-line interfaces. The setup.py file is essential for creating distributable packages that can be uploaded to repositories like PyPI or installed using pip.
'''

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    """
    try:
        requirements = []
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            [req.replace("\n", "") for req in requirements ]
            print(requirements)

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)

        return requirements
    except FileNotFoundError as e:
        print(e)

setup(
    name="network-security",
    version='0.0.1',
    author="Sanchit Vohra",
    author_email="sanchitvohra13@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)