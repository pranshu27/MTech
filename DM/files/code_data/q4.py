#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:54:26 2021

@author: pranshu
"""
import pandas as pd
import numpy as np



df3 = pd.read_csv( "districts.csv", low_memory=False)

tbd = [ 'Date', 'District','Confirmed']
df = df3[tbd]

dcodes = pd.read_csv( "district_wise.csv", low_memory=False)
dcodes  = dcodes[['District', 'District_Key', 'State', 'State_Code']]

tmp = dcodes['District'].isin(['Unassigned', 'Unknown', 'Other State'])
dcodes = dcodes[~tmp]

df3 = df.copy()


df3['Date'] = pd.to_datetime(df3['Date'], format='%Y-%m-%d')

#	Date Announced
#0	30/01/2020


#df3.sort_values('Date Announced', inplace=True)
df3.reset_index(inplace=True, drop=True)


#df3 = df3.loc[102:, :]

df3 = df3[~(df3['Date'] < '2020-03-15')]
df3 = df3[~(df3['Date'] > '2021-08-14')]

#df3.drop(df3[df3['Date Announced'] < '2020-15-03 00:00:00'].index, inplace=True)


#df3['Day'] = df3['Date Announced'].dt.dayofweek



df3['Confirmed'].fillna(0, inplace=True)


df3.dropna(subset=['Date'], inplace=True)

df3.reset_index(inplace=True, drop=True)


df3.reset_index(drop=True, inplace=True)



df3.sort_values(['District','Date'], inplace = True)


#print('removing duplicates')

imd = []
districts = list(df3['District'].unique() )


for dist in districts:
    tmp = df3[df3['District']==dist].copy()
    tmp.sort_values('Date', inplace = True)
    tmp.reset_index(drop=True, inplace=True)
    
    temp = tmp.shift(1)
    temp.fillna(0,inplace=True)
    tmp['Confirmed'] = tmp['Confirmed'] - temp['Confirmed']
    #tmp.set_index('Date',inplace=True)
# =============================================================================
#     for i in range(len(tmp)-1,0,-1):
#         tmp.loc[i, 'Confirmed'] = tmp.loc[i, 'Confirmed'] - tmp.loc[i-1, 'Confirmed']
#     
# =============================================================================
    imd.append(tmp)  
    

df3 = pd.concat(imd, ignore_index=True)
df3['Confirmed'] = df3['Confirmed'] .apply(lambda x: 0 if (x<0) else x)

##############
df3['Date'] = pd.to_datetime(df3['Date'], format='%Y-%m-%d')

#	Date Announced
#0	30/01/2020


#df3.sort_values('Date Announced', inplace=True)
df3.reset_index(inplace=True, drop=True)


#df3 = df3.loc[102:, :]

df3 = df3[~(df3['Date'] < '2020-03-15')]
df3 = df3[~(df3['Date'] > '2021-08-14')]


for i in range(4,9):
    df3.loc[((df3['Date'] >= '2020-0'+str(i)+'-15') & (df3['Date'] <= '2020-0'+str(i+1)+'-14')), 'monthid'] = i-3

df3.loc[((df3['Date'] >= '2020-09-15') & (df3['Date'] <= '2020-10-14')), 'monthid'] = 6


for i in range(10,12):
    df3.loc[((df3['Date'] >= '2020-'+str(i)+'-15') & (df3['Date'] <= '2020-'+str(i+1)+'-14')), 'monthid'] = i-3


df3.loc[((df3['Date'] >= '2020-12-15') & (df3['Date'] <= '2021-01-14')), 'monthid'] = 9

for i in range(1,8):
    df3.loc[((df3['Date'] >= '2021-0'+str(i)+'-15') & (df3['Date'] <= '2021-0'+str(i+1)+'-14')), 'monthid'] = i+9


df3['monthid'] = df3['monthid'].astype(int)

md = df3.copy()


md = md.groupby(['District', 'monthid']).agg('sum')
# 
md['districtid'] = md.index
md['monthid'] = md['districtid'].apply(lambda x: x[1])
md['districtid'] = md['districtid'].apply(lambda x: x[0])


md.reset_index(drop = True, inplace=True)

state_md = md.copy()
####################



#f3['Week_Number'] = df3['Date Announced'].dt.week
# Getting year. Weeknum is common across years to we need to create unique index by using year and weeknum
#df3['Year'] = df3['Date Announced'].dt.year



df3 = df3.set_index(pd.to_datetime(df3['Date']))

df4 = df3.groupby('District').resample('W-Sun', on='Date').sum()
df5 = df3.groupby('District').resample('W-Thu', on='Date').sum()


df6 = df4.groupby(['Date', 'District']).sum()

df7 = df5.groupby(['Date', 'District']).sum()


final = df6.append(df7)


final['weekid'] = final.index

final['districtid'] = final['weekid'].apply(lambda x:x[1])
final['weekid'] = final['weekid'].apply(lambda x:x[0])


final.reset_index(drop=True, inplace=True)


final.sort_values('weekid', inplace=True)




final['weekid_num'], tmp  = pd.Series(list(final['weekid'])).factorize()

final['weekid_num'] = final['weekid_num'].apply(lambda x: x+1)

final.drop(['monthid', 'weekid'], inplace=True, axis = 1)





cols = list(final.columns)



# =============================================================================
# 
# final.reset_index(drop = True, inplace=True)
# 
# 
# all_cities = df3.District.unique()
# 
# out =[]
# 
# 
# for city in all_cities:
#     
#     tmp = final[final['districtid']==city].copy()
#     tmp.sort_values(['districtid', 'weekid_num'], inplace = True)
#     tmp.reset_index(inplace=True, drop=True)
#     print(tmp)
#     
#     for i in range(tmp.loc[0, 'weekid_num'],tmp.loc[0, 'weekid_num']+tmp.loc[len(tmp)-1, 'weekid_num'] ):
#         t = {}
#         try:
#             
#             t['districtid'] = city
#             t['weekid_num'] = i
#             foo = tmp[tmp['weekid_num']==i].copy()
#             print(foo)
#             foo.reset_index(inplace=True, drop=True)
#             t['cases'] = foo.loc[len(foo)-2, 'Confirmed'] - foo.loc[0, 'Confirmed']
#             print(foo.loc[len(foo)-2, 'Confirmed'] - foo.loc[0, 'Confirmed'])
#             
#         except:
#             t['districtid'] = city
#             t['weekid_num'] = i
#             t['cases'] = 0
#             #print(city)
#         print(t)   
#         out.append(t)
#         break
#     break
# 
# =============================================================================


''' week1 - 21 first wave
109-125 wave 2

month 1-3 wave 1

13-15 wave 2

'''
all_dists = list(set(final['districtid']))

final.columns = ['cases', 'districtid', 'weekid_num']


final['cases'] = final['cases'].astype(int)
final_first = final[((final['weekid_num']>=0) & (final['weekid_num']<=25))]
final_second = final[((final['weekid_num']>=109) & (final['weekid_num']<=133))]

md_first = md[((md['monthid']>=1) & (md['monthid']<=3))]
md_second = md[((md['monthid']>=13) & (md['monthid']<=15))]



#faltu = set(final_first.districtid) & set(final['districtid'])

out = []
for i in range(len(all_dists)):
    
    try: 
        tmp = {}
        tmp['districtid'] = all_dists[i]
        df_curr =  final_first[final_first['districtid']==all_dists[i]]
        maxx = df_curr['cases'].max()
        tmp['wave1-weekid'] =str(list(set(df_curr.loc[df_curr['cases']==maxx, 'weekid_num']))[0]).replace('{', '').replace('}', '')
        
        df_curr =  final_second[final_second['districtid']==all_dists[i]]
        maxx = df_curr['cases'].max()
        tmp['wave2-weekid'] =str(list(set(df_curr.loc[df_curr['cases']==maxx, 'weekid_num']))[0]).replace('{', '').replace('}', '')
 
        df_curr =  md_first[md_first['districtid']==all_dists[i]]
        maxx = df_curr['Confirmed'].max()
        tmp['wave1-monthid'] =str(list(set(df_curr.loc[df_curr['Confirmed']==maxx, 'monthid']))[0]).replace('{', '').replace('}', '')
        
        df_curr =  md_second[md_second['districtid']==all_dists[i]]
        maxx = df_curr['Confirmed'].max()
        tmp['wave2-monthid'] =str(list(set(df_curr.loc[df_curr['Confirmed']==maxx, 'monthid']))[0]).replace('{', '').replace('}', '')       
        
        
        
        out.append(tmp)
        
        
        
    except:
        #print(all_dists[i])
        pass
       
ola = pd.DataFrame(out).replace('set()', 'NA')

dcodes = pd.read_csv( "district_wise.csv", low_memory=False)
dcodes  = dcodes[['District', 'District_Key']]

tmp = dcodes['District'].isin(['Unassigned', 'Unknown', 'Other State'])
dcodes = dcodes[~tmp]   

dcodes.columns = ['districtid', 'District_Key']

ola = pd.merge(ola,  dcodes, on = 'districtid')

ola.drop('districtid', inplace = True, axis = 1)

ola = ola[['District_Key','wave1-weekid', 'wave2-weekid', 'wave1-monthid', 'wave2-monthid']]
ola.columns = ['districtid','wave1-weekid', 'wave2-weekid', 'wave1-monthid', 'wave2-monthid']
    
ola.to_csv('output/districtid-peeks.csv', index = False)


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# # # # # # STATEWISE
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
import pandas as pd

df3 = pd.read_csv( "districts.csv", low_memory=False)

tbd = [ 'Date', 'State','Confirmed']
df = df3[tbd]

dcodes = pd.read_csv( "district_wise.csv", low_memory=False)
dcodes  = dcodes[['District', 'District_Key', 'State', 'State_Code']]


df3 = df.copy()


df3['Date'] = pd.to_datetime(df3['Date'], format='%Y-%m-%d')

#	Date Announced
#0	30/01/2020


#df3.sort_values('Date Announced', inplace=True)
df3.reset_index(inplace=True, drop=True)


#df3 = df3.loc[102:, :]

df3 = df3[~(df3['Date'] < '2020-03-15')]
df3 = df3[~(df3['Date'] > '2021-08-14')]

#df3.drop(df3[df3['Date Announced'] < '2020-15-03 00:00:00'].index, inplace=True)


#df3['Day'] = df3['Date Announced'].dt.dayofweek



df3['Confirmed'].fillna(0, inplace=True)


df3.dropna(subset=['Date'], inplace=True)

df3.reset_index(inplace=True, drop=True)


df3.reset_index(drop=True, inplace=True)




df3.sort_values(['State','Date'], inplace = True)


#print('removing duplicates')

imd = []
states = list(df3['State'].unique() )


for state in states:
    tmp = df3[df3['State']==state].copy()
    tmp.sort_values('Date', inplace = True)
    tmp.reset_index(drop=True, inplace=True)
    '''
    temp = tmp.shift(1)
    temp.fillna(0,inplace=True)
    tmp['Confirmed'] = tmp['Confirmed'] - temp['Confirmed']'''
    #tmp.set_index('Date',inplace=True)
# =============================================================================
    for i in range(len(tmp)-1,0,-1):
         tmp.loc[i, 'Confirmed'] = tmp.loc[i, 'Confirmed'] - tmp.loc[i-1, 'Confirmed']
#     
# =============================================================================
    imd.append(tmp)  
    


df3 = pd.concat(imd, ignore_index=True)

df3['Confirmed'] = df3['Confirmed'] .apply(lambda x: 0 if (x<0) else x)


##############
df3['Date'] = pd.to_datetime(df3['Date'], format='%Y-%m-%d')


df3.reset_index(inplace=True, drop=True)


#df3 = df3.loc[102:, :]

df3 = df3[~(df3['Date'] < '2020-03-15')]
df3 = df3[~(df3['Date'] > '2021-08-14')]


for i in range(4,9):
    df3.loc[((df3['Date'] >= '2020-0'+str(i)+'-15') & (df3['Date'] <= '2020-0'+str(i+1)+'-14')), 'monthid'] = i-3

df3.loc[((df3['Date'] >= '2020-09-15') & (df3['Date'] <= '2020-10-14')), 'monthid'] = 6


for i in range(10,12):
    df3.loc[((df3['Date'] >= '2020-'+str(i)+'-15') & (df3['Date'] <= '2020-'+str(i+1)+'-14')), 'monthid'] = i-3


df3.loc[((df3['Date'] >= '2020-12-15') & (df3['Date'] <= '2021-01-14')), 'monthid'] = 9

for i in range(1,8):
    df3.loc[((df3['Date'] >= '2021-0'+str(i)+'-15') & (df3['Date'] <= '2021-0'+str(i+1)+'-14')), 'monthid'] = i+9


df3['monthid'] = df3['monthid'].astype(int)

md = df3.copy()


md = md.groupby(['State', 'monthid']).agg('sum')
# 
md['stateid'] = md.index
md['monthid'] = md['stateid'].apply(lambda x: x[1])
md['stateid'] = md['stateid'].apply(lambda x: x[0])


md.reset_index(drop = True, inplace=True)

overall_md = md.copy()

####################



#f3['Week_Number'] = df3['Date Announced'].dt.week
# Getting year. Weeknum is common across years to we need to create unique index by using year and weeknum
#df3['Year'] = df3['Date Announced'].dt.year



df3 = df3.set_index(pd.to_datetime(df3['Date']))

df4 = df3.groupby('State').resample('W-Sun', on='Date').sum()
df5 = df3.groupby('State').resample('W-Thu', on='Date').sum()


df6 = df4.groupby(['Date', 'State']).sum()

df7 = df5.groupby(['Date', 'State']).sum()


final = df6.append(df7)


final['weekid'] = final.index

final['stateid'] = final['weekid'].apply(lambda x:x[1])
final['weekid'] = final['weekid'].apply(lambda x:x[0])


final.reset_index(drop=True, inplace=True)


final.sort_values('weekid', inplace=True)




final['weekid_num'], tmp  = pd.Series(list(final['weekid'])).factorize()

final['weekid_num'] = final['weekid_num'].apply(lambda x: x+1)

final.drop(['monthid', 'weekid'], inplace=True, axis = 1)



final.reset_index(drop=True, inplace=True)


cols = list(final.columns)


all_states = list(set(final['stateid']))

final.columns = ['cases', 'stateid', 'weekid_num']


final['cases'] = final['cases'].astype(int)

overall_final = final.copy()   
     
final_first = final[((final['weekid_num']>=0) & (final['weekid_num']<=25))]
final_second = final[((final['weekid_num']>=109) & (final['weekid_num']<=133))]

md_first = md[((md['monthid']>=1) & (md['monthid']<=3))]
md_second = md[((md['monthid']>=13) & (md['monthid']<=15))]



#faltu = set(final_first.districtid) & set(final['districtid'])

out = []
for i in range(len(all_states)):
    
    try: 
        tmp = {}
        tmp['stateid'] = all_states[i]
        df_curr =  final_first[final_first['stateid']==all_states[i]]
        maxx = df_curr['cases'].max()
        tmp['wave1-weekid'] =str(list(set(df_curr.loc[df_curr['cases']==maxx, 'weekid_num']))[0]).replace('{', '').replace('}', '')
        
        df_curr =  final_second[final_second['stateid']==all_states[i]]
        maxx = df_curr['cases'].max()
        tmp['wave2-weekid'] =str(list(set(df_curr.loc[df_curr['cases']==maxx, 'weekid_num']))[0]).replace('{', '').replace('}', '')
 
        df_curr =  md_first[md_first['stateid']==all_states[i]]
        maxx = df_curr['Confirmed'].max()
        tmp['wave1-monthid'] =str(list(set(df_curr.loc[df_curr['Confirmed']==maxx, 'monthid']))[0]).replace('{', '').replace('}', '')
        
        df_curr =  md_second[md_second['stateid']==all_states[i]]
        maxx = df_curr['Confirmed'].max()
        tmp['wave2-monthid'] =str(list(set(df_curr.loc[df_curr['Confirmed']==maxx, 'monthid']))[0]).replace('{', '').replace('}', '')       
        
        
        
        out.append(tmp)
        
        
        
    except:
        #print(all_dists[i])
        pass


ola = pd.DataFrame(out).replace('set()', 'NA')

dcodes = pd.read_csv( "district_wise.csv", low_memory=False)


tbd = []
for i in range(len(ola)):
     try:
         ola.loc[i, 'stateid'] = dcodes[dcodes['State']==ola.loc[i, 'stateid']]['State_Code'].values[0]
     except:
         tbd.append(i)

ola = ola[['stateid','wave1-weekid', 'wave2-weekid', 'wave1-monthid', 'wave2-monthid']]
    
ola.to_csv('output/stateid-peeks.csv', index = False)



# =============================================================================
# OVERALL
# =============================================================================


overall_final

overall_final = overall_final.groupby(['weekid_num']).agg('sum')
overall_md = overall_md.groupby(['monthid']).agg('sum')

