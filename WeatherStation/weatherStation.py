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

progDescription = "Downloads, stores and displayes enviroment data"
parser= argparse.ArgumentParser(prog="WeatherStationApp", description=progDescription)

helpText = "Updates the weather data from ARSO website"
parser.add_argument("-u", "--update", action="store_true", help=helpText)
args = parser.parse_args()

def main():
    ''''Runs the WeatherStationApp application'''
    #Is data update chosen
    if args.update:
        DownloadData.runUpdate()
    
    app = QApplication(sys.argv)
    appWindow = WeatherStationApp.MainWindow()
    appWindow.show()
    app.exec()

if __name__=="__main__":
    main()
    