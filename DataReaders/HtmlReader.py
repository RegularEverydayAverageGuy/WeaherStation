# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:57:31 2023

@author: dalib
"""

from abc import ABC, abstractmethod
import os
from bs4 import BeautifulSoup

class DataReader(ABC):
    '''Base class for extracting varios types of data (XML,txt etc..)'''
    def __init__(self):
        '''Abstract class DataReader __init__'''
    
    @abstractmethod
    def readFile(self):
        '''Opens a file with filename'''  
    
    @abstractmethod
    def getData(self, *dataIdentifier):
        ''''Retrievs specififc data from the file'''
    
    @abstractmethod
    def setFilename(self, filename):
        '''Sets the filename of the DataReader'''
    
class HTMLReader(DataReader):
    '''Sublclass of DataExtractor which extracts data in .xml format'''
    def __init__(self, filename):
        self.filename = filename
        self.contents = BeautifulSoup()
    
    def setFilename(self, filename):
        '''Sets the filename of the HTMLReader'''
        self.filename = filename
    
    def readFile(self):
        '''Checks and opens a .html file'''
        response = os.path.splitext(self.filename)
        if response[1] == ".html":
            with open(self.filename, "rb") as file:
                self.contents = BeautifulSoup(file, "html.parser")
            return True
        
        return False
    
    def getData(self, *dataIdentifier):
        '''Function that retrives data from HTML file based on the given identifier'''
        data = []
        retrivedValues = self.contents.find_all(*dataIdentifier)
        for value in retrivedValues:
            data.append(value.text)
        
        return data
