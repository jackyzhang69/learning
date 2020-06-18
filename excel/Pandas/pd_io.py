import pandas as pd 

data=pd.read_excel('noc_list.xlsx')
#print(data)
# data.to_pickle('2019.pickle')
data.to_json('2019.json')

# d1=pd.read_pickle('2019.pickle')
d2=pd.read_json('2019.json')
print(d2)