import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import csv

#The purpose of this program is to take a feedback model, a range of k4 values and an exclusion factor, and output
#the change in k2 required for this exclusion to be exceeded by E.

#
class models:
    
    def M1(x,t, pert, background):
        #Parameters:
        k1 = 0
        k2 = pert
        k3 = 100
        k4 = background
        k5 = 0.1875
        k6 = 0.125
        k7 = 10**-6
        #ki = 1

        A = x[0]
        E = x[1]

        DADT = k1 - ((k2+k4)*A) + (k3*E)

        DEDT = k5 -((k6*E)/(k7+E))*A

        return [DADT, DEDT]
    
    def M2(x,t, pert, background):
        #Parameters:
        k1 = 0
        k2 = pert
        k3 = 100
        k4 = background
        k5 = 2
        k6 = 3
        k7 = 10**-6
        ki = 1

        A = x[0]
        E = x[1]

        DADT = k1 - (k2*A) +((k3*ki)/(ki+E))-(k4*A)

        DEDT = k5*A -((k6*E)/(k7+E))

        return [DADT, DEDT]
    
    def M3(x,t, pert, background):
    #Parameters:
        k1 = 0
        k2 = pert
        k3 = 100
        k4 = background
        k5 = 0.625
        k6 = 0.25
        k7 = 10**-6
        ki = 1

        A = x[0]
        E = x[1]

        DADT = k1 - ((k2+k4)*A) + (k3*E)

        DEDT = ((k5*ki)/(ki+A))-((k6*E)/(k7+E))

        return [DADT, DEDT]

    def M4(x,t, pert, background):
    #Parameters:
        k1 = 0
        k2 = pert
        k3 = 100
        k4 = background
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
    
    def M5(x,t, pert, background):
        k1 = pert
        k2 = 0
        k3 = background
        k4 = 100
        k5 = 0.03125
        k6 = 0.046875
        k7 = 10**-6
        ki = 1

        A = x[0]
        E = x[1]

        DADT = k1 - (k2*A) +k3 -(k4*E*A)

        DEDT = k5*A -((k6*E)/(k7+E))

        return [DADT, DEDT]
    
    def M6(x,t, pert, background):
    #Parameters:
        k1 = pert
        k2 = 0
        k3 = background
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

    def M7(x,t, pert, background):
    #Parameters:
        k1 = pert
        k2 = 0
        k3 = background
        k4 = 100
        k5 = 0.0625
        k6 = 5/32
        k7 = 10**-6
        ki = 1

        A = x[0]
        E = x[1]

        DADT = k1 - (k2*A) +k3 -(k4*E*A)

        DEDT = k5 -((k6*E)/(k7+E))*(ki/(ki+A))

        return [DADT, DEDT]

    def M8(x,t, pert, background):
        #Parameters:
        k1 = pert
        k2 = 0
        k3 = background
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
background = range(0,32)
exclusion = 0.03
stepSize = 0.01
perturbation = 2
perturbation_org = 2
t = np.linspace(0,20,20000)

#establishEss() establishes the steady state value of E for a given k4 value. 
def establishEss(background):
    t = np.linspace(0,1000,1000000)
    x0=[1.5,15]
    perturbation=perturbation_org

    y = odeint(models.M8, x0, t, args=(perturbation,background))
    Ess = y[:,1][-1]
    return Ess

#loops through all given k4 values
for i in range(len(background)):
    Ess = establishEss(background[i])
    x0 = [1.5, Ess]
    perturbation=perturbation_org
    print(background[i], " original Ess", x0[1])

    #Loop running until absolute difference between Ess for k2=2 and Ess for k2=2+stepSize*n exceeds Ess for 
    # k2=2 * exclusion
    # 
    while True:

        perturbation += stepSize
        y = odeint(models.M8, x0, t, args=(perturbation,background[i]))

        A = y[:,0]
        Amax = max(A)
        Amin = min(A)
        
        if abs(Amax - 1.5) > 1.5*exclusion or abs(1.5-Amin > 1.5*exclusion):
            difference= perturbation-perturbation_org
            differences.append(difference)
            print(differences)
        
            break
#print(plotArray)

with open('Models_compare/JND_A//CSV/M8_ChangeEss.csv', "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["background","difference"])
    for i in range(len(background)):
        writer.writerow([background[i],differences[i]])

plt.plot(background,differences, 'o')
plt.grid()
plt.xlabel("Background")
plt.ylabel("Required perturbation")
plt.title("M8")
plt.savefig("Models_compare/JND_A/plots/M8_changeEss.pdf")
plt.show()
