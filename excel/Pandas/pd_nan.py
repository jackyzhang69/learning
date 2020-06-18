import numpy as np
import pandas as pd 

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan

# 检查是否有NaN
print(np.any(df.isnull())==True)

# 删除NaN数据
ddf=df.dropna(axis=0,how='any')  # axis=0, 删除行，1 列。 how=any or all.
print(ddf)

# 填充NaN数据
ddf=df.fillna(value=0)
print(ddf)


