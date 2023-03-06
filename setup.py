from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    this function withh return list of required packages
    '''
    requirments = []

    with open(file_path) as obj:
        requirments = obj.readlines()
        requirments = [obj.replace("\n", "") for obj in requirments]
    if HYPEN_E_DOT in requirments:
        requirments.remove(HYPEN_E_DOT)


setup(
name = 'mlproject',
version = '0.0.0.1',
author= 'RAVIRAJ KUKADE',
author_email= 'ravirajkukade11@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
)