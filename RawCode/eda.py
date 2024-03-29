
"""

@author: Krishna
EXPLORATORY DATA ANALYSIS ---- HAVING FUNN WITH PYTHON
"""
import random 
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
import urllib, urllib2, httplib
import numpy as np



glass= pd.read_csv('\glass.csv',header=None,prefix='V')
glass.columns=['Id','RI','Na','Mg','Al','Si','K','Ca','Ba','Fe','Type']
ncol1=len (glass.columns)
glassNormalized=glass.iloc[:,1:ncol1]

ncol2=len(glassNormalized.columns)
summ=glassNormalized.describe()


mean=summ[1:2][:].values
std=summ[2:3][:].values

array2 = np.zeros((ncol1,ncol2))

array1=np.array(glassNormalized)


for i in range(ncol2):
    for j in range (ncol1):
        array2[j][i]=((array1[j][i]-mean[0][i])/std[0][i])
#make it a dataFrame for usability        
glassNormalized2=DataFrame(array2)
#rename the header of the columns
glassNormalized2.columns=['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe','Type']
#plot the parallel plot to check for direct classification 
for i in range(ncol1):
    data=DataFrame(glassNormalized2.iloc[i,1:(ncol2-1)])
    label=glassNormalized2.iloc[i,(ncol2-1)]/7
    data.plot(color=plot.cm.RdYlBu(label),alpha=0.5)

#plot a Heat map to view the  corelations between features(attributes)
mat=DataFrame(glass.corr())
plot.pcolor(mat)
plot.show()

    

