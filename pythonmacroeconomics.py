# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:57:25 2021

@author: leore
"""

x=10
n=0.03 #tx de croissance
t=0 #valeur du temps au départ
X=[x] #faire un tableau ac ttes ls valeurs de x
T=[t]
while t<150: #on continue jusq'à ce que T soit egal a 150
    x=x+n*x
    t=t+1 #pr que le temps avance
    X=X+[x]#ancien tableau+nvelle valeur de x
    T=T+[t]#liste T (=[T])+ vlaur de t
print(x)
from pylab import * #on a besoin ds fonct° qui st là-dedans pr faire ds graphiques
plot(T,X)
plt.xlabel("Temps")

#faire ds listes pr sauvegarder ds valeurs
l=[]
l=l+[3]
l1=l+[2,1]
print(l)
print(l1)