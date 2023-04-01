# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:24:24 2023

@author: dalib
"""

from setuptools import setup

setup(
    name="Plain_old_weather_station_app",
    version="0.0.1",
    description="Downloads, stores and displays enviroment data from https://meteo.arso.gov.si/met/en/service2/",
    url="https://github.com/RegularEverydayAverageGuy/WeatherStation",
    author="Dalibor Maljurić",
    author_email="dalibor.maljuric@gmail.com",
    license="MIT",
    package_dir = "./WeatherStation/App/"
    python_requires=">=3.7",
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        "async-imgkit<1.0",
        "jinja2<3.0",
        "asyncio-periodic==2019.2",
        "aioprometheus[aiohttp]<21.0",
        "Pillow<9.0",
    ],
    extras_require={
        "st7789": [
            "st7789<1.0",
            "numpy<2.0",
            "spidev<4.0",
            "RPi.GPIO<1.0",
        ],
        "bme680": [
            "bme680<2.0",
            "smbus==1.1.post2",
        ],
    },
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