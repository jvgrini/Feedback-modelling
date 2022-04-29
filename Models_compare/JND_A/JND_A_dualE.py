import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import csv

#The purpose of this program is to take a feedback model, a range of k4 values and an exclusion factor, and output
#the change in k2 required for this exclusion to be exceeded by E.

#
class models:

    def M2_dualE(x,t,pert, background):
        k1 = 0
        k2 = pert
        k3 = 100
        k4 = background
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
    x0=[1.5,15,15]
    perturbation=perturbation_org

    y = odeint(models.M2_dualE, x0, t, args=(perturbation,background))
    Ess = [y[:,1][-1], y[:,2][-1]]
    return Ess

#loops through all given k4 values
for i in range(len(background)):
    Ess = establishEss(background[i])
    x0 = [1.5, Ess[0],Ess[1]]
    perturbation=perturbation_org
    print(background[i], " original Ess", x0[1])

    #Loop running until absolute difference between Ess for k2=2 and Ess for k2=2+stepSize*n exceeds Ess for 
    # k2=2 * exclusion
    # 
    while True:

        perturbation += stepSize
        y = odeint(models.M2_dualE, x0, t, args=(perturbation,background[i]))

        A = y[:,0]
        Amax = max(A)
        Amin = min(A)
        
        if abs(Amax - 1.5) > 1.5*exclusion or abs(1.5-Amin > 1.5*exclusion):
            difference= perturbation-perturbation_org
            differences.append(difference)
            print(differences)
        
            break
#print(plotArray)

with open('Models_compare/JND_A//CSV/M2_dualE.csv', "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["background","difference"])
    for i in range(len(background)):
        writer.writerow([background[i],differences[i]])

plt.plot(background,differences, 'o')
plt.grid()
plt.xlabel("Background")
plt.ylabel("Required perturbation")
plt.title("M2 antithetic model")
plt.savefig("Models_compare/JND_A/plots/M2_dualE.pdf")
plt.show()
