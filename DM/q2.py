#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:17:04 2021

@author: pranshu
"""

import os
os.chdir('/home/pranshu/Documents/GitHub/MTech/DM/ass2')
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

total_dict = {}
for f in os.listdir('c17'):
    print(f)
    if f=='DDW-C17-0000.XLSX':
        continue
    df = pd.read_excel('c17/'+f, sheet_name='Sheet1')
    
    df= df.iloc[5:,:]
    df.reset_index(drop=True, inplace=True)
    df.fillna(0, inplace = True)
    state =  df.loc[0, 'Unnamed: 1']
    df['Unnamed: 5'] = df['Unnamed: 5'].astype(int)
    df['Unnamed: 6'] = df['Unnamed: 6'].astype(int)
    
 
    m = df['Unnamed: 5'].sum()
    f = df['Unnamed: 6'].sum()
    
    total_dict[state] = [m,f]
    

df1 = pd.read_excel('DDW-C18-0000.xlsx', sheet_name='Sheet1')
df1= df1.iloc[5:,:]

df1 = df1[(df1['Unnamed: 3']=='Total') & (df1['Unnamed: 4']=='Total')]

df1.columns

df1 = df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX', 'Unnamed: 2',  'Unnamed: 9', 'Unnamed: 10']]

df1.columns = ['State-Code', 'State-Name','3+Males', '3+Females']

df1.reset_index(drop=True, inplace=True)

for i in range(len(df1)):
    if df1.loc[i, 'State-Name'] == 'INDIA':
        continue
    df1.loc[i,'Total_Males'] = total_dict[df1.loc[i, 'State-Name']][0]
    df1.loc[i,'Total_Females'] = total_dict[df1.loc[i, 'State-Name']][1]
#df.drop([0,4], axis = 0, inplace = True)


df1['Male_pct'] = df1['3+Males']*100/df1['Total_Males']
df1['Female_pct'] = df1['3+Females']*100/df1['Total_Females']
df1['abs_diff'] = np.abs(df1['Male_pct']-df1['Female_pct'])
df1.reset_index(drop=True, inplace=True)

for i in range(len(df1)):
    df1['p-value'] = ttest_ind(df1.loc[i,'Male_pct'], df1.loc[i,'Female_pct'], equal_var=False)[1]
