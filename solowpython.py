# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:12:30 2021

@author: leore
"""
"""
import math as m
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
s=0
S=[s]
C=[]
g=0.02
n=0.02
d=0.05
while s<1:
    k=1
    a=1
    l=1
    y=(k**(0.5))*((a*l)**0.5)
    t=0
    while t<15:
        k=k+s*y-d*k
        a=a+g*a
        l=l+n*l
        k=k+s*y-d*k
        K=K+[k]
        A=A+[a]
        L=L+[l]
        T=T+[t]
        y=(k**(0.5))*((a*l)**0.5)
        Y=Y+[y]
        p=y/(a*l)
        P=P+[p]
        t=t+1
    S=S+[s]
    c=p-s*p
    C=C+[c]
    s=s+0.01
import pylab
from pylab import *
plot(S,C)"""

import math as m
import numpy as np
import pylab
s=0
S=[ ]
C=[ ]
while s<1:
    K=1
    A=1
    L=1
    Y=K**(0.5)*(A*L)**(0.5)
    t=0
    while t<15:
        x=np.random.random()
        g=-0.05*x+(0.08)*x
        A=A+g*A
        n=0.02
        L=L+n*L
        d=0.05
        K=K+s*Y-d*K
        Y=K**(0.5)*(A*L)**(0.5)
        P=Y/(A*L)
        t=t+1
    S=S+[s]
    c=P-s*P
    C=C+[c]
    s=s+0.01
pylab.plot(S,C)

