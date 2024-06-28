from setuptools import find_packages, setup
from typing import List

Hypen_E_dot = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """Return a list of requirements from the given file_path."""
    requirements = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj:
            req = line.strip()
            if req and req != Hypen_E_dot:
                requirements.append(req)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Anand Kumar',
    author_email='h20220277@pilani.bits-pilani.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)
