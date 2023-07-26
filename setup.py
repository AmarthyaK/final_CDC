from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filename:str)-> List[str]:
    #this function will read the requirements.txt file
    requirements = []
    with open(filename) as f:
        for line in f:
            requirements.append(line.strip())
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name = 'final_CDC',
    version = '0.0.1',
    author = 'AmarthyaK',
    author_email = 'pragnayamarthyak41@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)