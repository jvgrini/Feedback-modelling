import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import csv

p1k2 = 2
p2k2 = 6


def model(x,t, vark2):
    #Parameters:
    k1 = 0
    k2 = vark2
    k3 = 100
    k4 = 0
    k5 = 2.5
    k6 = 1.0
    k7 = 10**-6
    ki = 1

    A = x[0]
    E = x[1]

    DADT = k1 - ((k2+k4)*A) + (k3*E)

    DEDT = ((k5*ki)/(ki+A))-((k6*E)/(k7+E))

    return [DADT, DEDT]

def establishEss(k2):
    x0=[1.5,15]
    t=np.linspace(0,1000,100000)
    y = odeint(model,x0,t,args=(k2,))

    Ess = y[:,1][-1]
    return Ess

x0 = [1.5,establishEss(p1k2)]
t1=np.linspace(0,10,10000)
t2=np.linspace(10,60,50000)
t = np.concatenate((t1,t2))

y = odeint(model, x0, t1, args=(p1k2,))
x1 = y[-1]
print (y[-1])
y = np.concatenate((y, odeint(model, x1, t2, args=(p2k2,))))


A = y[:,0]
E = y[:,1] 

with open("Models/M3/CSVfiles/highAggr_CSV_A_k4=0", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows([A])
with open ("Models/M3/CSVfiles/highAggr_CSV_E_k4=0", "w",newline='') as file:
    writer = csv.writer(file)
    writer.writerows([E])

plt.plot(t,A,label = "A")
plt.grid()
plt.savefig("Models/M3/Plots/highAggr_M3plot_k4=0.pdf")
plt.show()








