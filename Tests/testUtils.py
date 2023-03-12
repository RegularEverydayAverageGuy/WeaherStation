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
    #Tests the FormFilesURLs from utils module
    def testFilesURL(self):
        '''Testing formed URLs which dont have the filenames passed'''
        resultingURLs = utils.formFileURLs("https://test.gov.si/", [])
        self.assertFalse(resultingURLs)
     #Test resulting file URLs list size
    def testFilesURLSize(self):
        '''Testing formed URLs size'''
        resultingURLs = utils.formFileURLs("https://test.gov.si/", ["filename"])
        self.assertTrue(len(resultingURLs) == 1)
    #Test the resulting file URLs validity
    def testFilesURLValidity(self):
        '''Testing formed if the formed URLs are formed properly'''
        resultingURLs = utils.formFileURLs("https://test.gov.si/", ["testFilename"])
        self.assertTrue("https://test.gov.si/testFilename" == resultingURLs[0])
    #Test DownloadFiles function with no URL passed as argument
    def testDownloadFilesNoURL(self):
        '''Testing if download and storing of files fails if not valid arguments are given'''
        success = utils.downloadFiles([], [])
        self.assertFalse(success)
     #Test DownloadFiles function with no filenames passed as argument
    def testDownloadFilesNoFilenames(self):
        '''Testing formed URL which dont have corresponding filnemanes to store'''
        success = utils.downloadFiles(["https://test.gov.si/testfilename"], [])
        self.assertFalse(success)
        