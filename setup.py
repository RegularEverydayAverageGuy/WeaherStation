# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:24:24 2023

@author: dalib
"""

from setuptools import setup

setup(
    name="Plain_old_weather_station_app",
    version="0.0.1",
    description="Display data from https://meteo.arso.gov.si/met/en/service2/",
    url="https://github.com/RegularEverydayAverageGuy/WeatherStation",
    author="Dalibor Maljurić",
    author_email="dalibor.maljuric@gmail.com",
    license="MIT",
    packages = ['WeatherStation', 'App','DataReaders', 'utils', 'Tests'],
    package_dir={"": "WeatherStation"},
    python_requires=">=3.7",
    install_requires=[
        "astroid==2.15.0",
        "beautifulsoup4==4.11.2",
        "certifi==2022.12.7",
        "colorama==0.4.6",
        "coverage==7.2.1",
        "dill==0.3.6",
        "idna==3.4",
        "isort==5.11.5",
        "lazy-object-proxy==1.9.0",
        "mccabe==0.7.0",
        "platformdirs==3.1.1",
        "pylint==2.17.0",
        "PyQt5==5.15.9",
        "PyQt5-Qt5==5.15.2",
        "PyQt5-sip==12.11.1",
        "requests==2.28.2",
        "soupsieve==2.4",
        "tomli==2.0.1",
        "tomlkit==0.11.6",
        "tqdm==4.65.0",
        "typed-ast==1.5.4",
        "typing_extensions==4.5.0",
        "urllib3==1.26.14",
        "wrapt==1.15.0"
    ],
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
