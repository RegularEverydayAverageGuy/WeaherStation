# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:24:24 2023

@author: dalib
"""
from setuptools import setup, find_packages

with open("C:/Projekti/RLS/WeatherStation/requirements.txt", 'rb') as f:
    required = f.read().splitlines()

setup(
    name="WeatherStationApp",
    version="0.0.6",
    description="Display data from https://meteo.arso.gov.si/met/en/service2/",
    url="https://github.com/RegularEverydayAverageGuy/WeatherStation",
    author="Dalibor Maljurić",
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
        "console_scripts": ["WeatherStation=WeatherStation.cli:main"],
    },
)
