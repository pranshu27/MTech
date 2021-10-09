#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:17:04 2021

@author: pranshu
"""

import os
os.chdir('/home/pranshu/Documents/GitHub/MTech/DM/ass2')
import pandas as pd

total_dict = {}
for f in os.listdir('c17'):
    print(f)
# =============================================================================
#     if f=='DDW-C17-0000.XLSX':
#         continue
# =============================================================================
    df = pd.read_excel('c17/'+f, sheet_name='Sheet1')
    df= df.iloc[5:,:]
    df.reset_index(drop=True, inplace=True)
    df.fillna(0, inplace = True)
    state =  df.loc[0, 'Unnamed: 1']
    df['Unnamed: 4'] = df['Unnamed: 4'].astype(int)
    s = df['Unnamed: 4'].sum()
    total_dict[state] = s

df1 = pd.read_excel('DDW-C18-0000.xlsx', sheet_name='Sheet1')
df1= df1.iloc[5:,:]

df1 = df1[(df1['Unnamed: 3']=='Total') & (df1['Unnamed: 4']!='Total')]

df1.columns

df1 = df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX', 'Unnamed: 2','Unnamed: 4','Unnamed: 8', ]]

df1.columns = ['State-Code', 'State-Name','Age-group','3+']

df1.reset_index(drop=True, inplace=True)

for i in range(len(df1)):
    df1.loc[i,'Total'] = total_dict[df1.loc[i, 'State-Name']]

df1['3+_pct'] = df1['3+']*100/df1['Total']

df1.drop(['State-Name', '3+', 'Total'], axis = 1, inplace=True)

#df1 = df1.groupby(['State-Code','Age-group']).agg('max'
df1.reset_index(drop=True, inplace=True)

all_states = set(df1['State-Code'])

out = []
for state in all_states:
    t = {}
    tmp = df1[df1['State-Code']==state]
    tmp.reset_index(drop=True, inplace = True)
    maxx = tmp['3+_pct'].max()
    t['state/ut'] = state
    t['age-group'] = tmp[tmp['3+_pct']==maxx]['Age-group'].values[0]
    t['percentage'] = maxx
    out.append(t)
    
df = pd.DataFrame(out)
df.sort_values('state/ut', inplace=True)
df.to_csv('age-india.csv', index=False)