#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 05:49:23 2021

@author: pranshu
"""


import pandas as pd 
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


census = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx', \
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


my_df = my_df.groupby(['District_Key', 'District']).agg('max')

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

my_df.to_csv('output/districtid-vaccination-population-ratio.csv', index=False)


# =============================================================================
# STate-wise
# =============================================================================

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
my_df = my_df[['State','State_Code', 'Males', 'Females' ]]
#my_df['Date'] = pd.to_datetime(my_df['Date'], format='%d/%m/%Y')
    
   
my_df.dropna(subset=['Males', 'Females'], inplace=True)

my_df['Males'] = my_df['Males'].astype('int')
my_df['Females'] = my_df['Females'].astype('int')


my_df = my_df.groupby('State').agg('max')

my_df['State_Code'] = my_df.index

my_df.reset_index(drop = True, inplace=True)


census = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx', \
                       sheet_name='Sheet1')
    
    
census = census[(census['Level']=='STATE') & ((census['TRU']=='Total') )]

census = census[['Name', 'TOT_M', 'TOT_F']]

census.reset_index(inplace=True, drop = True)
census.columns = ['State', 'Males', 'Females']
my_df.columns = ['State', 'Males', 'Females']

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

my_df.to_csv('output/stateid-vaccination-population-ratio.csv', index=False)


# =============================================================================
# OVERALL
# =============================================================================


overall_pop = overall['populationratio'].sum() / 34
overall_vac = overall['vaccinationratio'].sum() / 34
overall_rat = overall['ratioofratios'].sum() / 34

tmp_dict = {
    'vaccinationratio' : overall_vac,
    'populationratio' : overall_pop,
    
    'ratioofratios':overall_rat
    }

df = pd.DataFrame([tmp_dict])

df.to_csv('output/overall-vaccination-population-ratio.csv', index=False)
###############################################################################################################
