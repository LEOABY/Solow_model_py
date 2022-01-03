# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:25:32 2021

@author: leore
"""

R=[r]
T=[t]
while t<=100:
    k=k+s*y-d*k
    f=(k/(a*l))**alpha
    fprime=alpha*((k/(a*l)**(1-alpha))) #R du K
    r=(fprime*k)/f
    t=t+1
    R=R+[r]
    T=T+[t]
print(r)
plot(T,R)