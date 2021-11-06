import numpy as np
import pandas as pd
dict1={"name":['a','b','c','d'],"marks":[100,50,60,70],"city":['x','y','z','q']}
# print(dict1)
df=pd.DataFrame(dict1)
print(df)
df.to_excel('panda1.xlsx',index=False)
print(df)
#print first two index of df
print(df.head(2))
#print last two index of df
print(df.tail(2))
#statistical analysis of numerical data
print(df.describe())
#reading data from a csv file
temp=pd.read_csv('test.csv')
print(temp)
print(temp['price'][0])
#custom indexing
temp.index=['i','ii','iii','iv']
print(temp)