# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:48:03 2023

@author: dalib
"""

from DataReaders.HtmlReader import DataReader

class PrettyData():
    '''Class which retrives data and holds data from the Data directory'''
    def __init__(self, dataReader: DataReader):
        self.reader = dataReader
        self.reader.readFile()
        self.dataTable = dict()
    
    def updateReaderContents(self, filename):
        '''Updates data from file with passed filename'''
        self.reader.setFilename(filename)
        self.reader.readFile()
    
    def populateDataTable(self):
        '''Populates the data table with chosen data'''
        self.__getTimeData()
        self.__getTemperature()
        self.__getWindSpeed()
        self.__getHumidity()
        
    def __getTemperature(self):
        '''Retrives temprature data from file with help of DataReader object'''
        title = self.reader.getData("th", {"class":"t"})
        data = self.reader.getData("td", {"class": "t"})
        
        #Add data to table only if valid
        if len(title) == 1 and data:
            self.dataTable[title[0]] = data
    
    def __getWindSpeed(self):
        '''Retrives wind speed data from file with help of DataReader object'''
        title = self.reader.getData("th", {"class":"ff_val:f1"})
        data = self.reader.getData("td", {"class": "ff_val"})
        
         #Add data to table only if valid
        if len(title) == 1 and data:
            self.dataTable[title[0]] = data
        
    def __getHumidity(self):
        '''Retrives humidity data from file with help of DataReader object'''
        title = self.reader.getData("th", {"class":"msl"})
        data = self.reader.getData("td", {"class": "msl"})
        
         #Add data to table only if valid
        if len(title) == 1 and data:
            self.dataTable[title[0]] = data
        
    def __getTimeData(self):
        '''Retrives time data from file with help of DataReader object'''
        data = self.reader.getData("td", {"class":"meteoSI-th"})
        
         #Add data to table only if valid
        if data:
            self.dataTable["Time"] = data
    
    def __getCityName(self):
        '''Retrives location data from file with help of DataReader object'''
        cityName = self.reader.getData("th", {"class":"meteoSI-header"})

        #Add data to table only if valid
        if cityName:
            self.dataTable["CityName"] = cityName