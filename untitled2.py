# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:18:13 2023

@author: gowtham reddy
"""
import pandas as pd

#Standard way creating a dataframe

df = pd.DataFrame({"Name": ["Gowtham","Satwik","virat"],
                   "Age": [20,20, 58],
                   "Sex": ["male", "male", "female"], })
# dict keys will be column names in the df
# the list of values beside keys will be entries under the same column
# creating row labels using index parameter
df1=pd.DataFrame({'Gowtham': ['I liked it.', 'It was awful.'], 
              'Sathwik': ['Pretty good.', 'Very bad.']},
             index=['Product A', 'Product B'])
df1

#creating a series 
df2=pd.Series([1, 2, 3, 4, 5])
print(df2)

# using index parameter and name paramter to name series
df3=pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(df3)
df4=pd.read_csv("top100.csv")
print(df4)
df4.shape
df5=df4.head(6)
df6=pd.read_csv("top100.csv",index_col=0)
print(df6)


#native accesors
# accesing values in a columns using object.attribute method
df7=pd.read_csv("top100.csv")
df8=df7.name

# other way to access column data is by using df8["column_name"]
df9=df7["name"]

f1=df7["name"][0]


"""
Accessors in pandas


The first is index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.
To select the first row of data in a DataFrame, we use the following:"""

f2=df7.iloc[1]


f3=df7.iloc[:, 0]
f4=df7.iloc[:3, 0]
f5=df7.iloc[1:3, 0]
f6=df7.iloc[[0, 1, 2], 0]
f7=df7.iloc[-5:]


"""Label-based selection
The second paradigm for attribute selection is the one followed by the loc operator: label-based selection. In this paradigm, it's the data index value, not its position, which matters.

For example, to get the first entry in top100 songs, we would now do the following:"""
f8=df7.loc[[0,1,2], 'name']


#manupulating index
f9=df7.set_index("id")


#conditional selection
f10=df7.duration<3.00
f11=df7.loc[f10]

#multiple conditions
f12=df7.energy>0.5
f13=df7.loc[f10&f12]
#similarly can use | operator


# assigning operator
#df7[id]="0"

#Or with an iterable of values:
#reviews['index_backwards'] = range(len(reviews), 0, -1)



#summary functions 
#describe (its typeaware)
f14=df7.duration.describe()
f15=df7.id.describe()

#returns mean of all values
f16=df7.duration.mean()

f17=df7.duration.unique()

f18=df7.id.value_counts()


#Maps
#using Map() function
#using apply() function
f19=df7.duration.map(lambda p: p+1)#ad of 1 min 




































"""
c=df.at[0,"Name"]
print(c)

d=df.iat[0,1]
print(d)

df["Age"]
df["Age"].max()
df.describe()

a=pd.read_csv('top100.csv')
b=a.to_json()
c=a.to_numpy()
print(c)

a=pd.read_csv('top100.csv')
a.info()
e=a.dtypes

a=pd.read_csv('top100.csv')
b=a[["name","duration"]]
e=b.head()
f=b.tail()
print(a.iloc[9:25, 2:5])

import matplotlib.pyplot as plt
a.iloc[9:25, 2:5].plot()"""






