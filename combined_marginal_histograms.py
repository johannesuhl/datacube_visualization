# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:49:50 2020

@author: Johannes H. Uhl, Department of Geography, University of Colorado Boulder
"""

import os
from osgeo import gdal
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx 
import matplotlib
matplotlib.rcParams['font.sans-serif'] = "Arial"
matplotlib.rcParams['font.family'] = "sans-serif"
matplotlib.rcParams['font.size'] = 10
#plt.style.use('dark_background')
plt.style.use('default')

### specify input datacube (as geoTiff) and colormap for visualization
#########################
img = './HyRANK_satellite/TrainingSet/Dioni.tif'
#img = './HyRANK_satellite/TrainingSet/Loukia.tif'
#img = './HyRANK_satellite/ValidationSet/Erato.tif'
#img = './HyRANK_satellite/ValidationSet/Kirki.tif'
#img = './HyRANK_satellite/ValidationSet/Nefeli.tif'
#img = './Hyperspectral_Project/dc.tif'
colormap='prism'
#########################

### note that gdal.Open().ReadAsArray() will return an array of dimension
### (bands,rows,columns). North-south denominates sums along the columns, east-west along the rows.

### read input
rastarr = gdal.Open(img).ReadAsArray()
bands = np.arange(rastarr.shape[0])

### compute cross sums
marg_sums_ns=[]
marg_sums_ew=[]
for band in bands:
    marg_sums_ns.append(np.sum(rastarr[band,:,:],axis=0))
    marg_sums_ew.append(np.sum(rastarr[band,:,:],axis=1))

### visulalize
cmap=plt.get_cmap(colormap)
cNorm  = colors.Normalize(vmin=0, vmax=len(bands)-1)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cmap) 

figNS=plt.subplots()
for band in bands:    
    margsumNS = marg_sums_ns[band]
    xvect_NS = np.arange(0,margsumNS.shape[0])

    if band==0:
        plt.fill_between(xvect_NS,margsumNS,color=scalarMap.to_rgba(band),lw=0)
    else:
        plt.fill_between(xvect_NS,xvect_NSprev,margsumNS,color=scalarMap.to_rgba(band),lw=0)    
    xvect_NSprev = margsumNS.copy()
axNS = plt.gca()
axNS.spines['bottom'].set_color('white')
axNS.spines['top'].set_color('white')
axNS.spines['left'].set_color('white')
axNS.spines['right'].set_color('white')
axNS.axes.xaxis.set_visible(False)
axNS.axes.yaxis.set_visible(False)
plt.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fileext=os.path.splitext(img)[-1]
plt.savefig(img.replace(fileext,'_marghist_stacked_north_south'+fileext),dpi=600)
    


figEW=plt.subplots()
for band in bands:    
    margsumEW = marg_sums_ew[band]
    xvect_EW = np.arange(0,margsumEW.shape[0])
    if band==0:
        plt.fill_between(xvect_EW,margsumEW,color=scalarMap.to_rgba(band),lw=0)
    else:
        plt.fill_between(xvect_EW,xvect_EWprev,margsumEW,color=scalarMap.to_rgba(band),lw=0)    
    xvect_EWprev = margsumEW.copy()
axEW = plt.gca()    
axEW.spines['bottom'].set_color('white')
axEW.spines['top'].set_color('white')
axEW.spines['left'].set_color('white')
axEW.spines['right'].set_color('white')
axEW.axes.xaxis.set_visible(False)
axEW.axes.yaxis.set_visible(False)
plt.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
#plt.tight_layout()
plt.savefig(img.replace(fileext,'_marghist_stacked_east_west'+fileext),dpi=600)

#### greyscale plot of the input datacube

figIMG=plt.subplots()
in_img_grey=np.mean(rastarr,axis=0)
plt.imshow(in_img_grey,cmap='Greys')
axIMG = plt.gca()
axIMG.spines['bottom'].set_color('white')
axIMG.spines['top'].set_color('white')
axIMG.spines['left'].set_color('white')
axIMG.spines['right'].set_color('white')
axIMG.axes.xaxis.set_visible(False)
axIMG.axes.yaxis.set_visible(False)
plt.savefig(img.replace(fileext,'_grey'+fileext),dpi=600)


##### marginal histograms for each band, stacked to a 2d heatmap:

fig=plt.subplots()
margsumNS_arr=[]
for i in range(len(marg_sums_ns)):
    margsumNS_arr.append(list(marg_sums_ns[i]))
margsumNS_arr=np.array(margsumNS_arr)    
plt.imshow(margsumNS_arr,cmap='gist_ncar')
ax = plt.gca()
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fileext=os.path.splitext(img)[-1]
plt.savefig(img.replace(fileext,'_marghist_2d_north_south'+fileext),dpi=600)
    

fig=plt.subplots()
margsumEW_arr=[]
for i in range(len(marg_sums_ew)):
    margsumEW_arr.append(list(marg_sums_ew[i]))
margsumEW_arr=np.array(margsumEW_arr)    
plt.imshow(margsumEW_arr,cmap='gist_ncar')
ax = plt.gca()
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fileext=os.path.splitext(img)[-1]
plt.savefig(img.replace(fileext,'_marghist_2d_east_west'+fileext),dpi=600)