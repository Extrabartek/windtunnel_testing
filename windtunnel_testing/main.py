import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

data1 = "data/corr_test.txt"
data2 = "data/naca642015a_no_vis.txt"
data3 = "data/naca642015a_vic.txt"

list1 = np.genfromtxt(data1, dtype='float', skip_header=2, skip_footer=10, usecols=(1, 2, 3, 4))
list2 = np.genfromtxt(data2, dtype='float', skip_header=12, usecols=(0, 1, 2, 4))
list3 = np.genfromtxt(data3, dtype='float', skip_header=12, usecols=(0, 1, 2, 4))


alpha_test = list1[:, 0].tolist()
cl_test = list1[:, 2].tolist()
cd_test = list1[:, 1].tolist()
cm_test = list1[:, 3].tolist()

alpha_vis = list3[:, 0].tolist()
cl_vis = list3[:, 1].tolist()
cd_vis = list3[:, 2].tolist()
cm_vis = list3[:, 3].tolist()

alpha_no_vis = list2[:, 0].tolist()
cl_no_vis = list2[:, 1].tolist()
cd_no_vis = list2[:, 2].tolist()
cm_no_vis = list2[:, 3].tolist()


# Lift plot

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.axhline(color='black')
ax1.axvline(color='black')
ax1.set_xlim(-5, 20)
ax1.set_ylim(-0.5, 1.25)
ax1.set_xticks(np.arange(-5, 21, 2.5))
ax1.set_yticks(np.arange(-0.5, 1.26, 0.25))
ax1.set_ylabel(r'Lift Coefficient ($c_l$)')
ax1.set_xlabel(r'Angle of Attack (AoA)')
ax1.xaxis.set_major_formatter(StrMethodFormatter(u'{x:.1f}°'))
plt.plot(alpha_test, cl_test, marker='x', label="Real world")
plt.plot(alpha_vis, cl_vis, label="XFOIL with viscosity")
plt.plot(alpha_no_vis, cl_no_vis, label="XFOIL without viscosity")
plt.plot([-math.degrees(1), math.degrees(1)], [-2 * math.pi, 2 * math.pi], label="ideal lift")
plt.title(r'Lift Coefficient vs. Angle of attack')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

'''
# Drag plot

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.axhline(color='black')
ax1.axvline(color='black')
ax1.set_xlim(-5, 20)
ax1.set_ylim(0, 0.08)
ax1.set_xticks(np.arange(-5, 21, 2.5))
ax1.set_yticks(np.arange(0, 0.08, 0.01))
ax1.set_ylabel(r'Drag Coefficient ($c_d$)')
ax1.set_xlabel(r'Angle of Attack (AoA)')
ax1.xaxis.set_major_formatter(StrMethodFormatter(u'{x:.1f}°'))
plt.plot(alpha_test, cd_test, marker='x', label="Real world")
plt.plot(alpha_vis, cd_vis, label="XFOIL with viscosity")
plt.plot(alpha_no_vis, cd_no_vis, label="XFOIL without viscosity")
plt.title(r'Drag Coefficient vs. Angle of attack')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
'''
'''
# Moment graph

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.axhline(color='black')
ax1.axvline(color='black')
ax1.set_xlim(-5, 20)
ax1.set_ylim(-0.06, 0.04)
ax1.set_xticks(np.arange(-5, 21, 2.5))
ax1.set_yticks(np.arange(-0.06, 0.05, 0.01))
ax1.set_ylabel(r'Moment Coefficient ($c_m$)')
ax1.set_xlabel(r'Angle of Attack (AoA)')
ax1.xaxis.set_major_formatter(StrMethodFormatter(u'{x:.1f}°'))
plt.plot(alpha_test, cm_test, marker='x', label="Real world")
plt.plot(alpha_vis, cm_vis, label="XFOIL with viscosity")
plt.plot(alpha_no_vis, cm_no_vis, label="XFOIL without viscosity")
plt.title(r'Moment Coefficient vs. Angle of attack')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
'''
'''
# Drag polar

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.axhline(color='black')
ax1.axvline(color='black', lw=3)
ax1.set_xlim(0, 0.1)
ax1.set_ylim(-0.5, 1.25)
ax1.set_xticks(np.arange(0, 0.11, 0.01))
ax1.set_yticks(np.arange(-0.5, 1.26, 0.25))
ax1.set_ylabel(r'Lift Coefficient ($c_l$)')
ax1.set_xlabel(r'Drag Coefficient ($c_d$)')
# ax1.xaxis.set_major_formatter(StrMethodFormatter(u'{x:.1f}°'))
plt.plot(cd_test, cl_test, marker='x', label="Real world")
plt.plot(cd_vis, cl_vis, label="XFOIL with viscosity")
# plt.plot(cd_no_vis, cl_no_vis, label="XFOIL without viscosity") # no drag so need for it being included
plt.title(r'Lift Coefficient vs. Drag coefficient')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
'''