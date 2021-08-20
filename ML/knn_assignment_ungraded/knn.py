#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:45:54 2021

@author: joker
"""
'''
import os
os.chdir(r"/home/joker/Downloads/Video/SEM1-Downloads/CS771A/demo01")

os.getcwd()
'''

import numpy as np
import numpy.linalg as lin
import time as t

# cs771 will be our course package and will contain several modules
# Right now we have a dummy module, a data generation module and a data plotting module
from cs771 import helloWorld as hW
from cs771 import genSyntheticData as gsd
from cs771 import plotData as pd


d = 2 
n = 30

# Choose points around which positive and negative class points will be sampled
muPos = np.array( [-5,5] )
muNeg = np.array( [5,0] )

# Generate nice spherical data using our data generation module
# Choose a nice radius
r = 5
XPos = gsd.genSphericalData( d, n, muPos, r )
XNeg = gsd.genSphericalData( d, n, muNeg, r )

# Let us plot these points on a plane and see where they landed
# First, obtain a new figure from the plotting module - the two arguments set the size of the figure
fig1 = pd.getFigure( 7, 7 )

# The three commands below are just to give the plot an aesthetic aspect ratio - do not worry about this
ax = fig1.add_axes( [0,0,0.75,0.75] )
ax.set_xlim( [-15, 15] )
ax.set_ylim( [-15, 15] )

# Now, plot the sampled points - you can change the color, marker and size of the markers
pd.plot2D( XPos, fig1, color = 'r', marker = '+' )
pd.plot2D( XNeg, fig1, color = 'g', marker = 'o' )


def knn(x,y):
    out = []
    for p in XPos:
        tmp = {}
        dist = lin.norm( np.array([x,y]) - p, 2)
        tmp['dist'] = dist
        tmp['label'] = "XPos"
        out.append(tmp)
    for n in XNeg:
        tmp = {}
        dist = lin.norm( np.array([x,y]) - n, 2)
        tmp['dist'] = dist
        tmp['label'] = "XNeg"
        out.append(tmp)
       
    out = sorted(out, key=lambda item: item['dist'])[:5]
    
    #print(out)
    count = 0
    for d in out:
        if (d["label"] == "XPos"):
            count = count+1
        else:
            count = count-1
    
    out.clear()
    return count
    
#knn(3,7)


fig2 = pd.getFigure( 7, 7 )

# Use the plotting module to shade the entire 2D space and visualize the decision boundary
tic = t.process_time()
pd.shade2D( knn, fig2, mode = 'point', xlim = 15, ylim = 15 )
toc = t.process_time()

toc-tic

