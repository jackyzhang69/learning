import pandas as pd 

data=pd.read_excel("noc_list.xlsx",index_col=None,)
d=data[(data.Noc>=11) & (data.Noc<=1111)]
print(d.Title)
