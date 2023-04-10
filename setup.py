# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:24:24 2023

@author: dalib
"""
from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="UTF-8")

with open("requirements.txt", 'r', encoding = "UTF-8") as f:
    required = f.read().splitlines()

setup(
    name="WeatherStationApp",
    version="0.0.1",
    description="Display data from https://meteo.arso.gov.si/met/en/service2/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RegularEverydayAverageGuy/WeatherStation",
    author="Dalibor Maljuric",
    author_email="dalibor.maljuric@gmail.com",
    license="MIT",
    packages = find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=required,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={
        "console_scripts": ["WeatherStation=WeatherStation.weatherStation:main"],
    },
)
