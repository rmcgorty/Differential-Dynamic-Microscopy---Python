# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:50:48 2019

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

newdatas = pickle.load(open('E:\\NewPaper2stuff\\allResults\\diffusion_newdata_050819.p','rb')) 
olddatas = pickle.load(open('E:\\NewPaper2stuff\\allResults\\AllDiffusionData.p','rb'))

Condition = ['Buffer', 'None', 'Microtubules', 'Actin', 'Both','CoXL']
#Condition = ['Buffer', 'Entangled', 'XLMTs', 'XLACTs', 'BothXL','CoXL']
Topology = ['Linear', 'Circular']

marks = ['s','o']
col = ['.5','k','r','g','b','c']

t = 1
c = 5

difs = newdatas['New '+ Topology[t]+' '+Condition[c]]['diffusion values']  #['difs']   #
alphas = newdatas['New '+Topology[t]+' '+Condition[c]]['alpha values'] #['alpha']          #

averagedif = np.nanmean(difs)
averagealph = np.nanmean(alphas)
stddifs = np.nanstd(difs)
stdalphs = np.nanstd(alphas)

#numRois = np.zeros((len(Topology),len(Condition)))
numRois[t,c] = len(difs)

'''
difvalues = np.zeros((len(Topology),len(Condition)))
alphavalues = np.zeros((len(Topology),len(Condition)))
difstds = np.zeros((len(Topology),len(Condition)))
alphsstds = np.zeros((len(Topology),len(Condition)))


difvalues[t,c] = averagedif
alphavalues[t,c] = averagealph

difstds[t,c] = stddifs
alphsstds[t,c] = stdalphs

'''



