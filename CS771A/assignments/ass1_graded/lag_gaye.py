# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:47:21 2021

@author: sethi
"""

import numpy as np
from collections import Counter

def entropy(y): # y is a vec containing all class labels
# p(x)=#x/next     number of occurances
    hist = np.bincount(y)  # for counting occurances of all class lables
    ps = hist/len(y)
    
    return -np.sum([p * np.log2(p) for p in ps if p>0])  

class node:     # store info of nodes
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        # leaf will only have value parameter
        
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf(self):
        return self.value is not None     #if self has a value then its a leaf node
    
class dt:
    def __init__(self, min_split=2, max_depth = 100, n_feats=None):   #stopping criteria is min_split ie to further split min data will be 2 data points
    #max_depth = no. of features krr lena
      
       self.min_split = min_split
       self.n_feats = n_feats 
       self.max_depth = max_depth
       self.root = None   #defines where to start traversing the tree from
   
    def fit(self, X, y):    #here we want to grow our tree so it get training data
    
        # this is a safty check st n_feats!> no. of features  
        self.n_feats = X.shape[1] if not self.n_feats else min(self.n_feats,X.shape[1])   #x.shape is a np array and [1]=number of features
        self.root = self.grow(X,y)
      
    def grow(self, X, y, depth=0):    #traverse tree, it gets test data
        n_sample, n_feature=X.shape 
        n_labels = len(np.unique(y))  
        
        #apply stopping criteria. we check for max depth, min samples and no more class
        if depth>=self.max_depth or n_labels == 1 or n_samples < self.min_split:
            # this means we are at leaf  node
            leaf = self.most_common_label(y)
            return node(value=leaf)
         
        #stopping criteria ye random forest ka he
        feat_idxs = np.random.choice(n_feature, self.n_feats, replace=False)
        
        #greedy search
        best_f, best_th=self._best_criteria(X,y,feat_idxs)
        left_idx, right_idx = self._split(X[:,best_f, best_th])
        left_q = self.grow(X[left_idx, :], y[left_idx], depth+1)        #left child
        right_q = self.grow(X[right_idx, :], y[right_idx], depth+1)
        return node(best_f, best_th, left_q, right_q)  # return new node in med
        
    def _best_criteria(self,X,y,feat_idxs):
    # here er are calculating information gain
        best_g = -1
        split_idx, split_th=None, None
        for idx in feat_idxs:
            X_col = X[:, idx]
            thresholds = np.unique(X_col)
                 
            for th in thresholds:
                gain = self._info_gain(y, X_col, th)
                    
                if gain>best_g:
                    best_g = gain
                    split_idx = idx
                    split_th = th
                    
        return  split_idx, split_th
            
    def _info_gain(self, y,X_col, split_th):
        #parent entropy
        parent_e = entropy(y)
        
        #generate split
        left_idx, right_idx = self._split(X_col, split_th)
        
        if len(left_idx) == 0 or len(right_idx) == 0:
            return 0        #ig is 0
        
        #weighted avg child E
        n = len(y) #no. of sample
        n_l,n_r = len(left_idx), len(right_idx)
        e_l,e_r = entropy(y[left_idx]), entropy(y[right_idx])
        child_entropy = (n_l/n)*e_l + (n_r/n)*e_r
        
        #return ig
        ig = parent_e - child_entropy
        return ig   
        
        
    def _split(self, X_col, split_th):
        left_idx = np.argwhere(X_col <= split_th).flatten()   # returns an array where all these cond are true for all val in our X_col. we want to flatten this array coz we want 1d array
        right_idx = np.argwhere(X_col > split_th).flatten()
        return left_idx, right_idx
        
    def most_common_label(self,y):
        counter=Counter(y)      #counts no. of occurances for y (similar to np.bincount)
        most_common = counter.most_common(1)[0][0]   #most_common(1) returns list of most common label. [0] specifies 1st element. it will store val, occurance so we only need val thats why [0]
        return most_common
    
    def predict(self, X):                   # traverse the tree
        return np.array([self,_traverse(x, self.root) for x in X])
    
    def _traverse(self, x, nodee):
        if nodee.is_leaf():
            return nodee.value 
        
        if x[nodee.feature]<= nodee.th:
            return self._traverse(x, nodee.left)
        
        return self._traverse(x, nodee.right)
          
       
       