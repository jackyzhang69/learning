import numpy as np
import pandas as pd 

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[2,2]=1111
print(df)

#df.A[df.A>4]=0 # A列中A>4的改为0
df.B[df.A>4]=0 # B列中A>4的改为0
print(df)

# 增加一列
df['F']=np.nan
print(df)

df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('2013-01-01',periods=6))
print(df)