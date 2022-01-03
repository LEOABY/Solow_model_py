# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:17:42 2021

@author: leore
"""
"""alpha=0.5
import math as m
k=1
a=1
l=1
t=0
K=[k]
A=[a]
L=[l]
T=[t]
y=(k**(alpha))*((a*l)**(1-alpha))
Y=[y]
p=y/(a*l)
P=[p]
g=0.02
n=0.02
s=0.2
d=0.05
while t<=100:
    k=k+s*y-d*k
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
plot(T,P)"""

alpha=0.5
import math as m
k=1
a=1
l=1
t=0
K=[k]
A=[a]
L=[l]
T=[t]
y=(k**(alpha))*((a*l)**(1-alpha))
Y=[y]
p=y/(a*l)
P=[p]
g=0.02
n=0.04
s=0.2
d=0.05
while t<=100:
    k=k+s*y-d*k
    a=a+g*a
    l=l+n*l
    y=(k**(0.5))*((a*l)**0.5)
    t=t+1
    K=K+[k]
    A=A+[a]
    L=L+[l]
    T=T+[t]
    Y=Y+[y]
    p=y/(a*l) #=f(k)
    P=P+[p]
    print(p)
"""from pylab import *
plot(T,P)"""

"""1er fait de kaldor:les parts du K et du L dans le R national sont relativement constantes"""
"""R=[r]
T=[t]
while t<=500:
    k=k+s*y-d*k
    f=(k/(a*l))**alpha
    fprime=alpha*((k/(a*l)**(1-alpha))) #R du K
    r=(fprime*k)/f
    t=t+1
    R=R+[r]
    T=T+[t]
print(r)
plot(T,R)"""

"""2éme fait de Kaldor: le tx de croissance de K/L est relativemennt constant sur une longue période"""
"""kl=k-l
KL=[kl]
t1=0
T1=[t1]
while t1<=100:
    k=k+k*(n+g)
    l=l+l*n
    K=[k]
    L=[l]
    kl=k-l
    KL=KL+[kl]
    t1=t1+1
    T1=T1+[t1]
    print(kl)
plot(T1,KL)"""

"""A REVOIR/5ème fait de Kaldor: le ratio K/Y est relativement constant au cours du temps"""
"""
ky=k-y
KY=[ky]
t2=0
T2=[t2]
K=[k]
L=[l]
y=(k**(0.5)*(a*l)**(0.5))
Y=[y]
while t2<=100:
    y=(k**(0.5)*(a*l)**(0.5))
    k=k+k*(n+g)
    y=y+y*(n+g)
    l=l+l*n
    Y=Y+[y]
    K=K+[k]
    L=L+[l]
    t2=t2+1
    T2=T2+[t2]
    ky=k-y
    KY=KY+[ky]
    print(ky)
plot(T2,KY)"""

"""3ème fait de Kaldor:le tx de croissance de la production par Leurs est relativemeny constant au cours du temps"""
"""
t3=0
yl=y-l
YL=[yl]
while t3<=100:
    y=y+y*(n+g)
    l=l+l*n
    yl=y-l
    YL=YL+[yl]
    Y=Y+[y]
    L=L+[l]
    t3=t3+1
    print(yl)
plot(T,YL)"""

w=y/(a*l)-(k/(a*l))