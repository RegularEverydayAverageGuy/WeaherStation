# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:17:17 2023

@author: dalib
"""
import sys
from PySide6.QtWidgets import QApplication
from App import WeatherStationApp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WeatherStationApp.MainWindow()
    w.show()
    app.exec()
    