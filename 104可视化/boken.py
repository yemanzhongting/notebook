# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/4 19:13'
#谷歌秘钥
#AIzaSyDL8oES4GIqwFoEal86NcUs9qNWldz8ClM
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.iris import flowers

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

p.circle(flowers["petal_length"], flowers["petal_width"],
         color=colors, fill_alpha=0.2, size=10)

output_file("iris.html", title="iris.py example")

show(p)