import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import csv

#The purpose of this program is to take a feedback model, a range of k4 values and an exclusion factor, and output
#the change in k2 required for this exclusion to be exceeded by E.

#
def model(x,t, vark1, vark3):
    #Parameters:
    k1 = vark1
    k2 = 0
    k3 = vark3
    k4 = 100
    k5 = 5
    k6 = 2
    k7 = 10**-6
    ki1 = 1
    ki2 = 1

    A = x[0]
    E = x[1]

    DADT = k1 - (k2*A) +k3 -((k4*ki2*A)/(ki2+E))

    DEDT = ((k5*ki1)/(ki1+A))-((k6*E)/(k7+E))

    return [DADT, DEDT]

#Initialize required variables:
#   differences: array to which required change in k2 will be appended
#   k4values: k4 values tested
#   exclusion: Exclusion factor
#   stepSize: Change in k2 between each calculation
#   k2: 
#   k2org:
differences = []
k3values = range(0,32)
exclusion = 0.03
stepSize = 0.01
k1 = 2
k1org = 2
t = np.linspace(0,20,20000)

#establishEss() establishes the steady state value of E for a given k4 value. 
def establishEss(k3):
    t = np.linspace(0,1000,1000000)
    x0=[1.5,15]
    k1=k1org

    y = odeint(model, x0, t, args=(k1,k3))
    Ess = y[:,1][-1]
    return Ess

#loops through all given k4 values
for i in range(len(k3values)):
    Ess = establishEss(k3values[i])
    x0 = [1.5, Ess]
    k1=k1org
    print(k3values[i], " original Ess", x0[1])

    #Loop running until absolute difference between Ess for k2=2 and Ess for k2=2+stepSize*n exceeds Ess for 
    # k2=2 * exclusion
    # 
    while True:

        k1 += stepSize
        y = odeint(model, x0, t, args=(k1,k3values[i]))

        E = y[:,1]
        
        if abs(Ess - E[-1]) > Ess*exclusion:
            print("k3 = ", k3values[i])
            print("Ess: ", E [-1])
            print("Difference between original and new Ess when exceding difference: ",Ess-E[-1])
            print("k1 value: ", k1)
            print("Difference between new and original k2 value: ", k1-k1org)
            difference= k1-k1org
            differences.append(difference)
            print(differences)
        
            break
#print(plotArray)

with open('CSV/M8_ChangeEss.csv', "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["k3","differences"])
    for i in range(len(k3values)):
        writer.writerow([k3values[i],differences[i]])

plt.plot(k3values,differences, 'o')
plt.grid()
plt.xlabel("k3")
plt.ylabel("Change in k1")
plt.savefig("M8_changeEss.pdf")
plt.show()
