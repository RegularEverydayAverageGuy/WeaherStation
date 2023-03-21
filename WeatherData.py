# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:48:03 2023

@author: dalib
"""

from DataReaders import DataReader

class WeatherData():
    def __init__(self, dataReader: DataReader):
        self.reader = dataReader
        self.reader.readFile()
    
    def updateData(self, filename):
        '''Updates data from file with passed filename'''
        self.reader.setFilename(filename)
        self.reader.readFile()
        
    def getTemperature(self):
        '''Retrives temprature data from file with help of DataReader object'''
        data = self.reader.getData()
        if data:
            return data
        else:
            return []
    
    def getWindSpeed(self):
        '''Retrives wind speed data from file with help of DataReader object'''
        data = self.reader.getData()
        if data:
            return data
        else:
            return []
        
    def getHumiditySpeed(self):
        '''Retrives humidity data from file with help of DataReader object'''
        data = self.reader.getData()
        if data:
            return data
        else:
            return []
        