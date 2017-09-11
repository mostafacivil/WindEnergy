# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:24:29 2017

@author: momen
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

d=np.zeros([135,3])
d[0:5,0]=0.85
d[5:10,0]=0.9
cc2 = np.arange(1,0,-0.2)
d[0:5,1]=0.85
d[5:10,1]=0.9
d[0:5,2]=0.85
d[5:10,2]=cc2*0.5+0.5
d[10:110,0]=1
cc2 = np.arange(1,0,-0.01)
d[10:110,1]=cc2*np.sqrt(cc2)
d[10:110,2]=0
cc2 = np.arange(1,0,-0.04)
d[110:135,1]=0
d[110:135,2]=0
d[110:135,0]=cc2
cmap2 = mpl.colors.ListedColormap(d)

fig=plt.figure(num=None, figsize=(8, 5), dpi=500, facecolor='w', edgecolor='k')
map = Basemap(projection='cyl', llcrnrlat=20, urcrnrlat=55.0,llcrnrlon=-140,
          urcrnrlon=-50, resolution='c', lon_0=0)
map.drawcoastlines(linewidth=0.4)
map.scatter(Lon_tur, Lat_tur, marker='.',c=Cap,cmap=cmap2,s=3)
plt.clim(-10,300)
"map.pcolormesh(xx,-yy,Zm2,shading='flat',cmap=plt.cm.gray,latlon=True)"
"plt.clim(-1,0)"
map.drawcountries(linewidth=0.5)
plt.colorbar()
plt.title('Wind Farm Locations and Total Capicity (MW) in the US')

plt.savefig('C:\\Users\\momen\\Dropbox\\Papers\\Wind Power\\WindFarm_Loc.png', format='png', dpi=500)
plt.savefig('C:\\Users\\momen\\Dropbox\\Papers\\Wind Power\\WindFarm_Loc.tif', format='tif', dpi=500)
