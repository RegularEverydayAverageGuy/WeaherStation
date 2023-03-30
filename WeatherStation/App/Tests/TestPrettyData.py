# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 12:17:44 2023

@author: dalib
"""

import unittest
from unittest.mock import patch, mock_open
from DataReaders import HtmlReader
from PrettyData import PrettyData

class TestPrettyData(unittest.TestCase):
    '''Tests functions from the PrettyData module'''
    @classmethod
    def setUpClass(cls):
        cls.reader = HtmlReader.HTMLReader("C:/Data/test.html")
        cls.prettyData = PrettyData(cls.reader)
        
    def testRunReader(self):
        '''Test whether the reader when encounterd with empty files'''
        #Test with empty file
        mockFile = mock_open(read_data="")
        with patch("builtins.open", mockFile):
            success = self.prettyData.runReader()
            
        self.assertTrue(success)
        self.assertEqual(self.reader.contents.getText(), "")
        
    def testUpdateReader(self):
        '''Test whether the reader updates succesfully'''
        newFilename = "C:/Data/newTest.html"
        mockFile = mock_open(read_data= "<html><title>NewData</title></html>")
        with patch("builtins.open", mockFile):
            success = self.prettyData.updateReader(newFilename)
            
        self.assertTrue(success)
        self.assertEqual(self.prettyData.reader.filename, newFilename)
        self.assertEqual(self.prettyData.reader.contents.getText(), "NewData")
    
    def testClearDataTable(self):
        '''Tests whether the clearDataTable function clears the dictionary properly'''
        self.prettyData.dataTable = {"Data0":list(range(0,5)), "Data1":list(range(5,0,-1))}
        self.prettyData.clearDataTable()
        
        self.assertEqual(self.prettyData.dataTable, {})
                                            