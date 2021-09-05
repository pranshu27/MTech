#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:52:14 2021

@author: pranshu
"""

import json
import pandas as pd



with open(r'/home/joker/Downloads/Video/SEM1-Downloads/DM/neighbor-districts.json') as f:
    
    js = json.load(f)
    #df = pd.json_normalize(js)

out = []
for key, value in js.items():
    tmp = {}
    tmp['district'] = key
    tmp['neighbours'] = value
    
    out.append(tmp)
    
   # print(key, value)
    
df = pd.DataFrame(out)
df['neighbours'] = df['neighbours'].apply(lambda x: str(x).replace('[', '').replace(']', '').replace("'", ""))

df[df['district'].str.contains('mumbai')]


#--------------------------------------------------------------------------

df1 = df.copy()
df1['district'] = df['district'].apply(lambda x: str(x).split('/')[0].lower().replace('_district', '').replace('_', ' '))

df1['neighbours'] = df1['neighbours'].apply(lambda x: [str(s).split('/')[0].lower().strip().replace('_district', '').replace('_', ' ') for s in str(x).split(',')])

df1['neighbours'] = df1['neighbours'].apply(lambda x: str(x).replace('[', '').replace(']', '').replace("'", ""))

dfc = pd.read_csv(r'/home/joker/Downloads/Video/SEM1-Downloads/DM/cowin_vaccine_data_districtwise.csv')


def corrected_name( x ):
    if(x=="aizwal"):
        x = "aizawl"
    if(x=="rae bareilly"):
        x = "rae bareli"
    if(x=='anugul'):
        x = 'angul'
    if(x=='ashok nagar'):
        x = 'ashoknagar'
    if(x=='badgam'):
        x = 'budgam'
    if(x=='baleshwar'):
        x = 'bageshwar'
    if(x=='banas kantha'):
        x = 'banaskantha'
    if(x=='bangalore rural'):
        x = 'bengaluru rural'
    if(x=='bangalore urban'):
        x = 'bengaluru urban'
    if(x=='baramula'):
        x = 'baramulla'
    if(x=='baudh'):
        x = 'boudh'
    if(x=='belgaum'):
        x = 'belagavi'
    if(x=='bellary'):
        x = 'ballari'
    if(x=='bemetara'):
        x = 'bametara'
    if(x=='bid'):
        x = 'beed'
    if(x=='bishwanath'):
        x = 'biswanath'
#     if(x=='central delhi'):
#         x = 'delhi'
    if(x=='chamarajanagar'):
        x = 'chamarajanagara'
    if(x=='dantewada'):
        x = 'dakshin bastar dantewada'
    if(x=='debagarh'):
        x = 'deogarh'
    if(x=='devbhumi dwaraka'):
        x = 'devbhumi dwarka'
    if(x=='dhaulpur'):
        x = 'dholpur'
#     if(x=='east delhi'):
#         x = "delhi"
    if(x=='east karbi anglong'):
        x = 'karbi anglong'
    if(x=='faizabad'):
        x = 'ayodhya'
    if(x=='fategarh sahib'):
        x = 'fatehgarh sahib'
    if(x=='firozpur'):
        x = 'ferozepur'
    if(x=='gondiya'):
        x = 'gondia'
    if(x=='hugli'):
        x = 'hooghly'
    if(x=='jagatsinghapur'):
        x = 'jagatsinghpur'
    if(x=='jajapur'):
        x = 'jajpur'
    if(x=='jalor'):
        x = 'jalore'
    if(x=='janjgir-champa'):
        x = 'janjgir champa'
    if(x=='jhunjhunun'):
        x = 'jhunjhunu'
    if(x=='jyotiba phule nagar'):
        x = 'amroha'
    if(x=='kabirdham'):
        x = 'kabeerdham'
    if(x=='kaimur (bhabua)'):
        x = 'kaimur'
    if(x=='kanchipuram'):
        x = 'kancheepuram'
    if(x=='kheri'):
        x = 'lakhimpur kheri'
    if(x=='kochbihar'):
        x = 'cooch behar'
    if(x=='kodarma'):
        x = 'koderma'
    if(x=='komram bheem'):
        x = 'komaram bheem'
    if(x=='konkan division'): #not found
        x = 'konkan division'
    if(x=='lahul and spiti'):
        x = 'lahaul and spiti'
    if(x=='mahesana'):
        x = 'mehsana'
    if(x=='mahrajganj'):
        x = 'maharajganj'
    if(x=='maldah'):
        x = 'malda'
    if(x=='marigaon'):
        x = 'morigaon'
    if(x=='medchal–malkajgiri'):
        x = 'medchal malkajgiri'
    if(x=='muktsar'): #not found
        x = 'sri muktsar sahib'
#     if(x=='mumbai city'):
#         x = 'mumbai'
#     if x== 'mumbai suburban':
#         x = 'mumbai'
    if x== 'nandubar':
        x = 'nandurbar'
    if x== 'narsimhapur':
        x = 'narsinghpur'
    if x== 'nav sari':
        x = 'navsari'
#     if x=='new delhi' :
#         x = 'delhi'
    if x== 'noklak': #not found
        x = 'noklak'
#     if x== 'north delhi':
#         x = 'delhi'
#     if x== 'north east delhi':
#         x = 'delhi'
#     if x== 'north west delhi':
#         x = 'delhi'
    if x== 'pakaur':
        x = 'pakur'
    if x== 'palghat':
        x = 'palghar'
    if x== 'panch mahal':
        x = 'panchmahal'
    if x== 'pashchim champaran':
        x = 'west champaran'
    if x== 'pashchimi singhbhum':
        x = 'west singhbhum'
    if x== 'pattanamtitta':
        x = 'pathanamthitta'
    if x== 'purba champaran':
        x = 'east champaran'
    if x== 'purbi singhbhum':
        x = 'east singhbhum'
    if x== 'puruliya':
        x = 'purulia'
    if x== 'rajauri':
        x = 'rajouri'
    if x== 'rangareddy':
        x = 'ranga reddy'
    if x== 'ri-bhoi':
        x = 'ribhoi'
    if x== 'sabar kantha':
        x = 'sabarkantha'
    if x== 'sahibzada ajit singh nagar':
        x = 's.a.s. nagar'
    if x== 'sait kibir nagar':
        x = 'sant kabir nagar'
    if x== 'sant ravidas nagar':
        x = 'bhadohi'
    if x== 'sepahijala':
        x = 'sipahijala'
    if x== 'seraikela kharsawan':
        x = 'saraikela-kharsawan'
    if x== 'shahdara': #not found
        x = 'shahdara'
    if x== 'shaheed bhagat singh nagar':
        x = 'shahid bhagat singh nagar'
    if x== 'sharawasti':
        x = 'shrawasti'
    if x== 'shimoga':
        x = 'shivamogga'
    if x== 'shopian':
        x = 'shopiyan'
    if x== 'siddharth nagar':
        x = 'siddharthnagar'
    if x== 'sivagangai':
        x = 'sivaganga'
    if x== 'sonapur':
        x = 'subarnapur'
#     if x== 'south delhi':
#         x = 'delhi'
#     if x== 'south east delhi':
#         x = 'delhi'
    if x== 'south salmara-mankachar':
        x = 'south salmara mankachar'
#     if x== 'south west delhi':
#         x = 'delhi'
    if x== 'sri ganganagar':
        x = 'ganganagar'
    if x== 'sri potti sriramulu nellore':
        x = 's.p.s. nellore'
    if x== 'the dangs':
        x = 'dang'
    if x== 'the nilgiris':
        x = 'nilgiris'
    if x== 'thoothukudi':
        x = 'thoothukkudi'
    if x== 'tiruchchirappalli':
        x = 'tiruchirappalli'
    if x== 'tirunelveli kattabo':
        x = 'tirunelveli'
    if x== 'tiruvanamalai':
        x = 'tiruvannamalai'
    if x== 'tumkur':
        x = 'tumakuru'
    if x== 'west delhi':
        x = 'delhi'
    if x== 'yadagiri':
        x = 'yadadri bhuvanagiri'
    if x== 'ysr':
        x = 'y.s.r. kadapa'
    return x

dfc = dfc[['District_Key', 'District']]

cowid_districts = dfc['District']


dfd = pd.read_csv(r'/home/joker/Downloads/Video/SEM1-Downloads/DM/district_wise.csv')

dfd = dfd[['District_Key', 'District']]
vaccine_districts = dfd['District']

for i in range(len(vaccine_districts)):
    try:
        vaccine_districts[i] = vaccine_districts[i].lower()
    except :
        pass

for i in range(len(cowid_districts)):
    try:
        cowid_districts[i] = cowid_districts[i].lower()
    except :
        pass
    
    
cowin_districts = list(set(cowid_districts) & set(vaccine_districts))


for i in range(len(df1)):
    df1.iloc[i, 0] = corrected_name(df1.iloc[i, 0])
    tmp = str(df1.loc[i, 'neighbours'])
    nbs = tmp.split(', ')
    for j in range(len(nbs)):
        nbs[j] = corrected_name(nbs[j])
    
    df1.loc[i, 'neighbours'] = ",".join(nbs)   
    
tot_len = len(df1)
for i in range(tot_len):
    try:
        curr = str(df1.iloc[i, 0])
        
        if (curr not in cowin_districts):
            #print(curr)
            print(i, curr)
            df1.drop(df1[df1['district']==curr].index, inplace=True)
# =============================================================================
#             for k in range(len(df1)):
#                 try:
#                     new_cols = df1.loc[k, 'neighbours'].split(',').remove(curr)
#                     df1.loc[k, 'neighbours'] = str(new_cols).replace('[', '').replace(']', '').replace("'", '')
#                 except:
#                     pass
# =============================================================================
    except :
        print("error", i)
# =============================================================================
#         
#         for k in range(len(df1)):
#             try:
#                 new_cols = df1.loc[k, 'neighbours'].split(',').remove(curr)
#                 df1.loc[k, 'neighbours'] = str(new_cols).replace('[', '').replace(']', '').replace("'", '')
#             except:
#                 pass
#     
# =============================================================================
            
        
df1.reset_index(inplace=True, drop=True)

common_dist = set(df1['district'] ) &set(cowin_districts) 

dfc_only = set(cowin_districts) - common_dist
df1_only = set(df1['district']) - common_dist

def combine(city):
    print(city)
    all_city = list(df1[df1['district'].str.contains(city)]['district'])
    print(all_city)
    neighbours = list()
    for d in all_city:
        tmp = str(df1[df1['district']==d]['neighbours'].values[0]).split(', ')
        neighbours.extend(tmp)
        df1.drop(df1[df1['district']==d].index, inplace=True)
    
        #print(tmp, type(tmp))
    neighbours = set(neighbours)
    tmp_dict = {}
    tmp_dict['district'] = city
    tmp_dict['neighbours'] = str(neighbours).replace('{', '').replace('}', '').replace("'", '')
    
    df1.loc[len(df.index)] = tmp_dict

#df1.drop(df1[df1['district']=='delhi'].index, inplace=True)

'''

#df1[df1['district'].str.contains( 'south')]['district']
tbc = ['delhi','champaran', 'sikkim', 'singhbhum', '24 parganas', \
       'salmara mankachar', 'goa',  'karbi anglong', 'tripura', 'godavari', \
           'jaintia hills', 'siang', 'kameng', 'garo hills', \
           'khasi hills', 'imphal', 'mumbai', 'warangal', 'kanpur' ]

for t in tbc:
    try:
        combine(t)
        print("merged ", t)
        print('\n')
    except:
        print("can't merge ", t)
        print('\n')

'''

combine('mumbai')

#dfc[dfc['District']==df1.loc[721, 'district']]['District_Key'].values[0]
df1.reset_index(inplace=True, drop=True)


tbd = []
for i in range(len(df1)):
    try:
        df1.loc[i, 'district_code'] = dfc[dfc['District']==df1.loc[i, 'district']]['District_Key'].values[0]
    except:
        tbd.append(i)
        print(i)
        #print(df1.loc[i, 'district'])
    



df1.drop(tbd, inplace=True)

df1.sort_values('district_code', inplace=True)
#dfc[dfc['District']==df1.loc[0, 'district']]['District_Key'].values[0]
df1.to_json('temp.json', orient='records', lines=True)

'''


more_common = set(dml_only) & set(df1_list)

df1_only = set(df1_list)-more_common

'''
####################################################################Question2#########################

#df2 = df1.copy()
out = []
def check(out, item):
    for i in range(len(out)):
        if(item == out[i]):
            return True
        
    return False
    

#print(check(out, {'district': 'lahaul and spiti', 'neighbour': 'leh'}))


for i in range(len(df1)):
    #df2.iloc[j, 'district'] = df1.loc[i, 'district']
    try:
        curr = df1.loc[i, 'district']
        #print(curr, '\n')

        #print(df1.loc[i, 'neighbours'].split(','))
        n_l = df1.loc[i, 'neighbours'].split(',')
        #print(n_l)
        for k in n_l:
            #print(k)
            tmp = {}
            tmp['district'] = curr
            tmp['neighbour'] = k
            if(check(out, {'district': k, 'neighbour': curr}) == False):
                
                out.append(tmp)

    except:
        print(curr)
    
        
df2 = pd.DataFrame(out) 

df2.to_csv('edge_list.csv')

#df1.loc[0, 'neighbours'].split(',')

####################################################################Question3#########################


'''
import os, glob
import pandas as pd

path = "/home/joker/Downloads/Video/SEM1-Downloads/DM/csvs"


all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = [pd.read_csv(f, sep=',') for f in all_files]
df_merged   = pd.concat(df_from_each_file, ignore_index=True)


df_merged.to_csv( "/home/joker/Downloads/Video/SEM1-Downloads/DM/covid_all_Data.csv")


'''


# =============================================================================
# =============================================================================
# 
# =============================================================================
# =============================================================================
# p = "/home/joker/Downloads/Video/SEM1-Downloads/DM/csvs/raw_data"
# 
# 
# 
# paths = [p + str(i) + '.csv' for i in range(1,34)]
# 
# df_from_each_file = [pd.read_csv(f, sep=',') for f in paths]
# df_merged   = pd.concat(df_from_each_file, ignore_index=True)
# 
# 
# df_merged.to_csv( "/home/joker/Downloads/Video/SEM1-Downloads/DM/covid_all_Data.csv")
# =============================================================================
# =============================================================================
# 
# 
# =============================================================================
# =============================================================================


import pandas as pd
import numpy as np

df3 = pd.read_csv( "/home/joker/Downloads/Video/SEM1-Downloads/DM/covid_all_Data.csv", low_memory=False)
tbd = [ 'Date Announced', \
       'Detected District',\
         'Num Cases']
df3 = df3[tbd]

df3['Date Announced'] = pd.to_datetime(df3['Date Announced'], format='%d/%m/%Y')

#	Date Announced
#0	30/01/2020


#df3.sort_values('Date Announced', inplace=True)
df3.reset_index(inplace=True, drop=True)


#df3 = df3.loc[102:, :]

df3 = df3[~(df3['Date Announced'] < '2020-03-15')]
df3 = df3[~(df3['Date Announced'] > '2021-08-14')]

#df3.drop(df3[df3['Date Announced'] < '2020-15-03 00:00:00'].index, inplace=True)


#df3['Day'] = df3['Date Announced'].dt.dayofweek



df3['Num Cases'].fillna(0, inplace=True)


df3.dropna(subset=['Date Announced'], inplace=True)

df3.reset_index(inplace=True, drop=True)

df3['cases'] = df3['Num Cases'].astype(int)

df3.reset_index(drop=True, inplace=True)


#f3['Week_Number'] = df3['Date Announced'].dt.week
# Getting year. Weeknum is common across years to we need to create unique index by using year and weeknum
#df3['Year'] = df3['Date Announced'].dt.year


df3 = df3.set_index(pd.to_datetime(df3['Date Announced']))

df4 = df3.groupby('Detected District').resample('W-Sun', on='Date Announced').sum()
df5 = df3.groupby('Detected District').resample('W-Thu', on='Date Announced').sum()


df6 = df4.groupby(['Date Announced', 'Detected District']).agg(sum)

df7 = df5.groupby(['Date Announced', 'Detected District']).agg(sum)


final = df6.append(df7)


final['timeid'] = final.index

final['districtid'] = final['timeid'].apply(lambda x:x[1])
final['timeid'] = final['timeid'].apply(lambda x:x[0])


final.reset_index(drop=True, inplace=True)
column_names = ['timeid']


final.sort_values('timeid', inplace=True)


for col in column_names:
  final[col], tmp  = pd.Series(list(final[col])).factorize()

final['timeid'] = final['timeid'].apply(lambda x: x+1)


cols = list(final.columns)

final = final[[ 'timeid', 'districtid','Num Cases']]
final.columns = [ 'timeid', 'districtid','cases']


final.reset_index(drop = True, inplace=True)

final.to_csv('case_generator.csv')





####################################question4##############################


import pandas as pd
import numpy as np

df3 = pd.read_csv( "/home/joker/Downloads/Video/SEM1-Downloads/DM/covid_all_Data.csv", low_memory=False)
tbd = [ 'Date Announced', \
       'Detected District',\
         'Num Cases']
df3 = df3[tbd]

df3['Date Announced'] = pd.to_datetime(df3['Date Announced'], format='%d/%m/%Y')

#	Date Announced
#0	30/01/2020


#df3.sort_values('Date Announced', inplace=True)
df3.reset_index(inplace=True, drop=True)


#df3 = df3.loc[102:, :]

df3 = df3[~(df3['Date Announced'] < '2020-03-15')]
df3 = df3[~(df3['Date Announced'] > '2021-08-14')]

#df3.drop(df3[df3['Date Announced'] < '2020-15-03 00:00:00'].index, inplace=True)


#df3['Day'] = df3['Date Announced'].dt.dayofweek



df3['Num Cases'].fillna(0, inplace=True)


df3.dropna(subset=['Date Announced'], inplace=True)

df3.reset_index(inplace=True, drop=True)

#df3['cases'] = df3['Num Cases'].astype(int)

df3.reset_index(drop=True, inplace=True)
df3.isna().sum()







##############
md = df3.copy()

md = md.groupby(['Date Announced', 'Detected District']).agg(sum)

md['Date Announced'] = md.index

md['districtid'] = md['Date Announced'].apply(lambda x:x[1])
md['Date Announced'] = md['Date Announced'].apply(lambda x:x[0])


md.reset_index(drop=True, inplace=True)

md = md[[ 'Date Announced', 'districtid','Num Cases']]
md.columns = [ 'Date Announced', 'districtid','cases']



for i in range(3,9):
    md.loc[((md['Date Announced'] >= '2020-0'+str(i)+'-15') & (md['Date Announced'] <= '2020-0'+str(i+1)+'-14')), 'monthid'] = i-2

md.loc[((md['Date Announced'] >= '2020-09-15') & (md['Date Announced'] <= '2020-10-14')), 'monthid'] = 7


for i in range(10,12):
    md.loc[((md['Date Announced'] >= '2020-'+str(i)+'-15') & (md['Date Announced'] <= '2020-'+str(i+1)+'-14')), 'monthid'] = i-2


md.loc[((md['Date Announced'] >= '2020-12-15') & (md['Date Announced'] <= '2021-01-14')), 'monthid'] = 10

for i in range(1,8):
    md.loc[((md['Date Announced'] >= '2021-0'+str(i)+'-15') & (md['Date Announced'] <= '2021-0'+str(i+1)+'-14')), 'monthid'] = i+10


md['monthid'] = md['monthid'].astype(int)

#md.groupby(['Detected District']).agg(sum)
####################



#f3['Week_Number'] = df3['Date Announced'].dt.week
# Getting year. Weeknum is common across years to we need to create unique index by using year and weeknum
#df3['Year'] = df3['Date Announced'].dt.year


df3 = df3.set_index(pd.to_datetime(df3['Date Announced']))

df4 = df3.groupby('Detected District').resample('W-Sun', on='Date Announced').sum()
df5 = df3.groupby('Detected District').resample('W-Thu', on='Date Announced').sum()


df6 = df4.groupby(['Date Announced', 'Detected District']).agg(sum)

df7 = df5.groupby(['Date Announced', 'Detected District']).agg(sum)


final = df6.append(df7)


final['weekid'] = final.index

final['districtid'] = final['weekid'].apply(lambda x:x[1])
final['weekid'] = final['weekid'].apply(lambda x:x[0])


final.reset_index(drop=True, inplace=True)


final.sort_values('weekid', inplace=True)




final['weekid_num'], tmp  = pd.Series(list(final['weekid'])).factorize()

final['weekid_num'] = final['weekid_num'].apply(lambda x: x+1)


cols = list(final.columns)

final = final[[ 'weekid', 'districtid','Num Cases']]
final.columns = [ 'weekid', 'districtid','cases']


final.reset_index(drop = True, inplace=True)






''' week1 - 21 first wave
109-125 wave 2

month 1-3 wave 1

13-15 wave 2

'''
all_dists = list(set(final['districtid']))

final['Num Cases'] = final['Num Cases'].astype(int)
final_first = final[((final['weekid_num']>=0) & (final['weekid_num']<=21))]
final_second = final[((final['weekid_num']>=109) & (final['weekid_num']<=125))]

md_first = md[((md['monthid']>=1) & (md['monthid']<=3))]
md_second = md[((md['monthid']>=13) & (md['monthid']<=15))]



faltu = set(final_first.districtid) & set(final['districtid'])

out = []
for i in range(len(all_dists)):
    
    try: 
        tmp = {}
        tmp['districtid'] = all_dists[i]
        df_curr =  final_first[final_first['districtid']==all_dists[i]]
        maxx = df_curr['Num Cases'].max()
        tmp['wave1-weekid'] =str(set(df_curr.loc[df_curr['Num Cases']==maxx, 'weekid_num'])).replace('{', '').replace('}', '')
        
        df_curr =  final_second[final_second['districtid']==all_dists[i]]
        maxx = df_curr['Num Cases'].max()
        tmp['wave2-weekid'] =str(set(df_curr.loc[df_curr['Num Cases']==maxx, 'weekid_num'])).replace('{', '').replace('}', '')
 
        df_curr =  md_first[md_first['districtid']==all_dists[i]]
        maxx = df_curr['cases'].max()
        tmp['wave1-monthid'] =str(set(df_curr.loc[df_curr['cases']==maxx, 'monthid'])).replace('{', '').replace('}', '')
        
        df_curr =  md_second[md_second['districtid']==all_dists[i]]
        maxx = df_curr['cases'].max()
        tmp['wave2-monthid'] =str(set(df_curr.loc[df_curr['cases']==maxx, 'monthid'])).replace('{', '').replace('}', '')       
        
        
        
        out.append(tmp)
        
        
        
    except:
        print(all_dists[i])
       
    
    
    
pd.DataFrame(out).replace('set()', 'NA').to_csv('peeks.csv')

###############################################################################################


# =============================================================================
# Question 5   
# districtid, timeid, dose1, dose2.
# =============================================================================
    
import pandas as pd 
dfc = pd.read_csv(r'/home/joker/Downloads/Video/SEM1-Downloads/DM/cowin_vaccine_data_districtwise.csv')
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
        td['dose1'] = dfc.loc[i,rd[j]+'.3']
        td['dose2'] = dfc.loc[i,rd[j]+'.4']
        out.append(td)
    

df = pd.DataFrame(out)

my_df = df.copy()
my_df = my_df[['Date','State_Code', 'District_Key',  'dose1', 'dose2']]
my_df['Date'] = pd.to_datetime(my_df['Date'], format='%d/%m/%Y')
    
   
my_df['dose1'].fillna(0, inplace=True)
my_df['dose2'].fillna(0, inplace=True)    
my_df['dose1'] =    my_df['dose1'].astype(int)
my_df['dose2'] =    my_df['dose2'].astype(int)   

for i in range(1,8):
    my_df.loc[((my_df['Date'] >= '2021-0'+str(i)+'-15') & (my_df['Date'] <= '2021-0'+str(i+1)+'-14')), 'monthid'] = i


my_df['monthid'] = my_df['monthid'].astype(int)

my_df.drop('Date', inplace=True, axis=1)
my_df.drop('State_Code', inplace=True, axis=1)

    
my_df = my_df[['District_Key', 'monthid', 'dose1', 'dose2']]
my_df.columns =    ['districtid', 'monthid', 'dose1', 'dose2'] 

my_df.sort_values('districtid', inplace=True)  

my_df = my_df.groupby(['districtid', 'monthid']).agg('sum')
 
my_df['monthid'] = my_df.index

my_df['districtid'] = my_df['monthid'].apply(lambda x:x[0])
my_df['monthid'] = my_df['monthid'].apply(lambda x:x[1])   
    
    
my_df = my_df[['districtid', 'monthid', 'dose1', 'dose2']]

my_df.reset_index(drop=True, inplace=True)
    
my_df.to_csv('vaccinated-count-month.csv')






# =============================================================================
# weekly
# =============================================================================

wdf = df.copy()

wdf = wdf[['Date','State_Code', 'District_Key',  'dose1', 'dose2']]
wdf['Date'] = pd.to_datetime(wdf['Date'], format='%d/%m/%Y')
    
   
wdf['dose1'].fillna(0, inplace=True)
wdf['dose2'].fillna(0, inplace=True)    
wdf['dose1'] =    wdf['dose1'].astype(int)
wdf['dose2'] =    wdf['dose2'].astype(int) 

wdf.drop('State_Code', inplace=True, axis=1)
   
   
wdf = wdf.set_index(pd.to_datetime(wdf['Date']))

final = wdf.groupby('District_Key').resample('W-Sun', on='Date').agg('sum')


final['weekid'] = final.index

final['districtid'] = final['weekid'].apply(lambda x:x[0])
final['weekid'] = final['weekid'].apply(lambda x:x[1])


final.reset_index(drop=True, inplace=True)


final.sort_values('weekid', inplace=True)


column_names = ['weekid']

for col in column_names:
  final[col], tmp  = pd.Series(list(final[col])).factorize()

final['weekid'] = final['weekid'].apply(lambda x: x+1)



final.sort_values('districtid', inplace=True)  

final = final.groupby(['districtid', 'weekid']).agg('sum')
 
final['weekid'] = final.index

final['districtid'] = final['weekid'].apply(lambda x:x[0])
final['weekid'] = final['weekid'].apply(lambda x:x[1])   
    
    
final = final[['districtid', 'weekid', 'dose1', 'dose2']]

final.reset_index(drop=True, inplace=True)
    



    
final = final[[  'districtid', 'weekid','dose1', 'dose2']]
    
    
final.to_csv('vaccinated-count-week.csv')


# =============================================================================
# =============================================================================
# # state-wise  
# =============================================================================
# =============================================================================
   
    
import pandas as pd 
dfc = pd.read_csv(r'/home/joker/Downloads/Video/SEM1-Downloads/DM/cowin_vaccine_data_districtwise.csv')
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
        td['dose1'] = dfc.loc[i,rd[j]+'.3']
        td['dose2'] = dfc.loc[i,rd[j]+'.4']
        out.append(td)
    

df = pd.DataFrame(out)

my_df = df.copy()
my_df = my_df[['Date','State_Code',  'dose1', 'dose2']]
my_df['Date'] = pd.to_datetime(my_df['Date'], format='%d/%m/%Y')
    
   
my_df['dose1'].fillna(0, inplace=True)
my_df['dose2'].fillna(0, inplace=True)    
my_df['dose1'] =    my_df['dose1'].astype(int)
my_df['dose2'] =    my_df['dose2'].astype(int)   

for i in range(1,8):
    my_df.loc[((my_df['Date'] >= '2021-0'+str(i)+'-15') & (my_df['Date'] <= '2021-0'+str(i+1)+'-14')), 'monthid'] = i


my_df['monthid'] = my_df['monthid'].astype(int)

my_df.drop('Date', inplace=True, axis=1)
#my_df.drop('State_Code', inplace=True, axis=1)

    
my_df = my_df[['State_Code', 'monthid', 'dose1', 'dose2']]
my_df.columns =    ['stateid', 'monthid', 'dose1', 'dose2'] 

my_df.sort_values('stateid', inplace=True)  

my_df = my_df.groupby(['stateid', 'monthid']).agg('sum')
 
my_df['monthid'] = my_df.index

my_df['stateid'] = my_df['monthid'].apply(lambda x:x[0])
my_df['monthid'] = my_df['monthid'].apply(lambda x:x[1])   
    
    
my_df = my_df[['stateid', 'monthid', 'dose1', 'dose2']]

my_df.reset_index(drop=True, inplace=True)
    
my_df.to_csv('state-vaccinated-count-month.csv')
    


# =============================================================================
# =============================================================================
# # WEEKLY    
# =============================================================================
# =============================================================================
    

wdf = df.copy()

wdf = wdf[['Date','State_Code',   'dose1', 'dose2']]
wdf['Date'] = pd.to_datetime(wdf['Date'], format='%d/%m/%Y')
    
   
wdf['dose1'].fillna(0, inplace=True)
wdf['dose2'].fillna(0, inplace=True)    
wdf['dose1'] =    wdf['dose1'].astype(int)
wdf['dose2'] =    wdf['dose2'].astype(int) 

#wdf.drop('State_Code', inplace=True, axis=1)
   
   
wdf = wdf.set_index(pd.to_datetime(wdf['Date']))

final = wdf.groupby('State_Code').resample('W-Sun', on='Date').agg('sum')


final['weekid'] = final.index

final['stateid'] = final['weekid'].apply(lambda x:x[0])
final['weekid'] = final['weekid'].apply(lambda x:x[1])


final.reset_index(drop=True, inplace=True)


final.sort_values('weekid', inplace=True)


column_names = ['weekid']

for col in column_names:
  final[col], tmp  = pd.Series(list(final[col])).factorize()

final['weekid'] = final['weekid'].apply(lambda x: x+1)



final.sort_values('stateid', inplace=True)  

final = final.groupby(['stateid', 'weekid']).agg('sum')
 
final['weekid'] = final.index

final['stateid'] = final['weekid'].apply(lambda x:x[0])
final['weekid'] = final['weekid'].apply(lambda x:x[1])   
    
    
final = final[['stateid', 'weekid', 'dose1', 'dose2']]

final.reset_index(drop=True, inplace=True)
    



    
final = final[[  'districtid', 'weekid','dose1', 'dose2']]
    
    
final.to_csv('vaccinated-count-week.csv')

my_df.to_csv('state-vaccinated-count-week.csv')


# =============================================================================
# =============================================================================
# # overall
# =============================================================================
# =============================================================================

wdf = df.copy()

wdf = wdf[['Date',  'dose1', 'dose2']]
wdf['Date'] = pd.to_datetime(wdf['Date'], format='%d/%m/%Y')
    
   
wdf['dose1'].fillna(0, inplace=True)
wdf['dose2'].fillna(0, inplace=True)    
wdf['dose1'] =    wdf['dose1'].astype(int)
wdf['dose2'] =    wdf['dose2'].astype(int)   




final = wdf.resample('W-Sun', on='Date').agg('max')



final['weekid'] = final.index



final.reset_index(drop=True, inplace=True)


final.sort_values('weekid', inplace=True)


column_names = ['weekid']

for col in column_names:
  final[col], tmp  = pd.Series(list(final[col])).factorize()

final['weekid'] = final['weekid'].apply(lambda x: x+1)

final = final[[  'weekid','dose1', 'dose2']]

final.to_csv("overall-vaccinated-count-week.csv")



# =============================================================================
# =============================================================================
# # monthly
# =============================================================================
# =============================================================================


my_df = df.copy()
my_df = my_df[['Date',  'dose1', 'dose2']]
my_df['Date'] = pd.to_datetime(my_df['Date'], format='%d/%m/%Y')
    
   
my_df['dose1'].fillna(0, inplace=True)
my_df['dose2'].fillna(0, inplace=True)    
my_df['dose1'] =    my_df['dose1'].astype(int)
my_df['dose2'] =    my_df['dose2'].astype(int)   

for i in range(1,8):
    my_df.loc[((my_df['Date'] >= '2021-0'+str(i)+'-15') & (my_df['Date'] <= '2021-0'+str(i+1)+'-14')), 'monthid'] = i


my_df['monthid'] = my_df['monthid'].astype(int)

my_df.drop('Date', inplace=True, axis=1)
#my_df.drop('State_Code', inplace=True, axis=1)

    
my_df = my_df[[ 'monthid', 'dose1', 'dose2']]
my_df.columns =    ['monthid', 'dose1', 'dose2'] 

my_df.sort_values('monthid', inplace=True)  

my_df = my_df.groupby(['monthid']).agg('max')
 
my_df['monthid'] = my_df.index
    
my_df = my_df[['monthid', 'dose1', 'dose2']]

my_df.reset_index(drop=True, inplace=True)
    
my_df.to_csv('overall-vaccinated-count-month.csv')





# =============================================================================
# =============================================================================
# # Question 6    districtid, vaccinationratio, populationratio, ratioof ratios.
# =============================================================================
# =============================================================================
    


import pandas as pd 
dfc = pd.read_csv(r'/home/joker/Downloads/Video/SEM1-Downloads/DM/cowin_vaccine_data_districtwise.csv', low_memory=False)
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
        td['Males'] = dfc.loc[i,rd[j]+'.5']
        td['Females'] = dfc.loc[i,rd[j]+'.6']
        
        out.append(td)
    

df = pd.DataFrame(out)


my_df = df.copy()
my_df = my_df[['District_Key','District', 'Males', 'Females' ]]
#my_df['Date'] = pd.to_datetime(my_df['Date'], format='%d/%m/%Y')
    
   
my_df.dropna(subset=['Males', 'Females'], inplace=True)

my_df['Males'] = my_df['Males'].astype('int')
my_df['Females'] = my_df['Females'].astype('int')


census = pd.read_excel(r'/home/joker/Downloads/Video/SEM1-Downloads/DM/DDW_PCA0000_2011_Indiastatedist.xlsx', \
                       sheet_name='Sheet1')
    
    
census = census[(census['Level']=='DISTRICT') & ((census['TRU']=='Total') )]

census = census[['Name', 'TOT_M', 'TOT_F']]

census.reset_index(inplace=True, drop = True)


common = set(census["Name"]) &  set(my_df['District'])

my_df['District'] = my_df['District'].apply(lambda x: str(x).lower().strip())
census['Name'] = census['Name'].apply(lambda x: str(x).lower().strip())


def corrected_name( x ):
    if(x=="ahmedabad"):
        x = "ahmadabad"
    if(x=="ahmednagar"):
        x = "ahmadnagar"
    if(x=="bagalkote"):
        x = "bagalkot"
        
    if(x=="bandipora"):
        x = "bandipore"
    if(x=="barabanki"):
        x = "bara banki"
    if(x=="buldhana"):
        x = "buldana"
    if(x=="chikkamagaluru"):
        x = "chikmagalur"
    if(x=="chittorgarh"):
        x = "chittaurgarh"
    if(x=="dadra and nagar haveli"):
        x = "dadra & nagar haveli"
    if(x=="darjeeling"):
        x = "darjiling"
    if(x=="dahod"):
        x = "dohad"
    if(x=="gurugram"):
        x = "gurgaon"
    if(x=="haridwar"):
        x = "hardwar"
    if(x=="janjgir champa"):
        x = "janjgir - champa"
    if(x=="kanyakumari"):
        x = "kanniyakumari"
    if(x=="khandwa"):
        x = "khandwa (east nimar)"
    if(x=="khargone"):
        x = "khargone (west nimar)"
    if(x=="kutch"):
        x = "kachchh"
    if(x=="lahaul and spiti"):
        x = "lahul & spiti"
    if(x=="leh"):
        x = "leh(ladakh)"
    if(x=="mahabubnagar"):
        x = "mahbubnagar"
    if(x=="mysuru"):
        x = "mysore"
    if(x=="north 24 parganas"):
        x = "north twenty four parganas"
    if(x=="south 24 parganas"):
        x = "south twenty four parganas"
    if(x=="north and middle andaman"):
        x = "north  & middle andaman"
    if(x=="panchmahal"):
        x = "panch mahals"
    if(x=="shopiyan"):
        x = "shupiyan"
    if(x=="y.s.r. kadapa"):
        x = "y.s.r."
    if(x=="bengaluru urban"):
        x = "bangalore"        
# =============================================================================
#         barabanki bara banki
#         buldhana buldana
#         chikkamagaluru chikmagalur
#         chittorgarh chittaurgarh
#         dadra and nagar haveli dadra & nagar haveli
#         darjeeling darjiling
#         dahod dohad
#         gurugram gurgaon
#         haridwar hardwar
#         janjgir champa janjgir - champa
#         kanyakumari kanniyakumari       
#         khandwa khandwa (east nimar)
#         khargone khargone (west nimar)
#         kutch kachchh
#         lahaul and spiti lahul & spiti
#         leh leh(ladakh)
#         mahabubnagar mahbubnagar
#         mysuru mysore
#         north 24 parganas north twenty four parganas
#         south 24 parganas south twenty four parganas
#         north and middle andaman north  & middle andaman
#         panchmahal panch mahals
#         shopiyan shupiyan
#y.s.r. kadapa  y.s.r.
# =============================================================================
    if(x=="aizwal"):
        x = "aizawl"
    if(x=="rae bareilly"):
        x = "rae bareli"
    if(x=='anugul'):
        x = 'angul'
    if(x=='ashok nagar'):
        x = 'ashoknagar'
    if(x=='badgam'):
        x = 'budgam'
    if(x=='baleshwar'):
        x = 'bageshwar'
    if(x=='banas kantha'):
        x = 'banaskantha'
    if(x=='bangalore rural'):
        x = 'bengaluru rural'
    if(x=='bangalore urban'): 
        x = 'bengaluru urban'
    if(x=='baramula'):
        x = 'baramulla'
    if(x=='baudh'):
        x = 'boudh'
    if(x=='belgaum'):
        x = 'belagavi'
    if(x=='bellary'):
        x = 'ballari'
    if(x=='bemetara'):
        x = 'bametara'
    if(x=='bid'):
        x = 'beed'
    if(x=='bishwanath'):
        x = 'biswanath'
#     if(x=='central delhi'):
#         x = 'delhi'
    if(x=='chamarajanagar'):
        x = 'chamarajanagara'
    if(x=='dantewada'):
        x = 'dakshin bastar dantewada'
    if(x=='debagarh'):
        x = 'deogarh'
    if(x=='devbhumi dwaraka'):
        x = 'devbhumi dwarka'
    if(x=='dhaulpur'):
        x = 'dholpur'
#     if(x=='east delhi'):
#         x = "delhi"
    if(x=='east karbi anglong'):
        x = 'karbi anglong'
    if(x=='faizabad'):
        x = 'ayodhya'
    if(x=='fategarh sahib'):
        x = 'fatehgarh sahib'
    if(x=='firozpur'):
        x = 'ferozepur'
    if(x=='gondiya'):
        x = 'gondia'
    if(x=='hugli'):
        x = 'hooghly'
    if(x=='jagatsinghapur'):
        x = 'jagatsinghpur'
    if(x=='jajapur'):
        x = 'jajpur'
    if(x=='jalor'):
        x = 'jalore'
    if(x=='janjgir-champa'):
        x = 'janjgir champa'
    if(x=='jhunjhunun'):
        x = 'jhunjhunu'
    if(x=='jyotiba phule nagar'):
        x = 'amroha'
    if(x=='kabirdham'):
        x = 'kabeerdham'
    if(x=='kaimur (bhabua)'):
        x = 'kaimur'
    if(x=='kanchipuram'):
        x = 'kancheepuram'
    if(x=='kheri'):
        x = 'lakhimpur kheri'
    if(x=='kochbihar'):
        x = 'cooch behar'
    if(x=='kodarma'):
        x = 'koderma'
    if(x=='komram bheem'):
        x = 'komaram bheem'
    if(x=='konkan division'): #not found
        x = 'konkan division'
    if(x=='lahul and spiti'):
        x = 'lahaul and spiti'
    if(x=='mahesana'):
        x = 'mehsana'
    if(x=='mahrajganj'):
        x = 'maharajganj'
    if(x=='maldah'):
        x = 'malda'
    if(x=='marigaon'):
        x = 'morigaon'
    if(x=='medchal–malkajgiri'):
        x = 'medchal malkajgiri'
    if(x=='muktsar'): #not found
        x = 'sri muktsar sahib'
#     if(x=='mumbai city'):
#         x = 'mumbai'
#     if x== 'mumbai suburban':
#         x = 'mumbai'
    if x== 'nandubar':
        x = 'nandurbar'
    if x== 'narsimhapur':
        x = 'narsinghpur'
    if x== 'nav sari':
        x = 'navsari'
#     if x=='new delhi' :
#         x = 'delhi'
    if x== 'noklak': #not found
        x = 'noklak'
#     if x== 'north delhi':
#         x = 'delhi'
#     if x== 'north east delhi':
#         x = 'delhi'
#     if x== 'north west delhi':
#         x = 'delhi'
    if x== 'pakaur':
        x = 'pakur'
    if x== 'palghat':
        x = 'palghar'
    if x== 'panch mahal':
        x = 'panchmahal'
    if x== 'pashchim champaran':
        x = 'west champaran'
    if x== 'pashchimi singhbhum':
        x = 'west singhbhum'
    if x== 'pattanamtitta':
        x = 'pathanamthitta'
    if x== 'purba champaran':
        x = 'east champaran'
    if x== 'purbi singhbhum':
        x = 'east singhbhum'
    if x== 'puruliya':
        x = 'purulia'
    if x== 'rajauri':
        x = 'rajouri'
    if x== 'rangareddy':
        x = 'ranga reddy'
    if x== 'ri-bhoi':
        x = 'ribhoi'
    if x== 'sabar kantha':
        x = 'sabarkantha'
    if x== 'sahibzada ajit singh nagar':
        x = 's.a.s. nagar'
    if x== 'sait kibir nagar':
        x = 'sant kabir nagar'
    if x== 'sant ravidas nagar':
        x = 'bhadohi'
    if x== 'sepahijala':
        x = 'sipahijala'
    if x== 'seraikela kharsawan':
        x = 'saraikela-kharsawan'
    if x== 'shahdara': #not found
        x = 'shahdara'
    if x== 'shaheed bhagat singh nagar':
        x = 'shahid bhagat singh nagar'
    if x== 'sharawasti':
        x = 'shrawasti'
    if x== 'shimoga':
        x = 'shivamogga'
    if x== 'shopian':
        x = 'shopiyan'
    if x== 'siddharth nagar':
        x = 'siddharthnagar'
    if x== 'sivagangai':
        x = 'sivaganga'
    if x== 'sonapur':
        x = 'subarnapur'
#     if x== 'south delhi':
#         x = 'delhi'
#     if x== 'south east delhi':
#         x = 'delhi'
    if x== 'south salmara-mankachar':
        x = 'south salmara mankachar'
#     if x== 'south west delhi':
#         x = 'delhi'
    if x== 'sri ganganagar':
        x = 'ganganagar'
    if x== 'sri potti sriramulu nellore':
        x = 's.p.s. nellore'
    if x== 'the dangs':
        x = 'dang'
    if x== 'the nilgiris':
        x = 'nilgiris'
    if x== 'thoothukudi':
        x = 'thoothukkudi'
    if x== 'tiruchchirappalli':
        x = 'tiruchirappalli'
    if x== 'tirunelveli kattabo':
        x = 'tirunelveli'
    if x== 'tiruvanamalai':
        x = 'tiruvannamalai'
    if x== 'tumkur':
        x = 'tumakuru'
    if x== 'west delhi':
        x = 'delhi'
    if x== 'yadagiri':
        x = 'yadadri bhuvanagiri'

    return x



census['Name'] = census['Name'].apply(lambda x: corrected_name(str(x)))
my_df['District'] = my_df['District'].apply(lambda x: corrected_name(str(x)))

census.reset_index(inplace=True, drop = True)




common = set(census["Name"]) &  set(my_df['District'])


census_only = set(census.Name) - common
vaccine_only = set(my_df.District) - common

tmp = census['Name'].isin(census_only)
census = census[~tmp]

tmp = my_df['District'].isin(vaccine_only)
my_df = my_df[~tmp]


census.columns = ['District', 'Males', 'Females']
census['Males'] = census['Males'].astype('int')
census['Females'] = census['Females'].astype('int')


my_df = my_df.groupby(['District_Key', 'District']).agg('sum')

my_df['District_Key'] = my_df.index
my_df['District'] = my_df['District_Key'].apply(lambda x: x[1])
my_df['District_Key'] = my_df['District_Key'].apply(lambda x: x[0])


my_df.reset_index(drop = True, inplace=True)

my_df['vaccinationratio'] = my_df['Females']/my_df['Males']
census['populationratio'] = census['Females']/census['Males']


census.drop_duplicates(subset = 'District', keep = 'last', inplace = True)
for i in range(len(my_df)):
    my_df.loc[i,'populationratio'] = \
        list(census[census['District'] == my_df.loc[i,'District']]['populationratio'])

my_df['ratioofratios'] = my_df['vaccinationratio']/my_df['populationratio']

my_df.columns
my_df.drop(['Males', 'Females', 'District'], inplace = True, axis = 1)

my_df.columns = ['districtid', 'vaccinationratio', 'populationratio', 'ratioofratios']

my_df.sort_values('ratioofratios', inplace=True)

my_df.to_csv('vaccination-population-ratio-district.csv')


# =============================================================================
# STate-wise
# =============================================================================


my_df = df.copy()
my_df = my_df[['State','State_Code', 'Males', 'Females' ]]
#my_df['Date'] = pd.to_datetime(my_df['Date'], format='%d/%m/%Y')
    
   
my_df.dropna(subset=['Males', 'Females'], inplace=True)

my_df['Males'] = my_df['Males'].astype('int')
my_df['Females'] = my_df['Females'].astype('int')


my_df = my_df.groupby('State').agg('sum')

my_df['State_Code'] = my_df.index

my_df.reset_index(drop = True, inplace=True)


census = pd.read_excel(r'/home/joker/Downloads/Video/SEM1-Downloads/DM/DDW_PCA0000_2011_Indiastatedist.xlsx', \
                       sheet_name='Sheet1')
    
    
census = census[(census['Level']=='STATE') & ((census['TRU']=='Total') )]

census = census[['Name', 'TOT_M', 'TOT_F']]

census.reset_index(inplace=True, drop = True)
census.columns = ['State', 'Males', 'Females']
my_df.columns = [ 'Males', 'Females', 'State']

for i in range(len(my_df)):
    my_df.loc[i, 'State_Code'] = list(df[df['State'] == my_df.loc[i, 'State']]['State_Code'])[0]

census['State'] = census['State'].apply(lambda x: str(x).lower().replace('&', 'and').strip())
my_df['State'] = my_df['State'].apply(lambda x: str(x).lower().replace('delhi','	nct of delhi' ).strip())

census[census['State'].isin(['daman and diu', 'dadra and nagar haveli'])].sum()

# =============================================================================
# State      daman and diudadra and nagar haveli
# Males                                   344061
# Females                                 242895
# dtype: object
# =============================================================================


census.drop([24,25], inplace = True)
census.reset_index(inplace=True, drop = True)

l = len(census)
census.loc[l, 'State'] = '	dadra and nagar haveli and daman and diu'.strip()

census.loc[l, 'Males'] = 344061
census.loc[l, 'Females'] = 242895


tmp = my_df['State'].isin(census['State'])

my_df = my_df[tmp]

my_df.reset_index(inplace=True, drop = True)



my_df['vaccinationratio'] = my_df['Females']/my_df['Males']
census['populationratio'] = census['Females']/census['Males']


for i in range(len(my_df)):
    my_df.loc[i,'populationratio'] = \
        list(census[census['State'] == my_df.loc[i,'State']]['populationratio'])
        
my_df['ratioofratios'] = my_df['vaccinationratio']/my_df['populationratio']

my_df.columns

overall = my_df.copy()
my_df.drop(['Males', 'Females', 'State'], inplace = True, axis = 1)

my_df.columns = ['stateid', 'vaccinationratio', 'populationratio', 'ratioofratios']

my_df.sort_values('ratioofratios', inplace=True)

my_df.to_csv('vaccination-population-ratio-state.csv')


# =============================================================================
# OVERALL
# =============================================================================


overall_pop = overall['populationratio'].sum() / 34
overall_vac = overall['vaccinationratio'].sum() / 34
overall_rat = overall['ratioofratios'].sum() / 34

tmp_dict = {
    'populationratio' : overall_pop,
    'vaccinationratio' : overall_vac,
    'ratioofratios':overall_rat
    }

df = pd.DataFrame([tmp_dict])

df.to_csv('vaccination-population-ratio-overall.csv')
###############################################################################################################
