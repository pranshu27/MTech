#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 06:48:55 2021

@author: pranshu
"""


# =============================================================================
# Question 9

# =============================================================================
# Output them in the following manner: stateid, populationlef t, rateof vaccination, date.
# Call this output file complete-vaccination.csv and the script/program to generate this
# complete-vaccination-generator.sh.
# =============================================================================
# =============================================================================



import pandas as pd 
import math
dfc = pd.read_csv(r'cowin_vaccine_data_districtwise.csv', low_memory=False)
dfc = dfc.loc[1:, :]
dfc.reset_index(drop=True, inplace=True)

per1 = pd.date_range(start ='16-01-2021', \
         end ='14-08-2021', freq ='D')
    
rd = [d.strftime('%d/%m/%Y') for d in per1]

out = []

for j in range(len(rd)):
    for i in range(len(dfc)):
        td = {}
        td['State'] = dfc.loc[i, 'State']
        td['State_Code'] = dfc.loc[i, 'State_Code']
        td['District_Key'] = dfc.loc[i, 'District_Key']
        td['District'] = dfc.loc[i, 'District']
        td['Date'] = rd[j]
        td['Dose1'] = dfc.loc[i,rd[j]+'.3']
        td['Dose2'] = dfc.loc[i,rd[j]+'.4']
        
        out.append(td)
    

df = pd.DataFrame(out)

my_df = df.copy()
my_df = my_df[['Date', 'State','State_Code', 'Dose1' ]]
my_df['Date'] = pd.to_datetime(my_df['Date'], format='%d/%m/%Y')
    
   
my_df.dropna(subset=['Dose1'], inplace=True)

my_df['Dose1'] = my_df['Dose1'].astype('int')
#my_df['Dose2'] = my_df['Dose2'].astype('int')


# =============================================================================
# my_df = my_df.groupby('State').agg('max')
# 
# my_df['State_Code'] = my_df.index
# 
# my_df.reset_index(drop = True, inplace=True)
# =============================================================================


temp = df[['State', 'State_Code']]
state_map = {}
for i in range(len(temp)):
    if(temp.iloc[i, 0] not in state_map.keys()):
        state_map[temp.iloc[i, 0]] =   temp.iloc[i, 1]  
    

census = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx', \
                       sheet_name='Sheet1')
    
    
census = census[(census['Level']=='STATE') & ((census['TRU']=='Total') )]

census = census[['Name', 'TOT_P']]

census.reset_index(inplace=True, drop = True)
census.columns = ['State', 'Total']
#my_df.columns = ['State', 'Dose1', 'Dose2']
my_df.reset_index(inplace=True, drop = True)
# =============================================================================
# 
# for i in range(len(my_df)):
#     #print(i)
#     my_df.loc[i, 'State_Code'] = state_map[my_df.loc[i, 'State']]
# =============================================================================

census['State'] = census['State'].apply(lambda x: str(x).lower().replace('&', 'and').strip())
my_df['State'] = my_df['State'].apply(lambda x: str(x).lower().replace('delhi','	nct of delhi' ).strip())

census[census['State'].isin(['daman and diu', 'dadra and nagar haveli'])].sum()
# =============================================================================
# State    daman and diudadra and nagar haveli
# Total                                 586956
# dtype: object
# 
# =============================================================================
census.drop([24,25], inplace = True)
census.reset_index(inplace=True, drop = True)

l = len(census)
census.loc[l, 'State'] = '	dadra and nagar haveli and daman and diu'.strip()

census.loc[l, 'Total'] = 586956


tmp = my_df['State'].isin(census['State'])

my_df = my_df[tmp]

my_df.reset_index(inplace=True, drop = True)

#my_df.drop('State', inplace = True, axis = 1)

my_df = my_df.groupby(['State_Code','State', 'Date']).agg('max')

 
my_df['Date'] = my_df.index

my_df['State_Code'] = my_df['Date'].apply(lambda x:x[0])
my_df['State'] = my_df['Date'].apply(lambda x:x[1])
my_df['Date'] = my_df['Date'].apply(lambda x:x[2])   
    
my_df.reset_index(inplace=True, drop = True)

my_df = my_df[['State','State_Code', 'Date', 'Dose1']]

for i in range(len(my_df)):
    my_df.loc[i,'Total'] = \
        list(census[census['State'] == my_df.loc[i,'State']]['Total'])

my_df['Left'] = my_df['Total'] - my_df['Dose1']

my_df['Change'] = my_df['Dose1'].pct_change()


#stateid, populationlef t, rateof vaccination, date
all_states = list(my_df['State'].unique())

my_df['Left'] = my_df['Left'].astype(int)
my_df['Date'] = pd.to_datetime(my_df['Date'], format='%d/%m/%Y')
my_df['Change'].fillna(0, inplace=True)
my_df['Change'] = my_df['Change'].astype(int)


out = []

for state in all_states:
    tmp = {}
    tdf = my_df[my_df['State']==state]
    tdf.reset_index(inplace=True, drop = True)
    l = len(tdf)
    tmp['stateid'] = list(tdf.loc[tdf['State']==state, 'State_Code'])[0]
    tmp['populationleft'] = list(tdf[tdf['Date']=='2021-08-14']['Left'])[0]
    s = (-1)*(tdf.loc[tdf[tdf['Date']=='2021-08-14 00:00:00'].index, 'Left'].values[0] \
                                - tdf.loc[tdf[tdf['Date']=='2021-08-07 00:00:00'].index, 'Left'].values[0])
    #print(s)
    tmp['rateofvaccination'] = s/7
 
    delta = math.ceil(tmp['populationleft']/tmp['rateofvaccination'])
    #print(tmp['rateofvaccination'],tmp['populationleft'], delta)
    tmp['date'] = (tdf.loc[l-1, 'Date'] + pd.DateOffset(days=delta)).strftime(format='%d/%m/%Y')
    out.append(tmp)
    

out_df = pd.DataFrame(out)

out_df.to_csv('output/complete-vaccination.csv', index = False)

