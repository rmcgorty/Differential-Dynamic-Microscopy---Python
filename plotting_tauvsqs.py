# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:11:57 2019

@author: Physics
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
sys.path.append('Z:\\Devynn_Summer2018\\Code\\Differential-Dynamic-Microscopy---Python')
import ddm_clean as ddm #this is the module containing the differential dynamic microscopy code
import scipy #scientific python
import pickle #for saving data

#E:\SoftMatterStuff\ddm
#################################################################################################
#################################################################################################
############# Begin by initializing a pickle file if you want to save the fit data ##############
# allResults = {} 
#################################################################################################
#################################################################################################
########### Define the framerate, pixel size, and ROI dimension #################################

newt = lambda t,s: (1./s)*gamma(1./s)*t
framerate = 18.0
px = 0.194
imDimension = 256
q = np.arange(0,imDimension/2)*2*np.pi*(1./(imDimension*(px))) 
#################################################################################################
#################################################################################################
########### Load in the data directory and the data file that you want to analyze ###############
condition = ['Buffer', 'Entangled_Networks', 'XL_MTs_entangledACTs','XL_ACTs_entangledMTs','Both_XL_Networks','CO_XL_Networks']
a = 4
data_dirL = "Z:\\Devynn_2018-2019\\Data\\Paper2\\all_allResults\\extraallresults\\"
data_dirC = "Z:\\Devynn_2018-2019\\Data\\Paper2\\all_allResults\\extraallresults\\"
dateL = '122118'
dateC = '012219'
data_fileL = 'allResults_'+condition[a]+'_Linear_allnanTaus_'+dateL+'.p'
data_fileC = 'allResults_'+condition[a]+'_Circular_allnanTaus_'+dateC+'_2.p'
useL = pickle.load(open(data_dirL+data_fileL,'rb'))
useC = pickle.load(open(data_dirC+data_fileC,'rb'))
roi = ['0','256','512','768','1024']
video = ['1', '2','3','4','5','6','7','8','9','10','11']
R = 4
V = 5
d = 28

col = ['0.5','k', 'r','g', 'b','c']
c = ['k', 'r','g', 'b','c']
#colC = ['kv','bv', 'gv', 'rv', 'cv', 'mv']

fig = plt.figure();
#figsize=(xsize,ysize)

new_xtick_pos = np.array([.5, 1,3])
new_xtick_labels = ['0.5', '1.0','3.0']
new_ytick_positions = np.array([ .15, 1, 10,100])
new_ytick_labels = [ '0.15',  '1.0','10','100'] 

#tauS = np.zeros([len(video)*len(roi),43])
#fig = plt.figure();
#for i in range(len(roi)):
ax = plt.gca()
taus = useC['NAN_taus_'+condition[a]+'_'+video[V]+'_'+roi[R]]
qs = useC['NAN_qs_'+condition[a]+'_'+video[V]+'_'+roi[R]]
#tauS[d,:] = taus
ax.loglog(qs,taus,color=col[a],marker = 's', mec = None, markersize= 2.5, linestyle = '', alpha=1)
ax.set_ylabel(r" Tau (s) ", fontdict=font_plt_ax)
ax.set_xlabel(r' Spatial Frequency q ($\mu m^{-1}$)', fontdict=font_plt_ax)
plt.xticks(new_xtick_pos, new_xtick_labels)
plt.yticks(new_ytick_positions, new_ytick_labels)
ax.set_ylim(.02,150)
ax.set_xlim(.3,3.0)

#ax.legend()
#plt.xticks(new_xtick_pos, new_xtick_labels)
#plt.yticks(new_ytick_positions, new_ytick_labels)

#useC = pickle.load(open(data_dirC+data_fileC,'rb'))
'''
#tauSC = np.zeros([len(video)*len(roi),43])
k = 0
for j in range(len(video)):
    for i in range(len(roi)):
        taus = useL['NAN_taus_'+condition[a]+'_'+video[j]+'_'+roi[i]]
        qs = useL['NAN_qs_'+condition[a]+'_'+video[j]+'_'+roi[i]]
        #tausC = useC['NAN_taus_'+condition[a]+'_'+video[j]+'_'+roi[i]]
        #qsC = useC['NAN_qs_'+condition[a]+'_'+video[j]+'_'+roi[i]]
        #ax.loglog(qs,taus,col[3], mec = None, markersize= 2.5, linestyle = '', alpha=1)
        #ax.loglog(qsC,tausC,colC[3], mec = None, markersize= 2.5, linestyle = '', alpha=1)
        tauS[k,:] = taus
        #tauSC[k,:] = tausC
        k = k + 1
        
#avgtaus = np.nanmean(tauS, axis=0)  
#avgtausC = np.nanmean(tauSC, axis=0)  
#allAvLin['avgTaus_Entangled_linear'] = avgtaus
#allAvLin['avgTaus_xlmts_circular'] = avgtausC

ax.loglog(qs,avgtausC,colC[a],mec = None, markersize= 4, linestyle = '', alpha=1)  
ax.loglog(qs,avgtaus,col[a],mec = None, markersize= 4, linestyle = '', alpha=1)     
ax.set_ylabel(r" Tau (s) ", fontdict=font_plt_ax)
ax.set_xlabel(r' Spatial Frequency q ($\mu m^{-1}$)', fontdict=font_plt_ax)
plt.xticks(new_xtick_pos, new_xtick_labels)
plt.yticks(new_ytick_positions, new_ytick_labels)
ax.set_ylim(.02,150)
ax.set_xlim(.3,3.0)
'''

'''
data_file = 'allResults_'+dateL+'_'+video[j]+'.p'
        use = pickle.load(open(data_dir+data_file,'rb'))
        fitparamsA = use['fitparams_'+dateL+'_'+video[j]+'_'+roi[i]]
        ax.loglog(q[:-1], ddm.newt(fitparamsA[:,1],fitparamsA[:,3]),col[0],mec = None, markersize= 3, linestyle = '', alpha=1) 
        fitparamsA = useC['fitparams_'+dateC+'_'+video[j]+'_'+roi[i]]
        ax.loglog(q[:-1], ddm.newt(fitparamsA[:,1],fitparamsA[:,3]),colC[3],mec = None, markersize= 3, linestyle = '', alpha=1)#
        '''

'''
diffusion_coeff = 0.15 # you can change this to get a rough estimate of the diffusion coef
power = 2.5 
ax.plot(q[2:-2], (1./diffusion_coeff) * 1./(q[2:-2]**power), '-c', label="D = 0.55+/-.05")
xsize = 8
ysize = 8
fig = plt.figure(figsize=(xsize,ysize));
#figsize=(xsize,ysize)
ax = plt.gca()
col = ['ko','bo','ro', 'co','mo','go']
for i in range(len(condition)):
    
    diffusion_coeff = [.49,.17,.04,.03,.025,0.15] # you can change this to get a rough estimate of the diffusion coef
    power = [2.0,2.5,3.0,3.0,3.0,2.5] 
    ax.loglog(q[2:-2], (1./diffusion_coeff[i]) * 1./(q[2:-2]**power[i]), col[i],label=condition[i]+r' K $\approx$ %.2f' %diffusion_coeff[i])
    #ax.loglog(q[10:-45], (1./1.0) * 1./(q[10:-45]**power[i]), 'k-',label=r' $\alpha \approx$ %.2f' %power[i])
    ax.set_ylabel(r" Tau (s) ", fontdict=font_plt_ax)
    ax.set_xlabel(r' Spatial Frequency q ($\mu m^{-1}$)', fontdict=font_plt_ax)
    ax.legend()
    plt.xticks(new_xtick_pos, new_xtick_labels)
    plt.yticks(new_ytick_positions, new_ytick_labels)
       
'''
