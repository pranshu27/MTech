#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 04:49:04 2021

@author: pranshu
"""


###############################################################################################


# =============================================================================
# Question 5   
# districtid, timeid, dose1, dose2.
# =============================================================================
    
import pandas as pd 
dfc = pd.read_csv(r'data/cowin_vaccine_data_districtwise.csv')
dfc = dfc.loc[1:, :]
dfc.reset_index(drop=True, inplace=True)


    
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
    

all_cities = my_df.districtid.unique()

out =[]

defected = []
for city in all_cities:
    try:
        
        tmp = my_df[my_df['districtid']==city].copy()
        tmp.sort_values(['districtid', 'monthid'], inplace = True)
        tmp.reset_index(inplace=True, drop=True)
        #print(tmp)
        #print(tmp)
        #print(tmp)
        for i in range(len(tmp)-1,0, -1):
            #tmp.loc[]
            #print('here')
            tmp.loc[i, 'dose1'] -= tmp.loc[i-1, 'dose1']
            tmp.loc[i, 'dose2'] -= tmp.loc[i-1, 'dose2']
    except:
        defected.append(city)

       # pass
   # tmp.drop([len(tmp)-2, len(tmp)-1], inplace = True, axis = 0)
    #print(tmp)
    #print(tmp)
    out.append(tmp)
    


my_df = pd.concat(out, ignore_index=True)
my_df.to_csv('output/month-district-vaccinated-count-time.csv', index = False)




# =============================================================================
# weekly
# =============================================================================


per1 = pd.date_range(start ='16-01-2021', \
         end ='15-08-2021', freq ='D')
    
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


out =[]

defected = []
for city in all_cities:
    try:
        
        tmp = final[final['districtid']==city].copy()
        tmp.sort_values(['districtid', 'weekid'], inplace = True)
        tmp.reset_index(inplace=True, drop=True)
        #print(tmp)
        #print(tmp)
        #print(tmp)
        for i in range(len(tmp)-1,0, -1):
            #tmp.loc[]
            #print('here')
            tmp.loc[i, 'dose1'] -= tmp.loc[i-1, 'dose1']
            tmp.loc[i, 'dose2'] -= tmp.loc[i-1, 'dose2']
        
    except:
        defected.append(city)
    
       # pass
   # tmp.drop([len(tmp)-2, len(tmp)-1], inplace = True, axis = 0)
    #print(tmp)
    #print(tmp)
    out.append(tmp)
    


final = pd.concat(out, ignore_index=True)
final.to_csv('output/week-district-vaccinated-count-time.csv', index = False)
    
    


# =============================================================================
# =============================================================================
# # state-wise  
# =============================================================================
# =============================================================================
   
    
import pandas as pd 
dfc = pd.read_csv(r'data/cowin_vaccine_data_districtwise.csv')
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

all_states = my_df.stateid.unique()

out =[]

defected = []
for city in all_states:
    try:
        
        tmp = my_df[my_df['stateid']==city].copy()
        tmp.sort_values(['stateid', 'monthid'], inplace = True)
        tmp.reset_index(inplace=True, drop=True)
        #print(tmp)
        #print(tmp)
        #print(tmp)
        for i in range(len(tmp)-1,0, -1):
            #tmp.loc[]
            #print('here')
            tmp.loc[i, 'dose1'] -= tmp.loc[i-1, 'dose1']
            tmp.loc[i, 'dose2'] -= tmp.loc[i-1, 'dose2']
    except:
        defected.append(city)

       # pass
   # tmp.drop([len(tmp)-2, len(tmp)-1], inplace = True, axis = 0)
    #print(tmp)
    #print(tmp)
    out.append(tmp)
    


my_df = pd.concat(out, ignore_index=True)
my_df.to_csv('output/month-state-vaccinated-count-time.csv', index = False)
    
    


# =============================================================================
# =============================================================================
# # WEEKLY    
# =============================================================================
# =============================================================================
    

per1 = pd.date_range(start ='16-01-2021', \
         end ='15-08-2021', freq ='D')
    
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
    



    
final = final[[  'stateid', 'weekid','dose1', 'dose2']]
    
all_states = final.stateid.unique()

out =[]

defected = []
for city in all_states:
    try:
        
        tmp = final[final['stateid']==city].copy()
        tmp.sort_values(['stateid', 'weekid'], inplace = True)
        tmp.reset_index(inplace=True, drop=True)
        #print(tmp)
        #print(tmp)
        #print(tmp)
        for i in range(len(tmp)-1,0, -1):
            #tmp.loc[]
            #print('here')
            tmp.loc[i, 'dose1'] -= tmp.loc[i-1, 'dose1']
            tmp.loc[i, 'dose2'] -= tmp.loc[i-1, 'dose2']
    except:
        defected.append(city)

       # pass
   # tmp.drop([len(tmp)-2, len(tmp)-1], inplace = True, axis = 0)
    #print(tmp)
    #print(tmp)
    out.append(tmp)
    


final = pd.concat(out, ignore_index=True)
final.to_csv('output/week-state-vaccinated-count-time.csv', index = False)


# =============================================================================
# =============================================================================
# # overall
# =============================================================================
# =============================================================================
per1 = pd.date_range(start ='16-01-2021', \
         end ='15-08-2021', freq ='D')
    
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

for i in range(len(final)-1,0, -1):
    #tmp.loc[]
    #print('here')
    final.loc[i, 'dose1'] -= final.loc[i-1, 'dose1']
    final.loc[i, 'dose2'] -= final.loc[i-1, 'dose2']

final.to_csv('output/week-overall-vaccinated-count-time.csv', index = False)



# =============================================================================
# =============================================================================
# # monthly
# =============================================================================
# =============================================================================

    
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
    
for i in range(len(my_df)-1,0, -1):
    #tmp.loc[]
    #print('here')
    my_df.loc[i, 'dose1'] -= my_df.loc[i-1, 'dose1']
    my_df.loc[i, 'dose2'] -= my_df.loc[i-1, 'dose2']

my_df.to_csv('output/month-overall-vaccinated-count-time.csv', index = False)



