# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 07:56:34 2019

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

#################################################################################################
#################################################################################################
############# Begin by initializing a pickle file if you want to save the fit data ##############
# allResultsRavsSave = {} 
#################################################################################################
#################################################################################################
########### Define the framerate, pixel size, and ROI dimension #################################

newt = lambda t,s: (1./s)*gamma(1./s)*t
framerate = 18.0
px = 0.194
imDimension = 256

q = np.arange(0,imDimension/2)*2*np.pi*(1./(imDimension*(px))) 
qrange = np.where((q>=0.3)&(q<=3.0)) #this is the q range where the values are typically reasonable!
dts = ddm.genLogDist(1,2998,400)
times = dts/framerate

Condition = ['None', 'Both']
Topology = ['Linear', 'Circular']

Data = pickle.load(open('W:\\Devynn_2018-2019\\Data\\Paper2\\all_allResults\\allResults_None_Both_ravs&fits.p','rb')) 

roi = ['512','768']

videoBL = ['1','2','3','4','5','6','7','8','9','10','11']
videoBC = ['1','2','3','4','5','8']
videoNL = ['1','2','3','4','5','6','7']
videoNC = ['1','2','3','4','5','6','7','8','9']

t = 1
c = 1

marks = ['s','o']
col = ['k','b']

colorscheme1 = ['darkmagenta','limegreen']
colorscheme2 = ['darkviolet','mediumseagreen']
colorscheme3 = ['darkviolet','darkolivegreen']

lincols = ['darkmagenta','limegreen']
rincols = ['0.5','b']
qs = [20]
qcols = ['b','r','c','m','g']

#fig = plt.figure();

video = videoBC
col = colorscheme1

for j in range(len(qs)):
    avgfq = np.zeros((400,2*len(video)))
    k = 0
    for r in range(len(roi)):
        for v in range(len(video)):
            q_index = qs[j]
            ravs = Data['ravs_'+Topology[t]+'_'+Condition[c]+'_'+video[v]+'_'+roi[r]]
            fits = Data['fitparams_'+Topology[t]+'_'+Condition[c]+'_'+video[v]+'_'+roi[r]]
            Amp = fits[:,0]
            Bg = fits[:,2]
            Amp = np.ones(len(ravs[:,q_index]))*Amp[q_index]
            Bg = np.ones(len(ravs[:,q_index]))*Bg[q_index]
            
            fq = (1-(ravs[:,q_index] - Bg)/(Amp))
            w = np.where((fq<-0.1))
            fq[w[0]] = np.nan
            
            avgfq[:,k] = fq
            
            k = k +1
            ax = plt.gca()
            ax.semilogx(times[::2],fq[::2],color='0.5',linestyle = '-',linewidth=3,alpha=0.7)
           
    ax = plt.gca()        
    stderrfqs = (np.nanstd(avgfq,axis=1))/(np.sqrt(len(avgfq[0,:])))        
    avgfqs = np.nanmean(avgfq,axis=1)
    lengs = (2*np.pi)/q[q_index]
    ax.semilogx(times[::4],avgfqs[::4],color=col[c],linestyle = '-',linewidth=3,alpha=1, label=r'length scale of: %.2f $\mu$m' % lengs)
    #ax.errorbar(times[::4],avgfqs[::4],yerr=stderrfqs[::4],color=col[c],marker=marks[t],capsize=2,linestyle='',alpha=1)
    ax.set_xlim(0.05,100)
    ax.set_ylim(-0.05,1)
ax.set_xlabel('Lag Time (s)', fontdict=font_plt_ax)
ax.set_ylabel('f(q,t)', fontdict=font_plt_ax)
#ax.legend()




'''
video = videoBL
for r in range(len(roi)):
    for v in range(len(video)):
        ds = pickle.load(open('W:\\Devynn_2018-2019\\Data\\Paper2\\Both_XL_Networks\\'+Topology[t]+'\\allResults\\allResults_122118_'+video[v]+'.p','rb')) 
        theory = ds['theory_122118_'+video[v]+'_'+roi[r]]
        allResultsRavsSave['theory_'+Topology[t]+'_'+Condition[c]+'_'+video[v]+'_'+roi[r]] = theory
        
#allResultsRavsSave['ravs_'+Topology[t]+'_'+Condition[c]+'_'+video[v]+'_'+roi[r]] = ravs
#allResultsRavsSave['fitparams_'+Topology[t]+'_'+Condition[c]+'_'+video[v]+'_'+roi[r]] = fits
'''