#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:28:51 2021

@author: joker
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


na = ['?']
tmp = ["symboling","normalized-losses","make","fuel-type", "aspiration", "num-of-doors", "body-style", \
       "drive-wheels","engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", \
           "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",  "peak-rpm", "city-mpg", "highway-mpg", \
               "price"]



df = pd.read_csv(r"/home/joker/Downloads/Video/SEM1-Downloads/CS771A/assignments/ass1_graded/imports-85.data", header = None, na_values = na,  names= tmp)
#df.columns = tmp
df = df.replace('?', np.nan)

df.fillna(df.mean(), inplace=True)

mode = str(df['num-of-doors'].mode())
df['num-of-doors'].fillna("four", inplace=True)

df.isna().sum()




a = list(df.columns.values)

dummy_cols = [col for col in df.columns if (df.dtypes[col] != np.float64 and df.dtypes[col] != np.int64)]
df = pd.get_dummies(df, columns = dummy_cols)


for d in dummy_cols:
    a.remove(d)

a.remove("price")
    
for col in a:
    maxx = df[col].max()
    minn = df[col].min()
    
    
    df[col] = df[col].apply(lambda x: (x-minn)/(maxx-minn))
    
training_data_u = df.sample(frac=0.8, random_state=25)
testing_data_u = df.drop(training_data_u.index)

validation_data_u = training_data_u.sample(frac=0.25, random_state=25)
training_data_u = training_data_u.drop(validation_data_u.index)



    

'''
symboling             0
normalized-losses    41
make                  0
fuel-type             0
aspiration            0
num-of-doors          2
body-style            0
drive-wheels          0
engine-location       0
wheel-base            0
length                0
width                 0
height                0
curb-weight           0
engine-type           0
num-of-cylinders      0
engine-size           0
fuel-system           0
bore                  4
stroke                4
compression-ratio     0
horsepower            2
peak-rpm              2
city-mpg              0
highway-mpg           0
price                 4

'''


'''

symboling            0
normalized-losses    0
make                 0
fuel-type            0
aspiration           0
num-of-doors         0
body-style           0
drive-wheels         0
engine-location      0
wheel-base           0
length               0
width                0
height               0
curb-weight          0
engine-type          0
num-of-cylinders     0
engine-size          0
fuel-system          0
bore                 0
stroke               0
compression-ratio    0
horsepower           0
peak-rpm             0
city-mpg             0
highway-mpg          0
price                0
dtype: int64
'''


tmp = df["price"]
df.drop("price", axis=1, inplace=True)
df['price'] = tmp

column_names = []
for i in df.columns.values:
    column_names.append(i)


def cross_validate():
# 10 fold cross validation since we are using 10 samples for each k
    final = []
    for k in range(1,15):
        
        rmse = 0
        for r in random.sample(range(20,40), 10):
    
            training_data = df.sample(frac=0.8, random_state=r)
            testing_data = df.drop(training_data.index)
            
            validation_data = training_data.sample(frac=0.25, random_state=r)
            training_data = training_data.drop(validation_data.index)
            
            
            def getPrice(x,ind,k):
                
                out = []
                for i in range(len(training_data)):
                    d = {}
                    d['price'] = training_data.iloc[i, 75]
                    d['distance'] = np.linalg.norm(np.array(x.iloc[ind, 0:75])-np.array(training_data.iloc[i,0:75]), ord=2)
                    
                    
                    out.append(d)
                
                out = sorted(out, key=lambda x:x['distance'])[:k]   
                
                mean = sum(d['price'] for d in out)/k
                return mean
            
            
            def knn(testing, k):
               mse_sum = 0
               for i in range(len(testing)):
                   #print(np.abs(getPrice(testing, i, k) - testing.iloc[i, 15]))
                   mse_sum +=np.abs(getPrice(testing, i, k) - testing.iloc[i, 75])**2
               return np.sqrt(mse_sum/len(testing))               
    
            '''
            
            print(k, knn(testing_data, k))
            rmse["rmse"] = knn(testing_data, k)
            rmse["k"] = k
            final.append(rmse)
            '''
            rmse = rmse + knn(validation_data, k)
            
                
        #
        
        #rmse_df.plot(y='rmse', x='k')
        rmse1 = {}
        rmse_avg = rmse/10
        print(k, rmse_avg)
        rmse1["rmse_avg"] = rmse_avg
        rmse1["k"] = k
        final.append(rmse1)
    
    
    
    rmse_df = pd.DataFrame(final)     
    rmse_df.dtypes
    
    rmse_df.plot(y = "rmse_avg", x = "k")
    
    
cross_validate()
            
#rmse_df.to_csv(r"/home/joker/Downloads/Video/SEM1-Downloads/CS771A/assignments/ass1_graded/123k.csv")
#rmse_df[rmse_df['rmse_avg']==rmse_df['rmse_avg'].min()]['k']
            
'''
1 3872.6893614431547
2 3679.642660559555
3 3595.789663641272
4 3774.438450835982
5 4073.0096915855474
6 4316.241312374587
7 4140.311533631042
8 4041.4907102168
9 4309.241756340013
10 4261.246255444983
11 4230.949538120256
12 4498.180325719729
13 4478.857362706848
14 4658.445844204476
122 8298.75740733874
'''


#cross_validate()


def sub_lists (l):
    lists = [()]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(set(l[j: i]))
    return lists
    
column_idx = [i for i in range(0,75)]
#column_names.remove('price')
perms = sub_lists(column_idx)[1:]

for p in perms:
    p.add(75)
    

    
def getPrice1(x,ind,k, cols):
    #print("gp"*10)  
    
    
    #print( cols)
    out = []
    for i in range(len(training_data)):
        d = {}
        d['price'] = training_data.iloc[i, len(cols)-1]
        #print(d['price'], cols)
        d['distance'] = np.linalg.norm(np.array(x.iloc[ind, :])-np.array(training_data_u.iloc[i, cols]), ord=2)
        
        
        out.append(d)
    
    out = sorted(out, key=lambda x:x['distance'])[:k]   
    
    mean = sum(d['price'] for d in out)/k
    return mean


def knn1(testing, k, cols):
   mse_sum = 0
   #print(cols)
   for i in range(len(testing)):
       #print(np.abs(getPrice(testing, i, k) - testing.iloc[i, 15]))
       mse_sum +=np.abs(getPrice1(testing, i, k, cols) - testing.iloc[i, len(cols)-1])**2
     
   #print("@"*100)     
   return np.sqrt(mse_sum/len(testing))   

k = 3 #learnt from CV
final_cols = []



for i in range(len(perms)):
    #print(perms[i])
    df1 = df.iloc[:,list(perms[i])]
    #print(df1.head())
    #print(df1.head())
    '''
    b = len(df1.columns)-1
    print(b)
    tmp = df1.iloc[:, b]
    df1.drop(df1.columns[[b]], axis=1, inplace=True)
    df1.iloc[:, b] = tmp
    
    break 
    '''   
    training_data = df1.sample(frac=0.8, random_state=25)
    testing_data = df1.drop(training_data.index)
    
    validation_data = training_data.sample(frac=0.25, random_state=25)
    training_data = training_data.drop(validation_data.index)
    
    #print(training_data.head())
    #print(testing_data.head())
    #print(validation_data.head())

    
    #print("-"*100)
    alpha = {}
    alpha['columns'] = perms[i]
    alpha['rmse'] = knn1(validation_data, k, list(perms[i]))
    final_cols.append(alpha)
    print(i+1)
    
    

   
x = ['price', 'length', 'width']
print(training_data[[c for c in training_data.columns if c in x]])
    
'''

print(k, knn(testing_data, k))
rmse["rmse"] = knn(testing_data, k)
rmse["k"] = k
final.append(rmse)
'''
    
df.iloc[:, 45]
l0_df = pd.DataFrame(final_cols)

l0_df.to_csv(r"/home/joker/l0.csv")


for i in range(len(df.columns.values)):
    print(str(i)+','+str(df.columns.values[i]))