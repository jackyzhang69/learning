import pandas as pd 
from matplotlib import pyplot as plt

# scatter
x=[2,4,6,8,10]
y=[8, 12, 4,9,18]

plt.scatter(x,y,label='skitscat',color='k', marker='o',s=100) # s is size, marker is shape
plt.title('Graph')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend([])
plt.show()

# stack
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,10,7,6]
playing=[3,4,6,4,3]

plt.stackplot(days,sleeping,eating,working,playing,colors=['red','green','blue','grey'])
plt.legend(['sleeping','eating','working','playing'])
plt.show()

# Pie
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,10,7,6]
playing=[3,4,6,4,3]

slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']
plt.pie(slices,labels=activities,colors=cols, explode=(0.1,0.1,0.3,0.1), startangle=90,autopct='%1.1f%%')
plt.legend(['sleeping','eating','working','playing'])
plt.show()
