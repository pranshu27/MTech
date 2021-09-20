#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 06:19:37 2021

@author: pranshu
"""

# =============================================================================
# QUESTION 7
# =============================================================================

# =============================================================================
# DISTRICTWISE
# =============================================================================
import pandas as pd 
dfc = pd.read_csv(r'cowin_vaccine_data_districtwise.csv', low_memory=False)
dfc = dfc.loc[1:, :]
dfc.reset_index(drop=True, inplace=True)

cols = [i for i in range(20)]
tmp = dfc.iloc[:, cols]
    
per1 = pd.date_range(start ='16-01-2021', \
         end ='14-08-2021', freq ='D')
    
rd = [d.strftime('%d/%m/%Y') for d in per1]

out = []

for j in range(len(rd)):
    for i in range(len(dfc)):
        td = {}
        td['State_Code'] = dfc.loc[i, 'State_Code']
        td['District_Key'] = dfc.loc[i, 'District_Key']
        td['Date'] = rd[j]
        td['Covaxin'] = dfc.loc[i,rd[j]+'.8']
        td['Covishield'] = dfc.loc[i,rd[j]+'.9']
        out.append(td)
    

d = pd.DataFrame(out)

d['Covaxin'].fillna(0, inplace=True)
d['Covishield'].fillna(0, inplace=True)    
d['Covaxin'] = d['Covaxin'].astype(int)
d['Covishield'] = d['Covishield'].astype(int)  


# =============================================================================
# d.sort_values(['Date','State_Code','District_Key'], inplace = True)
# 
# 
# 
# d = d.groupby(['State_Code','District_Key'])
# 
# later = pd.DataFrame()
# for district, district_df in d:
# 
#     temp = district_df.shift(1)
#     temp.fillna(0,inplace=True)
#     district_df['Covaxin'] = district_df['Covaxin'] - temp['Covaxin']
#     district_df['Covishield'] = district_df['Covishield'] - temp['Covishield']
#     district_df.set_index('Date',inplace=True)
# #     print(district_df)
#     later = later.append(district_df)
# 
# 
# 
# 
# d = later.copy()
# 
# d['Date'] = d.index
# 
# 
# d['Date'] = pd.to_datetime(d['Date'])
# =============================================================================

df = d.copy()

df = df[['District_Key','Covaxin','Covishield']]

df.dropna(subset=['Covaxin', 'Covishield'], inplace=True)

df['Covaxin'] = df['Covaxin'].astype('int')
df['Covishield'] = df['Covishield'].astype('int')


df = df.groupby('District_Key').agg('max')

df['districtid'] = df.index

df.reset_index(inplace=True, drop=True)

state = df.copy()
df['vaccineratio'] = df['Covishield']/df['Covaxin']

df.drop(['Covaxin', 'Covishield'], axis=1, inplace = True)

df.sort_values('vaccineratio', inplace=True)

df.reset_index(drop=True, inplace=True)

df.to_csv('output/district-vaccine-type-ratio.csv', index=False)



# =============================================================================
# STATEWISE
# =============================================================================


state['stateid'] = state['districtid'].apply(lambda x: str(x).split('_')[0])

state.drop('districtid', inplace = True, axis = 1)


state = state.groupby('stateid').agg('sum')

state['stateid'] = state.index


state['vaccineratio'] = state['Covishield']/state['Covaxin']

overall = state.copy()

state.drop(['Covaxin', 'Covishield'], axis=1, inplace = True)

state.sort_values('vaccineratio', inplace=True)

state.reset_index(drop=True, inplace=True)

state.to_csv('output/state-vaccine-type-ratio.csv', index=False)


# =============================================================================
# OVERALL
# =============================================================================


tmp = overall['Covishield'].sum()
tmp1 = overall['Covaxin'].sum()


ratio = tmp/tmp1

pd.DataFrame([{'overallid':1, 'vaccineratio': ratio}]).to_csv('output/overall-vaccine-type-ratio.csv', index=False)


####################################################################################
