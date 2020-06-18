import matplotlib.pyplot as plt
import numpy as np
import csv
import urllib
import matplotlib.dates as mdates

# 1. loading from file
# 传统方法
# x=[]
# y=[]
# with open('example.txt','r') as csvfile:
#     plots=csv.reader(csvfile,delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))

# numpy way
x,y=np.loadtxt('example.txt',delimiter=',',unpack=True)

plt.plot(x,y)
plt.title('Graph')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend([])
plt.show()      

