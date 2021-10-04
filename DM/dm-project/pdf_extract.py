
import os 
os.chdir(r'/home/pranshu/Documents/GitHub/MTech/DM/dm-project/')


import camelot

# extract all the tables in the PDF file


files = os.listdir('2021')

for f in files:
    
    abc = camelot.read_pdf('2021/'+f, pages="all") #address of file loation
    print(len(abc))
# print the first table as Pandas DataFrame
df1 = abc[0].df
df2 = abc[1].df

for i in range(0,12):
    print(abc[i].df) 