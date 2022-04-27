import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator

y1= abs(1.5 -max(np.loadtxt('M6/CSVfiles/CSV_A_k3=0', delimiter=',', unpack=True)))
y2= abs(1.5 -max(np.loadtxt('M6/CSVfiles/CSV_A_k3=2', delimiter=',', unpack=True)))
y3= abs(1.5 -max(np.loadtxt('M6/CSVfiles/CSV_A_k3=4', delimiter=',', unpack=True)))
y4= abs(1.5 -max(np.loadtxt('M6/CSVfiles/CSV_A_k3=8', delimiter=',', unpack=True)))
y5= abs(1.5 -max(np.loadtxt('M6/CSVfiles/CSV_A_k3=16', delimiter=',', unpack=True)))
y6= abs(1.5 -max(np.loadtxt('M6/CSVfiles/CSV_A_k3=32', delimiter=',', unpack=True)))

x = [1,2,4,8,16,32]
y = [y1,y2,y3,y4,y5,y6]
print(x,y)

fig, ax = plt.subplots()
ax.semilogx(x,y,'o', linestyle = 'dotted')
ax.xaxis.set_major_locator(LogLocator(10**0.25))
plt.xlabel("log(k4)")
plt.ylabel("Max response")
ax.grid(which='major')
plt.savefig("M6/Plots/M6plot_MaxResponse.pdf")
plt.show()