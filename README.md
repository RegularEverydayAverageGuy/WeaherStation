# WeatherStation GUI application
Python GUI application that collects and displays enviroment data from the https://meteo.arso.gov.si/met/en/service2/ website. 
## Installation
Create virtual environment
```
mkdir weatherStation
cd weatherStation
python -m venv .
```
Install application form TestPyPi server
```
pip install weatherStationApp
```
Or you can download the source code directly from repo to you virtual environment
```
git clone https://github.com/RegularEverydayAverageGuy/WeatherStation
```
## Run
Run the application
```
weatherStation
```
You can also run it with the **-u** flag which updates the enviroment data
```
weatherStation -u
```
