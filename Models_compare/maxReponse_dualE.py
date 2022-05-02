import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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
background = [2,4,8,16,32]
p1p = 2
p2p = 6
t1=np.linspace(0,10,10000)
t2=np.linspace(10,60,50000)
t = np.concatenate((t1,t2))
maxResponses = []

#establishEss() establishes the steady state value of E for a given k4 value. 
def establishEss(background):
    t = np.linspace(0,1000,1000000)
    x0=[1.5,15,15]
    perturbation=p1p

    y = odeint(models.M2_dualE, x0, t, args=(perturbation,background))
    Ess = [y[:,1][-1], y[:,2][-1]]
    return Ess

for i in range(len(background)):
     Ess = establishEss(background[i])

     x0 = [1.5, Ess[0], Ess[1]]
     y = odeint(models.M2_dualE, x0, t1, args=(p1p, background[i]))
     x1 = y[-1]
     y = np.concatenate((y, odeint(models.M2_dualE, x1, t2, args=(p2p,background[i]))))
     maxResponses.append(1.5 - min(y[:,0]))

print(maxResponses)

plt.loglog(background,maxResponses, 'o', linestyle = 'dotted')
plt.xlabel('log(background)')
plt.ylabel('log(max response')
plt.grid(which='both')
plt.tight_layout()
plt.savefig('Models_compare/plots_compare_models/maxResponse_M2_dualE.pdf')
plt.show()