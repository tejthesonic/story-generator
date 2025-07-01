from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def reqs (file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
    requirements= [i.replace("/n"," ") for i in requirements]
    
    for HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name="temptemp-jet",
version="0.0.1",
author="temp",
author_email="tempforclg@gmail.com",
packages=find_packages(),
install_requires=reqs("requirements.txt"),
)