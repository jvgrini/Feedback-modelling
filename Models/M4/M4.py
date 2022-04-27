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
    k5 = 2
    k6 = 32
    k7 = 10**-6
    ki1 = 1
    ki2 = 0.1

    A = x[0]
    E = x[1]

    DADT = k1 - k2*A -k4*A + k3*((ki1)/(ki1+E))

    DEDT = k5 -((k6*E)/(k7+E)) *(ki2/(ki2+A))

    return [DADT, DEDT]

x0 = [1.5,3.23369909]
t1=np.linspace(0,10,10000)
t2=np.linspace(10,100,90000)
t = np.concatenate((t1,t2))

y = odeint(model, x0, t1, args=(p1k2,))
x1 = y[-1]
print (y[-1])
y = np.concatenate((y, odeint(model, x1, t2, args=(p2k2,))))


A = y[:,0]
E = y[:,1] 

with open("Models/M4/CSVfiles/testCSV_k4=0_ki2=0.1.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows([A])

plt.plot(t,A,label = "A")
plt.grid()
plt.xlim(7.5,20)
plt.savefig("Models/Plots/testM4plot_k4=0_ki2=0.1.pdf")
plt.show()








