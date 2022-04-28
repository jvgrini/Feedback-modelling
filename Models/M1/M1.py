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
    k4 = 64
    k5 = 0.1875
    k6 = 0.125
    k7 = 10**-6
    #ki = 1

    A = x[0]
    E = x[1]

    DADT = k1 - ((k2+k4)*A) + (k3*E)

    DEDT = k5 -((k6*E)/(k7+E))*A

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

with open("Models/M1/CSVfiles/CSV_A_k4=64.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows([A])
with open ("Models/M1/CSVfiles/CSV_E_k4=64.csv", "w",newline='') as file:
    writer = csv.writer(file)
    writer.writerows([E])

plt.plot(t,A,label = "A")
plt.grid()
plt.xlim(7.5,20)
plt.savefig("Models/M1/Plots/M1plot_k4=64.pdf")
plt.show()








