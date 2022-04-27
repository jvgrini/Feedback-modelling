import matplotlib.pyplot as plt
import numpy as np

y1= np.loadtxt('M4/CSVfiles/CSV_k4=0', delimiter=',', unpack=True)
y2= np.loadtxt('M4/CSVfiles/CSV_k4=0_ki2=0.1', delimiter=',', unpack=True)

t = np.linspace(0,100,100000)

plt.plot(t,y1,label='ki1/2 = 1')
plt.plot(t,y2,label='ki1/2 = 0.1')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()

plt.savefig('M4/Plots/M4plot_compare_ki_values.pdf')
plt.show()