# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:23:06 2023

@author: dalib
"""
import os
import requests
from  tqdm import tqdm

#Forms complete file URLs from rootURL and filenames
def formFileURLs(rootURL, files):
    '''Function form file URLs'''
    fileURLs = []
    for i in tqdm(range(0, len(files)), desc = "Forming URLs"):
        fileURLs.append(rootURL + files[i])
    return fileURLs

#Downloads files from fileURLs list and stores in correspodning file named in fileNames list
def downloadFiles(fileURLs, fileNames):
    '''Function downloading and storing files'''
    #both list have to have same size to properly store data
    if(len(fileNames) != len(fileURLs) or fileURLs == []):
        return False
    #Download and store the data
    for i in tqdm(range(0, len(fileURLs)), desc = "Downloading and storig data"):
        response = requests.get(fileURLs[i], timeout=5)#We wait for max 5s for the responseunites
        filename = "./Data/" + fileNames[i]
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as file:
            file.write(response.content)
    return True
