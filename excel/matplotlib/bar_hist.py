import pandas as pd 
from matplotlib import pyplot as plt

x=[2,4,6,8,10]
y=[8, 12, 4,9,18]
x1=[1,3,5,7,9]
y1=[3,7,9,12,14]

plt.bar(x,y,label='Bars',color='blue')
plt.bar(x1,y1,label='Bars2',color='red')
plt.title('Graph')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend([])
plt.show()


population_ages=[1, 2,44,58,19,22,34,56,78,97,110,131,123,12,45,23,43,55,67,12,28,33,33,34,67]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype="bar",rwidth=0.8)
plt.show()