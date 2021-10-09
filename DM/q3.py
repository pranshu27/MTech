#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:17:04 2021

@author: pranshu
"""

import os
os.chdir('/home/pranshu/Documents/GitHub/MTech/DM/ass2')
import pandas as pd
from scipy.stats import ttest_ind

total_dict = {}


census = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx', \
                       sheet_name='Sheet1')
    
    
census = census[(census['Level']=='STATE') & ((census['TRU']=='Rural') |  (census['TRU']=='Urban'))]

census = census[['Name', 'TRU', 'TOT_P']]

census.reset_index(inplace=True, drop = True)

    

df1 = pd.read_excel('DDW-C18-0000.xlsx', sheet_name='Sheet1')
df1= df1.iloc[5:,:]

df1 = df1[((df1['Unnamed: 3']=='Rural') | (df1['Unnamed: 3']=='Urban')) & (df1['Unnamed: 4']=='Total')]

df1.columns

df1 = df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX', 'Unnamed: 2',  'Unnamed: 3','Unnamed: 8']]

df1.columns = ['State-Code', 'State-Name','Area','3+']

df1.reset_index(drop=True, inplace=True)




for i in range(len(df1)):
    try:
        df1.loc[i,'Total'] = census[(census['Name']==df1.loc[i,'State-Name']) & (census['TRU']==df1.loc[i,'Area'])]['TOT_P'].values[0]

    #df1.loc[i,'Total_Females'] = census[census.loc[i, 'State-Name']][1]
#df.drop([0,4], axis = 0, inplace = True)
    except:
        pass
    
out = []
all_states = set(df1['State-Name'])

for state in all_states:
    tmp_df = df1[df1['State-Name']==state]
    tmp_df.reset_index(drop=True, inplace=True)

    tmp = {}
    for i in range(len(tmp_df)):
        
        tmp['State-Code'] = tmp_df.loc[i, 'State-Code']
        tmp['State-Name'] = tmp_df.loc[i, 'State-Name']
        if tmp_df.loc[i, 'Area']=='Rural':
     
            tmp['Rural_pct'] = tmp_df.loc[i, '3+']*100/ tmp_df.loc[i, 'Total']
        else:
            tmp['Urban_pct'] = tmp_df.loc[i, '3+']*100/ tmp_df.loc[i, 'Total']
    out.append(tmp)

df1 = pd.DataFrame(out)

df1 = df1[df1['State-Code']!='00']



for i in range(len(df1)):
    df1['p-value'] = ttest_ind(df1.loc[i,'Rural_pct'], df1.loc[i,'Urban_pct'], equal_var=False)[1]