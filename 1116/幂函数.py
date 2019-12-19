# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 15:55
# @Author  : yemanzhongting
# @Email   : sggzhang@whu.edu.cn
# @File    : 幂函数.py
# @Software: PyCharm
import configparser
import os, sys
import matplotlib
import matplotlib.pyplot as plt
import numpy
import math
from pylab import *


from matplotlib.font_manager import _rebuild
_rebuild()

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

x = numpy.linspace(0.0001,10,200)
f1=numpy.power(x,-1)
f2=numpy.power(math.e,x)
f3 = numpy.power(2,x)

plt.plot(x,f1,'r',linewidth=2)#,x,f2,'b',x,f3,'g'
plt.axis([0,4,0,100])#xmin xmax ymin ymax
plt.text(0.5,7.5,r'$x^-1$',fontsize=16)
#plt.text(2.2,7.5,r'$e^x$',fontsize=16)
#plt.text(3.2,7.5,r'$2^x$',fontsize=16)
plt.title('幂函数',fontsize=16)
plt.xlabel("节点的度")
plt.ylabel("节点个数")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

savefig('power.pdf',dpi=1000)
show()