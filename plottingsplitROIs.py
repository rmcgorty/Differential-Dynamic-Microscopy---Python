# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:10:46 2019

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

px = 0.194
imDimension = 256
q = np.arange(0,imDimension/2)*2*np.pi*(1./(imDimension*px))

directanddata = 'E:\\NewPaper2stuff\\allResults_fromharddrive\\053119_8am_fixed_splitROI_difs.p'
fZ = pickle.load(open(directanddata,'rb'))

Topology = ['Linear', 'Circular']
Condition = ['None', 'Microtubules', 'Actin', 'Both', 'Co']
number = '2'
roi = ['0','256','512','768','1024']#
marks = ['s','o']
col = ['k','r','g','b','c']

t = 1
c = 0
#r = 0

video = fZ[Topology[t]+' '+Condition[c]+' '+number]

xticks_pos = [0,256,512,768,1024]#
xticks_label = ['0','256','512','768','1024']#


cons = np.array([0,256,512,768,1024])#256,
fig = plt.figure();
for r in range(len(roi)): 
    region = video[roi[r]]
    ax = plt.gca()
    alphas = region['alpha values']
    transport = region['diffusion values']
    stdas = np.nanstd(alphas)
    avgas = np.nanmean(alphas)
    avgts = np.nanmean(transport)
    stdts = np.nanstd(transport)
    N = len(alphas)
    stdtsEr = stdts/(np.sqrt(N))
    stdasEr = stdas/(np.sqrt(N))
    ax.errorbar(cons[r],avgts,yerr=stdtsEr,color=col[c],marker=marks[t],capsize=2)
    #ax = plt.gca()
    #ax.errorbar(cons[r],avgas,yerr=stdas,color=col[r],marker=marks[t],capsize=2)
    #ax.set_ylim(0.0002,0.31)
    ax.set_xlabel(r" ROIs ", fontdict=font_plt_ax)
    ax.set_ylabel(r' Transport Coefficients', fontdict=font_plt_ax)
ax.set_title(Topology[t]+' '+Condition[c], fontdict=font_plt_ax)
plt.xticks(xticks_pos, xticks_label)
plt.savefig('E:\\NewPaper2stuff\\allResults_fromharddrive\\ROIs_inconditions\\stderror_forerrorbars\\transportCoefs\\'+Topology[t]+'_'+Condition[c]+'_ROIs_'+number+'data.png')
#plt.yticks(yticks_pos, yticks_label)
