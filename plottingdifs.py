# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:51:33 2019

@author: devyn
"""
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

from IPython.html.widgets import interact, fixed
import ipywidgets as widgets

import io

font_plt = {'family': 'serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 10,
            }
font_plt_ax = {'family': 'serif',
               'color':  'black',
               'weight': 'normal',
               'size': 10,
              }
import sys
import glob #glob is helpful for searching for filenames or directories
sys.path.append('E:\\Differential-Dynamic-Microscopy---Python')
import ddm_clean as ddm #this is the module containing the differential dynamic microscopy code
import scipy #scientific python
import pickle #for saving data

newt = lambda t,s: (1./s)*gamma(1./s)*t
framerate = 18.0
px = 0.194
imDimension = 256

q = np.arange(0,imDimension/2)*2*np.pi*(1./(imDimension*(px))) 
qrange = np.where((q>=0.3)&(q<=3.0)) #this is the q range where the values are typically reasonable!
dts = ddm.genLogDist(1,2998,400)
times = dts/framerate

newds = pickle.load(open('E:\\NewPaper2stuff\\allResults\\NewDifvalues.p','rb')) 
oldds = pickle.load(open('E:\\NewPaper2stuff\\allResults\\OldDifvalues.p','rb'))
nums = pickle.load(open('E:\\NewPaper2stuff\\allResults\\numRois_used.p','rb'))

marks = ['s','o']
col = ['.5','k','r','g','b','c']

ds = newds['New Diffusion Averages']
stdds = newds['New Diffusion Stds']

As = newds['New Alpha Averages']
stdas = newds['New Alpha Stds']


dsO = oldds['New Diffusion Averages']
stddsO = oldds['New Diffusion Stds']

AsO = oldds['New Alpha Averages']
stdasO = oldds['New Alpha Stds']

roisO = nums['Old data ROIs used']

rois = nums['New data ROIs used']

rans = np.arange(len(col))
rans2 = np.array([0.5,1.5,2.5,3.5,4.5,5.5])
t = 1
#fig = plt.figure();

for i in range(1,len(col)):
    ax = plt.gca()

    #ax.errorbar(rans[i],AsO[1,i],yerr=stdasO[1,i],color=col[i],marker=marks[1],capsize=2)
    #ax.errorbar(rans[i],As[1,i],yerr=stdas[1,i],color=col[i],marker=marks[1],capsize=2)
    #ax.semilogy(rans[i],dsO[t,i],mec=col[i],marker=marks[t])
    #ax.errorbar(rans[i],dsO[t,i],yerr=stddsO[t,i],mfc='1.0',mec=col[i],marker=marks[t],ecolor=col[i],capsize=2)
    #ax.errorbar(rans[i],ds[t,i],yerr=stdds[t,i],color=col[i],marker=marks[t],capsize=2)
    ax.bar(rans2[i], rois[t,i], color=col[i], width=0.3, alpha= 0.5)

