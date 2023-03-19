# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:25:49 2023

@author: dalib
"""

import unittest
from unittest.mock import patch, mock_open
from DataReaders import HtmlReader

class TestHTMLReader(unittest.TestCase):
    '''Test class for testing the XMLReader functionality'''
    @classmethod
    def setUpClass(cls):
        cls.reader = HtmlReader.HTMLReader("C:/Data/test.html")
        cls.mockFile = mock_open(read_data="<html><title>Data</title></html>")
     
    def testFilenameSetter(self):
        '''Tests whether the filename is set correctly'''
        self.reader.setFilename("C:/Data/newTest.html")
        self.assertEqual(self.reader.filename, "C:/Data/newTest.html")
        
    def testWrongFormat(self):
        '''Tests whether the HTMLReader rejects a wrong file format'''
        self.reader = HtmlReader.HTMLReader("C:/Data/test.xml")
        success = self.reader.readFile()
        self.assertFalse(success)      
        
        self.reader = HtmlReader.HTMLReader("C:/Data/test.txt")
        success = self.reader.readFile()
        self.assertFalse(success) 
   
    def testCorrectFormat(self):
        '''Tests whether the function properly reads a file in correct format'''
        self.reader = HtmlReader.HTMLReader("C:/Data/test.html")
        with patch("builtins.open", self.mockFile):
            success = self.reader.readFile()
        
        self.assertTrue(success)
        self.assertEqual(self.reader.contents.title.text,"Data")
        
    def testEmptyRetrivedData(self):
        '''Tests whether the retrived data given the input identifier is empty'''
        with patch("builtins.open", self.mockFile):
            success = self.reader.readFile()
        self.assertTrue(success)
        
        if success:
            data = self.reader.getData("")
            self.assertEqual(data, [])

    def testNonEmptyRetrivedData(self):
        '''Tests whether the retrived data given the input identifier is correct'''
        self.reader = HtmlReader.HTMLReader("C:/Data/test.html")
        with patch("builtins.open", self.mockFile):
            success = self.reader.readFile()
        self.assertTrue(success)
        
        if success:
            data = self.reader.getData("title")
            self.assertEqual(data, ["Data"])
