import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import csv

p1k1 = 2
p2k1 = 6

def establishEss(k1):
    x0=[1.5,15]
    t=np.linspace(0,1000,100000)
    y = odeint(model,x0,t,args=(k1,))

    Ess = y[:,1][-1]
    return Ess


def model(x,t, vark1):
    #Parameters:
    k1 = vark1
    k2 = 0
    k3 = 64
    k4 = 100
    k5 = 3
    k6 = 2
    k7 = 10**-6
    ki = 1

    A = x[0]
    E = x[1]

    DADT = k1 - (k2*A) +k3 -((k4*ki*A)/(ki+E))

    DEDT = k5 -(((k6*E)/(k7+E))*A)

    return [DADT, DEDT]

x0 = [1.5,establishEss(p1k1)]
print(x0)
t1=np.linspace(0,10,10000)
t2=np.linspace(10,60,50000)
t = np.concatenate((t1,t2))

y = odeint(model, x0, t1, args=(p1k1,))
x1 = y[-1]
print (y[-1])
y = np.concatenate((y, odeint(model, x1, t2, args=(p2k1,))))


A = y[:,0]
E = y[:,1] 

with open("M6/CSVfiles/CSV_A_k3=64", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows([A])
with open ("M6/CSVfiles/CSV_E_k3=64", "w",newline='') as file:
    writer = csv.writer(file)
    writer.writerows([E])

plt.plot(t,A,label = "A")
plt.grid()
#plt.xlim(7.5,20)
plt.savefig("M6/Plots/M5plot_k3=64.pdf")
plt.show()








