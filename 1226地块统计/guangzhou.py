# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/12/26 21:17'
import pandas as pd
with open('haizhu.csv','r+',encoding='utf-8') as f:
    df1 = pd.read_csv(f,header=None, index_col = None,engine='python')#names=range(2,6),

print(df1.index)
#groupby_regiment = df1[0].groupby(df['regiment'])
df1[1] = df1.index

mat=df1.values
print(mat)
feature=list(set(mat[:,0].tolist()))

road=list(set(mat[:,1].tolist()))

import numpy as np
x = np.empty([len(feature),len(road)], dtype = int)
print (x)

print(df1[0])
#for index, value in enumerate(numbers)
for indexi,i in enumerate(feature):
    tmp_road = df1[df1[0] == i].values[:, 1].T.tolist()
    print(tmp_road)
    for indexj, j in enumerate(road):
        x[indexi,indexj]=tmp_road.count(j)
print(x)
pddata=pd.DataFrame(x)

print('###')
print(feature)
print(road)
pddata.to_csv('test.csv')

#https://www.jianshu.com/p/a213384a0dbf