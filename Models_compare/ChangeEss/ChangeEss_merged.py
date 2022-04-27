import numpy as np
import matplotlib.pyplot as plt

M5 = (np.loadtxt('CSV/M5_ChangeEss.csv', delimiter=',', unpack=False, skiprows=1)[:,1])
M6 = (np.loadtxt('CSV/M6_ChangeEss.csv', delimiter=',', unpack=False, skiprows=1)[:,1])
M7 = (np.loadtxt('CSV/M7_ChangeEss.csv', delimiter=',', unpack=False, skiprows=1)[:,1])
M8 = (np.loadtxt('CSV/M8_ChangeEss.csv', delimiter=',', unpack=False, skiprows=1)[:,1])

t = range(32)

fig, ax = plt.subplots(nrows=2,ncols=2)
ax[0,0].plot(t,M5, 'o', label='M5', markersize=3)
ax[0,0].set_title('M5')
ax[0,0].grid()
ax[0,0].set_xlabel('k3')
ax[0,0].set_ylabel('change k1')

ax[0,1].plot(t,M6, 'o', label='M6', markersize=3)
ax[0,1].set_title('M6')
ax[0,1].grid()
ax[0,1].set_xlabel('k3')
ax[0,1].set_ylabel('change k1')

ax[1,0].plot(t,M7, 'o', label='M7', markersize=3)
ax[1,0].set_title('M7')
ax[1,0].grid()
ax[1,0].set_xlabel('k3')
ax[1,0].set_ylabel('change k1')

ax[1,1].plot(t,M8, 'o', label='M8', markersize=3)
ax[1,1].set_title('M8')
ax[1,1].grid()
ax[1,1].set_xlabel('k3')
ax[1,1].set_ylabel('change k1')


fig.tight_layout()
plt.savefig('M5-M8_changeEss.pdf')
plt.show()