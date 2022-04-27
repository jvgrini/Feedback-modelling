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
    k4 = 6
    k5 = 2
    k6 = 3
    k7 = 10**-6
    ki = 1

    A = x[0]
    E = x[1]

    DADT = k1 - (k2*A) +((k3*ki)/(ki+E))-(k4*A)

    DEDT = k5*A -((k6*E)/(k7+E))

    return [DADT, DEDT]

x0 = [1.5,7.96078686]
t1=np.linspace(0,10,10000)
t2=np.linspace(10,60,50000)
t = np.concatenate((t1,t2))

y = odeint(model, x0, t1, args=(p1k2,))
x1 = y[-1]
print (y[-1])
y = np.concatenate((y, odeint(model, x1, t2, args=(p2k2,))))


A = y[:,0]
E = y[:,1] 

with open("Models/M2/CSVfiles/testCSV_k4=32.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows([A])

plt.plot(t,A,label = "A")
plt.grid()
plt.savefig("Models/M2/Plots/testM2plot_k4=32.pdf")
plt.show()








