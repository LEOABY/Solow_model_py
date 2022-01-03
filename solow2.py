# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:47:19 2021

@author: leore
"""

import math as m
import numpy as np
k=1
a=1
l=1
t=0
K=[k]
A=[a]
L=[l]
T=[t]
y=(k**(0.5))*((a*l)**0.5)
Y=[y]
p=y/(a*l)
P=[p]
g=0.02
n=0.02
s=0.2
d=0.05
while t<=100:
    k=k+s*y-d*k
    x=np.random.random()
    g=-0.2*x+(0.02)*x
    a=a+g*a
    l=l+n*l
    y=(k**(0.5))*((a*l)**0.5)
    t=t+1
    K=K+[k]
    A=A+[a]
    L=L+[l]
    T=T+[t]
    Y=Y+[y]
    p=y/(a*l)
    P=P+[p]
    print(p)
from pylab import *
plot(T,P)