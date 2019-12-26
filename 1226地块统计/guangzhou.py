# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/12/26 21:17'
import pandas as pd
with open('天河区市政设施统计.csv','r+',encoding='utf-8') as f:
    df1 = pd.read_csv(f,header=None, engine='python')

#groupby_regiment = df1[0].groupby(df['regiment'])

mat=df1.values
feature=list(set(mat[:,0].tolist()))

road=list(set(mat[:,1].tolist()))

print(df1[0])
for i in feature:
    for j in road:
        print(df1[df1[0] == i].values)

# df=pd.read_csv('天河区市政设施统计.csv')
# print(df)
#https://www.jianshu.com/p/a213384a0dbf