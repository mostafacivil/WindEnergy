# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:46:48 2017

@author: momen
"""

#-------- Loading Data:
    
import csv
samp='C:\\Users\\momen\\Dropbox\\Papers\\Wind Power\WindPowerLocations.csv'
with open(samp) as f:
    reader = csv.reader(f)
    list1=list(reader)
    
list1=np.asanyarray(list1)

m=np.shape(list1)
 
Lat_tur=[]
Lon_tur=[]
Cap=[]
for i in range(1, m[0]):
    if float(list1[i,19])>-135:
        Lat_tur.append(float(list1[i,18]))
        Lon_tur.append(float(list1[i,19]))
        Cap.append(float(list1[i,12]))
     
     
