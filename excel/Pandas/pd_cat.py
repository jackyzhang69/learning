import pandas as pd 
import numpy as np

# concatenating
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

print(df1)
print(df2)
print(df3)

res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)  # axis=0 表示纵向合并，增加rows。 1 横向，增加columns
print(res)

# join, ['inner','outer']
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)

res1=pd.concat([df1,df2],join='outer',ignore_index=True) #默认就是outer模式 ignore_index可以控制index变成连续
res2=pd.concat([df1,df2],join='inner') 
print(res1)
print(res2)
# join_axes
res=pd.concat([df1,df2],axis=1) # 以df1的index作为基础
print(res)

# append
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])

res=df1.append([df2,df3],ignore_index=True)
print(res)

print("s1 below")
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df1.append(s1,ignore_index=True) # 添加一行 Series

print(res)
