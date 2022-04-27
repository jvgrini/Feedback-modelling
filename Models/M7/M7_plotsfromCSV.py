import matplotlib.pyplot as plt
import numpy as np

y1= np.loadtxt('Models/M7/CSVfiles/CSV_A_k3=0.csv', delimiter=',', unpack=True)
y2= np.loadtxt('Models/M7/CSVfiles/CSV_A_k3=2.csv', delimiter=',', unpack=True)
y3= np.loadtxt('Models/M7/CSVfiles/CSV_A_k3=4.csv', delimiter=',', unpack=True)
y4= np.loadtxt('Models/M7/CSVfiles/CSV_A_k3=8.csv', delimiter=',', unpack=True)
y5= np.loadtxt('Models/M7/CSVfiles/CSV_A_k3=16.csv', delimiter=',', unpack=True)
y6= np.loadtxt('Models/M7/CSVfiles/CSV_A_k3=32.csv', delimiter=',', unpack=True)

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
plt.title('M7')
#plt.xlabel('Time')
#plt.ylabel(' ')
plt.xlim([9,20])

plt.savefig("Models/M7/Plots/M7plot_merged.pdf",bbox_inches='tight')
plt.show()