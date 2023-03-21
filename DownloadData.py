# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 20:16:53 2023

@author: dalib
"""

from utils import utils

#This is the root URL from which the data will be downloaded
rootURL = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/"


#Here type the name of the files that you want to download on the given rootURL
files = ["observation_CELJE_history.html",
         "observation_CERKLJE_LETAL-SCE_history.html",
         "observation_CRNOMELJ_history.html",
         "observation_KATARINA_history.html",
         "observation_KOCEVJE_history.html",
         "observation_KREDA-ICA_history.html",
         "observation_LESCE_history.html",
         "observation_LISCA_history.html",
         "observation_LJUBL-ANA_BEZIGRAD_history.html",
         "observation_LJUBL-ANA_BRNIK_history.html",
         "observation_MARIBOR_SLIVNICA_history.html",
         "observation_MURSK-SOB_history.html",
         "observation_NOVA-GOR_history.html",
         "observation_NOVO-MES_history.html",
         "observation_PORTOROZ_SECOVLJE_history.html",
         "observation_POSTOJNA_history.html",
         "observation_RATECE_history.html",
         "observation_SLOVE-GRA_history.html",
         "observation_VOGEL_history.html",
         "observation_VOJSKO_history.html"]
     
#Form file URLs
fileURLs = utils.formFileURLs(rootURL, files)
#Download file from formed URLs
success = utils.downloadFiles(fileURLs, files)

if success:
    print("\n Succesfully downloaded and stored data from given URLs")
else:
    print("\n Download failed!")
