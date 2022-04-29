import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import csv

def M2_dualE(x,t,pert):
    k1 = 0
    k2 = pert
    k3 = 100
    k4 = 32
    k5 = 2
    k6 = 3
    k7 = 1
    KI = 1

    A = x[0]
    E1 = x[1]
    E2 = x[2]

    DADT = k1 - A*(k2+k4) + ((k3*KI)/(KI + E1))

    DE1DT = k5 * A - k7 *E1*E2

    DE2DT = k6 -k7*E1*E2

    return [DADT, DE1DT, DE2DT]

def establishEss(pert):
    x0=[1.5,15,15]
    t=np.linspace(0,1000,100000)
    y = odeint(M2_dualE,x0,t,args=(pert,))

    Ess = [y[:,1][-1], y[:,2][-1]]
    return Ess

p1pert = 2
p2pert = 6

Ess = establishEss(p1pert)
x0 = [1.5, Ess[0], Ess[1]]
print(x0)
t1=np.linspace(0,10,10000)
t2=np.linspace(10,60,50000)
t = np.concatenate((t1,t2))

y = odeint(M2_dualE, x0, t1, args=(p1pert,))
x1 = y[-1]
print (y[-1])
y = np.concatenate((y, odeint(M2_dualE, x1, t2, args=(p2pert,))))


A = y[:,0]
E1 = y[:,1] 
E2 = y[:,2]

with open("Models/M2_dualE/CSVfiles/CSV_A_k4=32.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows([A])
with open ("Models/M2_dualE/CSVfiles/CSV_E1_k4=32.csv", "w",newline='') as file:
    writer = csv.writer(file)
    writer.writerows([E1])
with open ("Models/M2_dualE/CSVfiles/CSV_E2_k4=32.csv", "w",newline='') as file:
    writer = csv.writer(file)
    writer.writerows([E2])

plt.plot(t,A,label = "A")
#plt.plot(t,E1,label = "E1")
#plt.plot(t,E2,label = "E2")
plt.grid()
#plt.xlim(7.5,20)
plt.savefig("Models/M2_dualE/Plots/M2_dualE_plot_k4=32.pdf")
plt.show()