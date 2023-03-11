# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:10:12 2023

@author: dalib
"""

import unittest
from utils import utils

#Tests the utils module
class TestUtils(unittest.TestCase):
    
    #Tests the FormFilesURLs from utils module
    def test_FilesURL(self):
        resultingURLs = utils.FormFileURLs("https://test.gov.si/", [])
        self.assertFalse(resultingURLs)
     #Test resulting file URLs list size
    def test_FilesURLSize(self):
        resultingURLs = utils.FormFileURLs("https://test.gov.si/", ["filename"])
        self.assertTrue(len(resultingURLs) == 1)
    #Test the resulting file URLs validity
    def test_FilesURLValidity(self):
        resultingURLs = utils.FormFileURLs("https://test.gov.si/", ["testFilename"])
        self.assertTrue("https://test.gov.si/testFilename" == resultingURLs[0])
    #Test DownloadFiles function with no URL passed as argument
    def test_DownloadFilesNoURL(self):
        success = utils.DownloadFiles([], [])
        self.assertFalse(success)
     #Test DownloadFiles function with no filenames passed as argument
    def test_DownloadFilesNoFilenames(self):
        success = utils.DownloadFiles(["https://test.gov.si/testfilename"], [])
        self.assertFalse(success)