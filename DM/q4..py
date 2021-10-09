

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
   # print(f)
    if f=='DDW-C17-0000.XLSX':
        continue
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

df1 = df1[(df1['Unnamed: 3']=='Total') & (df1['Unnamed: 4']=='Total')]

df1.columns

df1 = df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX', 'Unnamed: 2',\
       'Unnamed: 5','Unnamed: 8', ]]

df1.columns = ['State-Code', 'State-Name', '2+','3+']

df1.reset_index(drop=True, inplace=True)
for i in range(len(df1)):
    try:
        df1.loc[i,'Total'] = total_dict[df1.loc[i, 'State-Name']]
    except:
        pass
#df.drop([0,4], axis = 0, inplace = True)


df1['1'] = df1['Total']-df1['2+']
df1['2'] = df1['2+']-df1['3+']


df1['3to2'] = df1['3+']/df1['2']

df1.sort_values('3to2', inplace=True)
df1.reset_index(drop=True, inplace=True)

worst_three = df1.loc[0:2,:]


df1.sort_values('3to2', inplace=True, ascending=False)
df1.reset_index(drop=True, inplace=True)

best_three = df1.loc[0:2,:]

out = best_three.append(worst_three)


out.to_csv('3-to-2-ratio.csv', index = False)


df1.drop('3to2', inplace=True, axis = 1)

df1['2to1'] = df1['2']/df1['1']

df1.sort_values('2to1', inplace=True)
df1.reset_index(drop=True, inplace=True)

worst_three = df1.loc[0:2,:]


df1.sort_values('2to1', inplace=True, ascending=False)
df1.reset_index(drop=True, inplace=True)

best_three = df1.loc[0:2,:]

out = best_three.append(worst_three)


out.to_csv('2-to-1-ratio.csv', index = False)
