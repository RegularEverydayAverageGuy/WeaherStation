# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 20:16:53 2023

@author: dalib
"""

from utils import utils

#This is the root URL from which the data will be downloaded
rootURL = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/"

#Here type the name of the files that you want to download on the given rootURL
files = ["observation_CELJE_latest.xml",
         "observation_CERKLJE_LETAL-SCE_latest.xml",
         "observation_CRNOMELJ_latest.xml",
         "observation_KATARINA_latest.xml",
         "observation_KOCEVJE_latest.xml",
         "observation_KREDA-ICA_latest.xml",
         "observation_LESCE_latest.xml",
         "observation_LISCA_latest.xml",
         "observation_LJUBL-ANA_BEZIGRAD_latest.xml",
         "observation_LJUBL-ANA_BRNIK_latest.xml",
         "observation_MARIBOR_SLIVNICA_latest.xml",
         "observation_MURSK-SOB_latest.xml",
         "observation_NOVA-GOR_latest.xml",
         "observation_NOVO-MES_latest.xml",
         "observation_PORTOROZ_SECOVLJE_latest.xml",
         "observation_POSTOJNA_latest.xml",
         "observation_RATECE_latest.xml",
         "observation_SLOVE-GRA_latest.xml",
         "observation_VOGEL_latest.xml",
         "observation_VOJSKO_latest.xml"]
         
#Form file URLs
fileURLs = utils.FormFileURLs(rootURL, files)
#Download file from formed URLs
success = utils.DownloadFiles(fileURLs, files)

if(success):
    print("\nData successfully downloaded to Data directory.")
else:
    print("\nNo data was downoaded to Data directory.")