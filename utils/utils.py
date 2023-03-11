# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:23:06 2023

@author: dalib
"""
import os
import requests
from  tqdm import tqdm

#Forms complete file URLs from rootURL and filenames
def FormFileURLs(rootURL, files):
    fileURLs = []
    for i in tqdm(range(0, len(files)), desc = "Forming URLs"):
        fileURLs.append(rootURL + files[i])
        
    return fileURLs


#Downloads files from fileURLs list and stores in correspodning file named in fileNames list
def DownloadFiles(fileURLs, fileNames):
    #both list have to have same size to properly store data
    if(len(fileNames) != len(fileURLs) or fileURLs == []):
        return False
    
    #Download and store the data
    for i in tqdm(range(0, len(fileURLs)), desc = "Downloading and storig data"):
        response = requests.get(fileURLs[i])
        filename = "./Data/" + fileNames[i]
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        open(filename, "wb").write(response.content)
    
    return True