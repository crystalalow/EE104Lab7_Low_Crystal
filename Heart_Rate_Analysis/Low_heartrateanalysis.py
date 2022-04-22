# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:14:03 2022

@author: Crystal
"""

import heartpy as hp
import matplotlib.pyplot as plt

#sampling rate changed accordingly 
sample_rate = 250

#read the dataset collected 
data=hp.get_data('hb.csv')
plt.figure(figsize=(12,4))
plt.plot(data)
plt.show

#runs the analysis 
wd, m = hp.process(data, sample_rate)
#visualize in plot of custom size 
plt.figure(figsize=(3,4)) #3,4
hp.plotter(wd, m)
#display computed measures 
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))