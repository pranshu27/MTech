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
dfc = pd.read_csv(r'cowin_vaccine_data_districtwise.csv',  low_memory=(False))
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
        td['Cowin_Key'] = dfc.loc[i, 'Cowin Key']
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
my_df['dose1'] = my_df['dose1'].astype(int)
my_df['dose2'] = my_df['dose2'].astype(int)   


my_df.sort_values(['State_Code','District_Key','Date'], inplace = True)



my_df = my_df.groupby(['State_Code','District_Key'])

later = pd.DataFrame()
for district, district_df in my_df:

    temp = district_df.shift(1)
    temp.fillna(0,inplace=True)
    district_df['dose1'] = district_df['dose1'] - temp['dose1']
    district_df['dose2'] = district_df['dose2'] - temp['dose2']
    district_df.set_index('Date',inplace=True)
#     print(district_df)
    later = later.append(district_df)




my_df = later.copy()

my_df['Date'] = my_df.index


my_df['Date'] = pd.to_datetime(my_df['Date'], format='%Y-%m-%d')

# =============================================================================
# my_df['dose1'].apply(lambda x: 0 if x<0 else x)
# my_df['dose1'].apply(lambda x: 0 if x<0 else x)
# =============================================================================

wdf = my_df.copy()

for i in range(1,8):
    my_df.loc[((my_df['Date'] >= '2021-0'+str(i)+'-15') & (my_df['Date'] <= '2021-0'+str(i+1)+'-14')), 'monthid'] = i


my_df['monthid'] = my_df['monthid'].astype(int)

my_df.drop('Date', inplace=True, axis=1)
#my_df.drop('State_Code', inplace=True, axis=1)

    
my_df = my_df[['District_Key', 'monthid', 'dose1', 'dose2']]
my_df.columns =    ['districtid', 'monthid', 'dose1', 'dose2'] 

my_df.sort_values(['districtid', 'monthid'], inplace=True)  

my_df = my_df.groupby(['districtid', 'monthid']).agg('sum')
 
my_df['monthid'] = my_df.index

my_df['districtid'] = my_df['monthid'].apply(lambda x:x[0])
my_df['monthid'] = my_df['monthid'].apply(lambda x:x[1])   
    
    
my_df = my_df[['districtid', 'monthid', 'dose1', 'dose2']]

my_df.reset_index(drop=True, inplace=True)
    

# =============================================================================
# all_cities = my_df.districtid.unique()
# 
# out =[]
# 
# defected = []
# for city in all_cities:
#     try:
#         
#         tmp = my_df[my_df['districtid']==city].copy()
#         tmp.sort_values(['districtid', 'monthid'], inplace = True)
#         tmp.reset_index(inplace=True, drop=True)
#         #print(tmp)
#         #print(tmp)
#         #print(tmp)
#         for i in range(len(tmp)-1,0, -1):
#             #tmp.loc[]
#             #print('here')
#             tmp.loc[i, 'dose1'] -= tmp.loc[i-1, 'dose1']
#             tmp.loc[i, 'dose2'] -= tmp.loc[i-1, 'dose2']
#     except:
#         defected.append(city)
# 
#        # pass
#    # tmp.drop([len(tmp)-2, len(tmp)-1], inplace = True, axis = 0)
#     #print(tmp)
#     #print(tmp)
#     out.append(tmp)
#     
# 
# 
# my_df = pd.concat(out, ignore_index=True)
# =============================================================================
my_df.reset_index(drop=True, inplace=True)

my_df.sort_values('districtid', inplace = True)

my_df.to_csv('output/district-vaccinated-count-month.csv', index = False)

print('district-vaccinated-count-month.csv')


# =============================================================================
# weekly
# =============================================================================

   
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
final.sort_values('districtid', inplace = True)

final.to_csv('output/district-vaccinated-count-week.csv', index = False)
    
print('district-vaccinated-count-week.csv')    


# =============================================================================
# =============================================================================
# # state-wise  
# =============================================================================
# =============================================================================
   
my_df1 = my_df.copy()
my_df1['stateid'] = my_df1['districtid'].apply(lambda x: str(x).split('_')[0])
my_df1.drop('districtid', axis = 1, inplace = True)
my_df1 = my_df1.groupby(['stateid', 'monthid']).agg('sum')


my_df1['monthid'] = my_df1.index
my_df1['stateid'] =my_df1['monthid'].apply(lambda x: x[0])

my_df1['monthid'] =my_df1['monthid'].apply(lambda x: x[1])

my_df1 = my_df1[['stateid', 'monthid', 'dose1', 'dose2']]

my_df1.reset_index(drop=True, inplace=True)

my_df1.sort_values('stateid', inplace = True)
my_df1.to_csv('output/state-vaccinated-count-state.csv', index = False)
    
print('state-vaccinated-count-state.csv')    
  


# =============================================================================
# =============================================================================
# # WEEKLY    
# =============================================================================
# =============================================================================
    

final1 = final.copy()

final1['stateid'] = final1['districtid'].apply(lambda x: str(x).split('_')[0])
final1.drop('districtid', axis = 1, inplace = True)
final1 = final1.groupby(['stateid', 'weekid']).agg('sum')


final1['weekid'] = final1.index
final1['stateid'] =final1['weekid'].apply(lambda x: x[0])

final1['weekid'] =final1['weekid'].apply(lambda x: x[1])

final1 = final1[['stateid', 'weekid', 'dose1', 'dose2']]
final1.reset_index(drop=True, inplace=True)

final1.sort_values('stateid', inplace = True)

final1.to_csv('output/state-vaccinated-count-week.csv', index = False)

print('state-vaccinated-count-week.csv')


# =============================================================================
# =============================================================================
# # overall
# =============================================================================
# =============================================================================
final2 = final1.copy()


final2.reset_index(drop=True, inplace=True)

final2.drop('weekid', inplace=True, axis = 1)

final2 = final2.groupby('stateid').agg('sum')

final2['stateid'] = final2.index

final2.reset_index(drop=True, inplace=True)

final2 = final2[['stateid', 'dose1', 'dose2']]
final2.reset_index(drop=True, inplace=True)

final2.sort_values('stateid', inplace = True)

final2.to_csv('output/state-vaccinated-count-overall.csv', index = False)

print('state-vaccinated-count-overall.csv')



# =============================================================================
# =============================================================================
# # monthly
# =============================================================================
# =============================================================================

    
my_df2 = final.copy()
my_df2.reset_index(drop=True, inplace=True)

my_df2.drop('weekid', inplace=True, axis = 1)


my_df2 = my_df2.groupby('districtid').agg('sum')

my_df2['districtid'] = my_df2.index

my_df2.reset_index(drop=True, inplace=True)

my_df2 = my_df2[['districtid', 'dose1', 'dose2']]

my_df2.sort_values('districtid', inplace = True)
my_df2.to_csv('output/district-vaccinated-count-overall.csv', index = False)

print('district-vaccinated-count-overall.csv')



