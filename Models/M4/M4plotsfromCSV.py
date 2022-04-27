import matplotlib.pyplot as plt
import numpy as np

y1= np.loadtxt('Models/M4/CSVfiles/CSV_k4=0', delimiter=',', unpack=True)
y2= np.loadtxt('Models/M4/CSVfiles/CSV_k4=2', delimiter=',', unpack=True)
y3= np.loadtxt('Models/M4/CSVfiles/CSV_k4=4', delimiter=',', unpack=True)
y4= np.loadtxt('Models/M4/CSVfiles/CSV_k4=8', delimiter=',', unpack=True)
y5= np.loadtxt('Models/M4/CSVfiles/CSV_k4=16', delimiter=',', unpack=True)
y6= np.loadtxt('Models/M4/CSVfiles/CSV_k4=32', delimiter=',', unpack=True)
x= np.linspace(0,100,100000)

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
plt.title('M4')

#plt.title('')
#plt.xlabel('Time')
#plt.ylabel(' ')
plt.xlim([9,100])

plt.savefig("Models/M4/Plots/M4plot_merged.pdf", bbox_inches='tight')
plt.show()