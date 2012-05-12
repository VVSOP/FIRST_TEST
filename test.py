import numpy as np
from pylab import *

s_file = open("dataLinReg1D.txt","r")
x=[]
y=[]
line = s_file.readline()
line = line [2:]
print line
for i in range(len(line)):
    if (line[i]==' '):
        print i
        x.append(float(line[1:i]))
        y.append(float(line[i+1:-1]))
        break 
print x 
print y