# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:17:17 2023

@author: dalib
"""
import sys
import argparse
from PySide6.QtWidgets import QApplication
from WeatherStation.App import WeatherStationApp
from WeatherStation.App import DownloadData

progDescription = "Downloads, stores and displayes enviroment data from https://meteo.arso.gov.si/met/en/service2/"
parser= argparse.ArgumentParser(prog="WeatherStationApp", description=progDescription)

parser.add_argument("-u", "--update", action="store_true", help="Updates the weather data from ARSO website")
args = parser.parse_args()

if __name__ == '__main__':
    
    #Is data update chosen
    if(args.update):
        DownloadData.runUpdate()
    
    app = QApplication(sys.argv)
    w = WeatherStationApp.MainWindow()
    w.show()
    app.exec()
    