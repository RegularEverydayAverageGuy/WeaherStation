# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:10:12 2023

@author: dalib
"""

import unittest
from utils import utils

#Tests the utils module
class TestUtils(unittest.TestCase):
    '''Tests functions from the utils module'''
    
    def testFilesURL(self):
        '''Testsformed URLs which dont have the filenames passed'''
        resultingURLs = utils.formFileURLs("https://test.gov.si/", [])
        self.assertFalse(resultingURLs)
        
    def testFilesURLSize(self):
        '''Tests formed URLs size'''
        resultingURLs = utils.formFileURLs("https://test.gov.si/", ["filename"])
        self.assertTrue(len(resultingURLs) == 1)
        
    def testFilesURLValidity(self):
        '''Tests formed if the formed URLs are formed properly'''
        resultingURLs = utils.formFileURLs("https://test.gov.si/", ["testFilename"])
        self.assertTrue("https://test.gov.si/testFilename" == resultingURLs[0])
        
    def testDownloadFilesNoURL(self):
        '''Tests if download and storing of files fails if not valid arguments are given'''
        success = utils.downloadFiles([], [])
        self.assertFalse(success)
        
    def testDownloadFilesNoFilenames(self):
        '''Tests formed URL which dont have corresponding filnemanes to store'''
        success = utils.downloadFiles(["https://test.gov.si/testfilename"], [])
        self.assertFalse(success)
    
    def testValidURL(self):
        '''Test if valid URLs store properly store downloaded data'''
        url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/"
        filename = "observation_CELJE_history.html"
        success = utils.downloadFiles([url+filename], [filename])
        self.assertTrue(success)
