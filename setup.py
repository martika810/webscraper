#!/usr/bin/env python
from setuptools import setup

with open("./requirements.txt") as requirements_file:
    requirements = [
        requirement for requirement in requirements_file.read().split("\n")
        if requirement != ""
    ]
setup(
    name = 'webscraper',
    packages = ['webscraper','webscraper/config'],
    package_dir ={
        "webscraper":"webscraper"
    },
    py_modules=["webscraper"],
    version = '1.0.0',
    entry_points = """
        [console_scripts]
        webscraper = webscraper.webapp:main
    """ ,
    install_requires = requirements,
    keywords = "webscraper"
)