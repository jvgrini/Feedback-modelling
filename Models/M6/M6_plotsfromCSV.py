import matplotlib.pyplot as plt
import numpy as np

y1= np.loadtxt('Models/M6/CSVfiles/CSV_A_k3=0', delimiter=',', unpack=True)
y2= np.loadtxt('Models/M6/CSVfiles/CSV_A_k3=2', delimiter=',', unpack=True)
y3= np.loadtxt('Models/M6/CSVfiles/CSV_A_k3=4', delimiter=',', unpack=True)
y4= np.loadtxt('Models/M6/CSVfiles/CSV_A_k3=8', delimiter=',', unpack=True)
y5= np.loadtxt('Models/M6/CSVfiles/CSV_A_k3=16', delimiter=',', unpack=True)
y6= np.loadtxt('Models/M6/CSVfiles/CSV_A_k3=32', delimiter=',', unpack=True)
y7= np.loadtxt('Models/M6/CSVfiles/CSV_A_k3=64', delimiter=',', unpack=True)
x= np.linspace(0,60,60000)

plt.plot(x,y1, label="k3=0")
plt.plot(x,y2,label="k3=2")
plt.plot(x,y3,label="k3=4")
plt.plot(x,y4,label="k3=8")
plt.plot(x,y5,label="k3=16")
plt.plot(x,y6,label="k3=32")
#plt.plot(x,y7,label="k3=64")

plt.grid()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
plt.tight_layout()
plt.title('M6')
#plt.xlabel('Time')
#plt.ylabel(' ')
plt.xlim([9,50])

plt.savefig("Models/M6/Plots/M6plot_merged.pdf",bbox_inches='tight')
plt.show()