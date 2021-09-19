#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:52:14 2021

@author: pranshu
"""

import json
import pandas as pd



with open(r'neighbor-districts.json') as f:
    
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

dfc = pd.read_csv(r'cowin_vaccine_data_districtwise.csv', low_memory=False)


hatao = ['chirang','peddapalli','rajanna sircilla']
tmp = df1['district'].isin(hatao)

df1.reset_index(inplace=True, drop=True)

for h in hatao:
    
    for k in range(len(df1)):
         if h in df1.loc[k, 'neighbours'].split(','):
             new_cols =  df1.loc[k, 'neighbours'].split(',')
             new_cols.remove(h)
             
             for n in new_cols:
                 n = n.strip()
             #print(new_cols)
             df1.loc[k, 'neighbours'] = ','.join(new_cols).replace('[]', '')


df1 = df1[~tmp]

df1.reset_index(inplace=True, drop=True)



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

dfc = dfc[['District_Key', 'District', 'State_Code']]

cowid_districts = dfc['District']


dfd = pd.read_csv(r'districts.csv')

dfd = dfd[['District']]
dfd['District'] = dfd['District'].apply(lambda x: str(x).lower())
vaccine_districts = dfd['District']
# =============================================================================
# 
# for d in vaccine_districts[:10]:
#     print(d)
# =============================================================================


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
# =============================================================================
#             print(curr)
#             print('\n')
# =============================================================================
            df1.drop(df1[df1['district']==curr].index, inplace=True)


       # print("error", i)

            df1.reset_index(inplace=True, drop=True)
    
            for k in range(len(df1)):
                 if curr in df1.loc[k, 'neighbours'].split(','):
                     new_cols =  df1.loc[k, 'neighbours'].split(',')
                     new_cols.remove(curr)
                     
                     for n in new_cols:
                         n = n.strip()
                     print(new_cols)
                     df1.loc[k, 'neighbours'] = ','.join(new_cols).replace('[]', '')
            
            #df1.reset_index(inplace=True, drop=True)
    except :
        pass       
            
df1.reset_index(inplace=True, drop=True)

#df1[df1['district'].str.contains('champaran')]




common_dist = set(df1['district'] ) &set(cowin_districts) 

dfc_only = set(cowin_districts) - common_dist
df1_only = set(df1['district']) - common_dist
'''
def combine(city):
    print(city)
    all_city = list(df1[df1['district'].str.contains(city)]['district'])
   # print(all_city)
    neighbours = list()
    for d in all_city:
        tmp = str(df1[df1['district']==d]['neighbours'].values[0]).split(', ')
        neighbours.extend(tmp)
        df1.drop(df1[df1['district']==d].index, inplace=True)
    
        #print(tmp, type(tmp))
    neighbours = set(neighbours) - set(all_city)
    print(neighbours)
    print(all_city)
    tmp_dict = {}
    tmp_dict['district'] = all_city[0]
    tmp_dict['neighbours'] = str(neighbours).replace('{', '').replace('}', '').replace("'", '')
   # print(tmp_dict)
    df1.reset_index(inplace=True, drop=True)

    
    df1.loc[len(df1.index)] = tmp_dict
    df1.reset_index(inplace=True, drop=True)
    
    
list(df1[df1['district'].str.contains('delhi')]['district'])
combine('delhi')

#df1.drop(df1[df1['district']=='delhi'].index, inplace=True)


#df1[df1['district'].str.contains( 'south')]['district']
tbc = ['delhi','champaran', 'sikkim', 'singhbhum', '24 parganas', \
        'goa',  'karbi anglong', 'tripura', 'godavari', \
           'jaintia hills', 'siang', 'kameng', 'garo hills', \
           'khasi hills', 'imphal', 'mumbai', 'warangal', 'kanpur' ]

for t in tbc:
    try:
        combine(t)
        print("merged ", t)
    except:
        print("can't merge ", t)

#combine('mumbai')

#dfc[dfc['District']==df1.loc[721, 'district']]['District_Key'].values[0]
df1.reset_index(inplace=True, drop=True)

'''


#tbd = ['district']
# =============================================================================

# =============================================================================

#df1.drop(tbd, inplace=True, axis = 1)


df1.reset_index(inplace=True, drop=True)


dcodes = pd.read_csv( "district_wise.csv", low_memory=False)
dcodes  = dcodes[['District', 'District_Key', 'State_Code']]

tmp = dcodes['District'].isin(['Unassigned', 'Unknown', 'Other State'])
dcodes = dcodes[~tmp]

dcodes['District'] = dcodes['District'].apply(lambda x: str(x).split('/')[0].lower().replace('_district', '').replace('_', ' '))




tbd = []
for i in range(len(df1)):
     try:
         df1.loc[i, 'districtid'] = dcodes[dcodes['District']==df1.loc[i, 'district']]['District_Key'].values[0]
         df1.loc[i, 'stateid'] = dcodes[dcodes['District']==df1.loc[i, 'district']]['State_Code'].values[0]
     except:
         tbd.append(i)
         print(i)


for j in range(len(df1)):
    try:
        tmp = df1.loc[j, 'neighbours'].split(',')
        for i in range(len(tmp)):
           tmp[i] = dfc[dfc['District']==tmp[i]]['District_Key'].values[0] 
        df1.loc[j, 'neighbours'] = ','.join(tmp).replace('[]', '')
        #print(tmp)
    except:
        pass
    
df1.drop(tbd, inplace = True)

df1 = df1[['stateid', 'districtid', 'neighbours']]

df1.sort_values(['stateid', 'districtid'], inplace=True)

#dfc[dfc['District']==df1.loc[0, 'district']]['District_Key'].values[0]
df1.to_json('output/neighbor-districts-modified.json', orient='records', lines=True)

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
        curr = df1.loc[i, 'districtid']
        #print(curr, '\n')
        #print(curr)
        #print(df1.loc[i, 'neighbours'].split(','))
        n_l = df1.loc[i, 'neighbours'].split(',')
        
        for j in range(len(n_l)):
            n_l[j] = n_l[j].strip()
            tmp = {}
            tmp['districtid'] = curr
            tmp['neighbourid'] =  n_l[j]
            if(check(out, {'districtid':  n_l[j], 'neighbourid': curr}) == False):
                
                out.append(tmp)


    except:
        pass
    
        #print(curr)
    
        
df2 = pd.DataFrame(out) 

df2.to_csv('output/edge_list.csv', index=False)


