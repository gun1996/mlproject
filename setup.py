from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) ->List[str]:
    requirement=[]
    HYPHEN_DOT='-e.'
    with open(file_path) as filepath:
        requirement=filepath.readlines()
        requirement=[require.replace("\n","") for require in requirement]

        if HYPHEN_DOT in requirement:
            requirement.remove(HYPHEN_DOT)
    
    return requirement


setup (
name='mlproject',
version='0.0.1',
author_email='singhguneesh@gmail.com',
author='Guneesh',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)