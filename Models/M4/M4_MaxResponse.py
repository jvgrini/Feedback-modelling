import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator

y1= 1.5 -min(np.loadtxt('M4/CSVfiles/CSV_k4=0', delimiter=',', unpack=True))
y2= 1.5 -min(np.loadtxt('M4/CSVfiles/CSV_k4=2', delimiter=',', unpack=True))
y3= 1.5 -min(np.loadtxt('M4/CSVfiles/CSV_k4=4', delimiter=',', unpack=True))
y4= 1.5 -min(np.loadtxt('M4/CSVfiles/CSV_k4=8', delimiter=',', unpack=True))
y5= 1.5 -min(np.loadtxt('M4/CSVfiles/CSV_k4=16', delimiter=',', unpack=True))
y6= 1.5 -min(np.loadtxt('M4/CSVfiles/CSV_k4=32', delimiter=',', unpack=True))

x = [1,2,4,8,16,32]
y = [y1,y2,y3,y4,y5,y6]
print(x,y)

fig, ax = plt.subplots()
ax.semilogx(x,y,'o', linestyle = 'dotted')
ax.xaxis.set_major_locator(LogLocator(10**0.25))
plt.xlabel("log(k4)")
plt.ylabel("Max response")
ax.grid(which='major')
plt.savefig("M4/Plots/M4plot_MaxResponse.pdf")
plt.show()