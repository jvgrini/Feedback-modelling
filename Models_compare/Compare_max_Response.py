from cmath import log
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator
import copy

# Max response M1
#[[0, 2, 4, 8, 16, 32] 
# [0.3159807095969127, 0.29051140823711163, 0.26858601968049967, 0.23286865396764656, 0.18295238351728393, 0.12674932489967294]
#
# Max response M2
#[0, 2, 4, 8, 16, 32]
#[0.9776938928358834, 0.7195022735184228, 0.5683824719089509, 0.399927010352525, 0.25094567044169036, 0.14376667221805572]
#
# Max response M3
#[0, 2, 4, 8, 16, 32] 
# [0.5079855555208392, 0.44503835242040113, 0.39483153067343024, 0.32045417543414856, 0.23046313965343757, 0.1456791952149905]
#
#Max response M4
#[0, 2, 4, 8, 16, 32]
#[0.9847708316382977, 0.7308255262753451, 0.581102071146689, 0.4120163671039325, 0.2604692815195031, 0.15008105836272856]

#Outflow
#
#Max response M5
#[0, 2, 4, 8, 16, 32] 
#[2.5434754903110264, 1.3186410994456823, 0.8915015471159609, 0.5414625508080908, 0.30344852216701357, 0.1615185390149585]
#
#Max response M6
#[0, 2, 4, 8, 16, 32] 
#[2.5434754903110264, 1.3186410994456823, 0.8915015471159609, 0.5414625508080908, 0.30344852216701357, 0.1615185390149585]
#
#Max response M7
#[0, 2, 4, 8, 16, 32] 
#[0.31877328490658474, 0.29451634537966087, 0.2733098115448507, 0.23817348969351282, 0.18801447809325222, 0.13040585443041453]
#
#Max response M8
#[0, 2, 4, 8, 16, 32] 
#[2.8303077172809132, 1.4227284847543, 0.9509561421239812, 0.5720486992491467, 0.31846110797336036, 0.1688299348327198]
#
# Cannot include values for k4 = 0. This point cannot be plotted on loglog plot.
#Inpunt values in y1-4 for the models that you wish to compare

points =[2,4,8,16,32]
y1 = [1.3186410994456823, 0.8915015471159609, 0.5414625508080908, 0.30344852216701357, 0.1615185390149585]
y2 = [1.3186410994456823, 0.8915015471159609, 0.5414625508080908, 0.30344852216701357, 0.1615185390149585]
y3 = [0.29451634537966087, 0.2733098115448507, 0.23817348969351282, 0.18801447809325222, 0.13040585443041453]
y4 = [1.4227284847543, 0.9509561421239812, 0.5720486992491467, 0.31846110797336036, 0.1688299348327198]

y1norm= copy.deepcopy(y1)
y2norm = copy.deepcopy(y2)
y3norm = copy.deepcopy(y3)
y4norm = copy.deepcopy(y4)

#Normalizing data
for i in range(len(y1norm)):
    y1norm[i] = y1norm[i]/y1[0]

for i in range(len(y2norm)):
    y2norm[i] = y2norm[i]/y2[0]

for i in range(len(y3norm)):
    y3norm[i] = y3norm[i]/y3[0]

for i in range(len(y4norm)):
    y4norm[i] = y4norm[i]/y4[0]


#Create plot
fig, ax= plt.subplots(2)

#Axis 1, true values
ax[0].loglog(points, y1, 'o', linestyle='dotted', label = 'M5')
ax[0].loglog(points, y2, 'o', linestyle='dotted', label = 'M6')
ax[0].loglog(points, y3, 'o', linestyle='dotted', label = 'M7')
ax[0].loglog(points, y4, 'o', linestyle='dotted', label = 'M8')

#Axis 2, normalized values
ax[1].loglog(points, y1norm, 'o', linestyle = 'dotted', label ="M5")
ax[1].loglog(points, y2norm, 'o', linestyle = 'dotted', label = "M6")
ax[1].loglog(points, y3norm, 'o', linestyle = 'dotted', label = "M7")
ax[1].loglog(points, y4norm, 'o', linestyle = 'dotted', label = "M8")

ax[0].set_title('Max Response')
ax[0].set_xlabel('log(k4)')
ax[0].set_ylabel('log(max response)')
ax[0].grid(which ='both')
ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax[1].set_title('Normalized Max Response')
ax[1].set_xlabel('log(k4)')
ax[1].set_ylabel('log(max response)')
ax[1].grid(which ='both')
ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('Plot_compare_response_m5-8.pdf')
plt.show()