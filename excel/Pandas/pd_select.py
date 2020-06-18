import numpy as np
import pandas as pd

dates=pd.date_range('20200101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

# 选择数据
print(df['A'],df.A) # 选择一列，2个方式都可以
print(df.loc['20200102'])   #选择一行
print(df.loc[:,['A','B']]) # 选择所有行，列是A和B. :前后没有索引表示所有
print(df.loc['2020-01-02',['A','B']]) # 选择一行，2列
#print(df.loc[['2020-01-02','2020-01-04'],['A','B']]) #这个不行？

# selct by position: iloc
print(df.iloc[3:5,1:4])  # 选取index从3-5的行，就是第4到第5行。
print(df.iloc[[1,3,5],1:4])

# mixed selection ix
# print(df.ix[:3,['A','B']]) #版本不支持了。

# Boolen indexing
print(df)
print(df[df.A>=8])
