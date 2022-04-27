import matplotlib.pyplot as plt
import numpy as np

y1= np.loadtxt('Models/M3/CSVfiles/CSV_A_k4=0.csv', delimiter=',', unpack=True)
y2= np.loadtxt('Models/M3/CSVfiles/CSV_A_k4=2.csv', delimiter=',', unpack=True)
y3= np.loadtxt('Models/M3/CSVfiles/CSV_A_k4=4.csv', delimiter=',', unpack=True)
y4= np.loadtxt('Models/M3/CSVfiles/CSV_A_k4=8.csv', delimiter=',', unpack=True)
y5= np.loadtxt('Models/M3/CSVfiles/CSV_A_k4=16.csv', delimiter=',', unpack=True)
y6= np.loadtxt('Models/M3/CSVfiles/CSV_A_k4=32.csv', delimiter=',', unpack=True)
x= np.linspace(0,60,60000)

plt.plot(x,y1, label="k4=0")
plt.plot(x,y2,label="k4=2")
plt.plot(x,y3,label="k4=4")
plt.plot(x,y4,label="k4=8")
plt.plot(x,y5,label="k4=16")
plt.plot(x,y6,label="k4=32")

plt.grid()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
plt.tight_layout()
plt.title('M3')
#plt.xlabel('Time')
#plt.ylabel(' ')
plt.xlim([9,20])

plt.savefig("Models/M3/Plots/M3plot_merged.pdf",bbox_inches='tight')
plt.show()