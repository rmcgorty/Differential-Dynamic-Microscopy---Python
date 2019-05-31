# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:01:50 2019

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
sys.path.append('W:\\Devynn_Summer2018\\Code\\Differential-Dynamic-Microscopy---Python')
import ddm_clean as ddm #this is the module containing the differential dynamic microscopy code
import scipy #scientific python
import pickle #for saving data
sys.path.append('W:\\Code\\PythonCode\\')
import niceplot

framerate = 18.0
px = 0.194
imDimension = 256
q = np.arange(0,imDimension/2)*2*np.pi*(1./(imDimension*(px))) 
qrange = np.where((q>=0.3)&(q<=6.0)) #this is the q range where the values are typically reasonable!
dts = ddm.genLogDist(1,2998,400)
times = dts/framerate

Files = pickle.load(open('W:\\Devynn_2018-2019\\Data\\Paper2\\CO_XL_Networks\\Linear\\allResults\\allResults_Linear_CoXL_041619.p','rb'))

video = ['1','2','3','4','5','6','7','8']
roi = ['0','256','512','768','1024']

col = ['.5','k','r','g','b','c']

fig = plt.figure();
for i in range(len(video)):
    for j in range(len(roi)):
        ax = plt.gca()
        #tau = Files['NAN_taus_'+video[i]+'_'+roi[j]]
        fitparams = Files['fitparams_'+video[i]+'_'+roi[j]]
        tau = fitparams[:,1]
        ax.loglog(q[qrange],tau[qrange],color=col[5],marker = 's', mec = None, markersize= 2.5, linestyle = '', alpha=1)
        
diffusion_coeff = .05 # you can change this to get a rough estimate of the diffusion coef
power = 3.0 
ax.plot(q[qrange], (1./diffusion_coeff) * 1./(q[qrange]**power), '--k', label="Diffusive")
ax.set_xlabel(r'Spatial Frequencies')
ax.set_ylabel(r'Taus')