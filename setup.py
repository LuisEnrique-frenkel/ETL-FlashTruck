# setup.py
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(include=['module']),
    install_requires=[
        'fs',
        'pandas' 
    ],
    include_package_data=True,
)