from setuptools import setup, find_packages
from setuptools import *

setup(
    name = "OwLA",
    version = "1.0.1",
    description = "A CLI to demonstrate our DBMS project.",
    license = "Apache",
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        "click",
    ],
    entry_points = {
        "console_scripts":[
            "owla=owla.cli:cli"
        ]
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)