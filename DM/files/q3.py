#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:32:45 2021

@author: pranshu
"""




import pandas as pd


df3 = pd.read_csv( "districts.csv", low_memory=False)

tbd = [ 'Date', 'District','Confirmed']
df = df3[tbd]

dcodes = pd.read_csv( "data/district_wise.csv", low_memory=False)
dcodes  = dcodes[['District', 'District_Key']]

tmp = dcodes['District'].isin(['Unassigned', 'Unknown', 'Other State'])
dcodes = dcodes[~tmp]



# =============================================================================
# d_map = {}
# 
# for i in range(len(dcodes)):
#     d_map[dcodes.loc[i, 'District']] = dcodes.loc[i, 'District_Key']
# 
# =============================================================================



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


#f3['Week_Number'] = df3['Date Announced'].dt.week
# Getting year. Weeknum is common across years to we need to create unique index by using year and weeknum
#df3['Year'] = df3['Date Announced'].dt.year




df3.sort_values(['District','Date'], inplace = True)




imd = []
districts = list(df3['District'].unique() )


for dist in districts:
    tmp = df3[df3['District']==dist].copy()
    tmp.sort_values('Date', inplace = True)
    tmp.reset_index(drop=True, inplace=True)
    for i in range(len(tmp)-1,0,-1):
        tmp.loc[i, 'Confirmed'] = tmp.loc[i, 'Confirmed'] - tmp.loc[i-1, 'Confirmed']
        if (tmp.loc[i, 'Confirmed']<0):
            tmp.loc[i, 'Confirmed'] = 0
    
    imd.append(tmp)  


df3 = pd.concat(imd, ignore_index=True)


df3 = df3.set_index(pd.to_datetime(df3['Date']))

df4 = df3.groupby('District').resample('W-Sun', on='Date').sum()


df6 = df4.groupby(['Date', 'District']).agg(sum)



final = df6


final['weekid'] = final.index

final['district'] = final['weekid'].apply(lambda x:x[1])
final['weekid'] = final['weekid'].apply(lambda x:x[0])

final.reset_index(inplace=True, drop=True)


# =============================================================================
# 
# for i in range(len(final)):
#     try:
#         final.loc[i, 'districtid'] = d_map[final.loc[i, 'district']]
#     except:
#         pass
# =============================================================================


final.reset_index(drop=True, inplace=True)
column_names = ['weekid']


final.sort_values('weekid', inplace=True)


for col in column_names:
  final[col], tmp  = pd.Series(list(final[col])).factorize()

final['weekid'] = final['weekid'].apply(lambda x: x+1)


cols = list(final.columns)
final = final [['district','weekid', 'Confirmed']]

final.columns = [ 'districtid', 'weekid','cases']

final.reset_index(drop = True, inplace=True)

dcodes.columns = ['districtid', 'District_Key']


final = pd.merge(final,  dcodes, on = 'districtid')

final.drop('districtid', inplace = True, axis =1)
final = final[ [ 'District_Key','weekid','cases' ]]

final.columns = [ 'districtid','weekid','cases']


final.sort_values(['districtid', 'weekid'], inplace = True)


# =============================================================================
# 
# all_cities = final.districtid.unique()
# 
# out =[]
# 
# for city in all_cities:
#     tmp = final[final['districtid']==city].copy()
#     tmp.sort_values(['districtid', 'weekid'], inplace = True)
#     tmp.reset_index(inplace=True, drop=True)
#     #print(tmp)
#     for i in range(len(tmp)-3, 1, -1):
#         #tmp.loc[]
#         tmp.loc[i, 'cases'] -= tmp.loc[i-1, 'cases']
#        # pass
#     tmp.drop([len(tmp)-2, len(tmp)-1], inplace = True, axis = 0)
#     
#     #print(tmp)
#     out.append(tmp)
#     
# 
#     
# 
# final = pd.concat(out, ignore_index=True)
# =============================================================================
final.to_csv('output/week-cases-time.csv', index = False)





# =============================================================================
# MONTHLY
# =============================================================================


df3 = pd.read_csv( "districts.csv", low_memory=False)

tbd = [ 'Date', 'District','Confirmed']
df = df3[tbd]

dcodes = pd.read_csv( "data/district_wise.csv", low_memory=False)
dcodes  = dcodes[['District', 'District_Key']]

tmp = dcodes['District'].isin(['Unassigned', 'Unknown', 'Other State'])
dcodes = dcodes[~tmp]



# =============================================================================
# d_map = {}
# 
# for i in range(len(dcodes)):
#     d_map[dcodes.loc[i, 'District']] = dcodes.loc[i, 'District_Key']
# 
# =============================================================================



df3 = df.copy()


df3['Date'] = pd.to_datetime(df3['Date'], format='%Y-%m-%d')

#	Date Announced
#0	30/01/2020


#df3.sort_values('Date Announced', inplace=True)
df3.reset_index(inplace=True, drop=True)


#df3 = df3.loc[102:, :]

df3 = df3[~(df3['Date'] < '2020-03-15')]
df3 = df3[~(df3['Date'] > '2021-08-14')]


df3['Confirmed'].fillna(0, inplace=True)


df3.dropna(subset=['Date'], inplace=True)

df3.reset_index(inplace=True, drop=True)


df3.reset_index(drop=True, inplace=True)


#f3['Week_Number'] = df3['Date Announced'].dt.week
# Getting year. Weeknum is common across years to we need to create unique index by using year and weeknum
#df3['Year'] = df3['Date Announced'].dt.year




df3.sort_values(['District','Date'], inplace = True)

imd = []
districts = list(df3['District'].unique() )


for dist in districts:
    tmp = df3[df3['District']==dist].copy()
    tmp.sort_values('Date', inplace = True)
    tmp.reset_index(drop=True, inplace=True)
    for i in range(len(tmp)-1,0,-1):
        tmp.loc[i, 'Confirmed'] = tmp.loc[i, 'Confirmed'] - tmp.loc[i-1, 'Confirmed']
    
    imd.append(tmp)  


df3 = pd.concat(imd, ignore_index=True)


for i in range(4,9):
    df3.loc[((df3['Date'] >= '2020-0'+str(i)+'-15') & (df3['Date'] <= '2020-0'+str(i+1)+'-14')), 'monthid'] = i-3

df3.loc[((df3['Date'] >= '2020-09-15') & (df3['Date'] <= '2020-10-14')), 'monthid'] = 6


for i in range(10,12):
    df3.loc[((df3['Date'] >= '2020-'+str(i)+'-15') & (df3['Date'] <= '2020-'+str(i+1)+'-14')), 'monthid'] = i-3


df3.loc[((df3['Date'] >= '2020-12-15') & (df3['Date'] <= '2021-01-14')), 'monthid'] = 9

for i in range(1,8):
    df3.loc[((df3['Date'] >= '2021-0'+str(i)+'-15') & (df3['Date'] <= '2021-0'+str(i+1)+'-14')), 'monthid'] = i+9


df3['monthid'] = df3['monthid'].astype(int)

df3.drop('Date', inplace = True, axis = 1)

 
 
 
df3 = df3.groupby(['District', 'monthid']).agg('sum')
# 
df3['districtid'] = df3.index
df3['monthid'] = df3['districtid'].apply(lambda x: x[1])
df3['districtid'] = df3['districtid'].apply(lambda x: x[0])


df3.reset_index(drop = True, inplace=True)

df3 = df3[ [ 'districtid', 'monthid', 'Confirmed']]

df3.columns = [ 'districtid', 'monthid', 'cases']

dcodes.columns = ['districtid', 'District_Key']

df3 = pd.merge(df3,  dcodes, on = 'districtid')
df3.drop('districtid', inplace = True, axis = 1)


df3 = df3[ [ 'District_Key','monthid','cases' ]]

df3.columns = [ 'districtid','monthid','cases']

df3.sort_values(['districtid', 'monthid'], inplace = True)



df3.to_csv('output/month-cases-time.csv', index = False)

# =============================================================================
# 
# all_cities = df3.District.unique()
# 
# out =[]
# 
# for city in all_cities:
#     
#     tmp = df3[df3['District']==city].copy()
#     tmp.sort_values(['District', 'monthid'], inplace = True)
#     tmp.reset_index(inplace=True, drop=True)
#     #print(tmp)
#     
#     for i in range(1,17):
#         t = {}
#         try:
#             
#             t['districtid'] = city
#             t['monthid'] = i
#             foo = tmp[tmp['monthid']==i].copy()
#             foo.reset_index(inplace=True, drop=True)
#             t['cases'] = foo.loc[len(foo)-2, 'Confirmed'] - foo.loc[0, 'Confirmed']
#             
#         except:
#             t['districtid'] = city
#             t['monthid'] = i
#             t['cases'] = 0
#             print(city)
#             
#         out.append(t)
# =============================================================================
    
# =============================================================================
# df3 = pd.concat(out, ignore_index=True)
# 
# 
# 
# df3 = df3.groupby(['District', 'monthid']).agg('sum')
# 
# df3['districtid'] = df3.index
# df3['monthid'] = df3['districtid'].apply(lambda x: x[1])
# df3['districtid'] = df3['districtid'].apply(lambda x: x[0])
# 
# df3.reset_index(drop = True, inplace=True)
# 
# df3 = df3[ [ 'districtid', 'monthid', 'Confirmed']]
# 
# df3.columns = [ 'districtid', 'monthid', 'cases']
# 
# dcodes.columns = ['districtid', 'District_Key']
# 
# df3 = pd.merge(df3,  dcodes, on = 'districtid')
# df3.drop('districtid', inplace = True, axis = 1)
# =============================================================================



# =============================================================================
# OVERALL
# =============================================================================


df3 = df3.groupby('districtid').agg('sum')

df3.drop('monthid', inplace = True, axis = 1)

df3['districtid'] = df3.index

df3.reset_index(drop=True, inplace = True)


df3 = df3[['districtid', 'cases']]



df3.sort_values(['districtid'], inplace = True)




df3.to_csv('output/overall-cases-time.csv', index = False)
