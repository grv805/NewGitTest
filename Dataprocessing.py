# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:36:37 2018

@author: Manas.Goth
"""

import os
import re
import nltk
import matplotlib.pyplot as plt
#nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd
import unicodedata
import numpy as np
import math
import distance
from collections import Counter



cwd = os.getcwd()
print(cwd)
#Change Directory
# 1 #os.chdir("C:\\Users\\Manas.Goth.GEP\\Projects\\Astellas\\CORPUS\\Corpus1")
os.chdir("C:\\Users\\Manas.Goth.GEP\\Projects\\Census")
#Print all files in CWD
os.listdir('.')
# Reading the data file
#file = 'ASTELLAS_ECC_LFA1_NOV2017_SupplierDetails.xlsx'
inputdata = 'InputData.xlsx'
#SupplierDataFile = 'OnlyUniqueSuppliers.xlsx'
#SupplierDataFile = 'SupplierNames.xlsx'

#Loading the spreadsheet  
datafile = pd.ExcelFile(inputdata)
datafile = datafile.parse('Sheet1')


village = datafile.iloc[:,0].tolist()
booth = datafile.iloc[:,1].tolist()
village = [word for word in village if str(word) != 'nan']
def preprocess(ListOfText):
    temp = []    
    for i in ListOfText:
        name = " ".join(i.split())
        name = re.sub('[.]','',name)
        name =  name.lower()
        temp.append(name)
    return(temp)    
        
village = preprocess(village)
booth = preprocess(booth)

def substitute(booth):
    output= []
    for i in booth:
        words = i.split()
        print(words)
        final = ""
        for j in words :
            if (j == 'khurd'):
                j = 'kh'
            elif(j == 'khur'):
                    j = 'kh'
            elif(j == 'khu'):
                    j = 'kh'        
            elif(j == 'bu'):
                j = 'bk'
            final = final+" "+j        
        output.append(final)         
    return(output)
    
booth1 = substitute(booth)
    
   

     

