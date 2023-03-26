# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:48:03 2023

@author: dalib
"""

import math
from DataReaders.HtmlReader import DataReader

class PrettyData():
    '''Class which retrives data from a file with the help of the passed reader object
       and stores in a form of a dictionary'''
    
    def __init__(self, dataReader: DataReader):
        self.reader = dataReader
        self.dataTable = {}

    def runReader(self):
        '''Reads the file contets with the help of the reader object'''
        self.reader.readFile()
        
    def updateReader(self, filename):
        '''Updates data from file with passed filename'''
        self.reader.setFilename(filename)
        self.runReader()

    def populateDataTable(self):
        '''Populates the data table with chosen data'''
        self._getCityName()
        self._getTimeData()
        self._getTemperature()
        self._getWindSpeed()
        self._getPressure()
        
    def clearDataTable(self):
        '''Clear the data fro mthe data table'''
        if self.dataTable:
            self.dataTable = self.dataTable.clear()
            self.dataTable = {}
            
    def updateDataTable(self):
        '''Update the contents of the data table'''
        self.clearDataTable()
        self.populateDataTable()
            
    def _getTemperature(self):
        '''Retrives temprature data from file with help of DataReader object'''
        data = self.reader.getData("td", {"class": "t"})
        #Add data to table only if valid
        if data:
            for count, value in enumerate(data):
                try:
                    data[count] = float(value)
                except ValueError:
                    data[count] = math.nan
                    
            self.dataTable["Temperature [°C]"] = data
    
    def _getWindSpeed(self):
        '''Retrives wind speed data from file with help of DataReader object'''
        data = self.reader.getData("td", {"class": "ff_val"})
         #Add data to table only if valid
        if data:
            for count, value in enumerate(data):
                try:
                    data[count] = float(value)
                except ValueError:
                    data[count] = math.nan
                    
            self.dataTable["Wind speed [km/h]"] = data
        
    def _getPressure(self):
        '''Retrives humidity data from file with help of DataReader object'''
        data = self.reader.getData("td", {"class": "msl"})
         #Add data to table only if valid
        if data:
            for count, value in enumerate(data):
                try:
                    data[count] = float(value)
                except ValueError:
                    data[count] = math.nan
                    
            self.dataTable["Pressure [hPa]"] = data
        
    def _getTimeData(self):
        '''Retrives time data from file with help of DataReader object'''
        data = self.reader.getData("td", {"class":"meteoSI-th"})
         #Add data to table only if valid
        if data:
            self.dataTable["Time"] = data
    
    def _getCityName(self):
        '''Retrives location data from file with help of DataReader object'''
        cityName = self.reader.getData("th", {"class":"meteoSI-header"})
        #Add city name to data table
        if cityName:
            self.dataTable["CityName"] = cityName
        else:
            self.dataTable["CityName"] = ""
