import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

data1 = "data/corr_test.txt"
data2 = "data/naca642015a_no_vis.txt"
data3 = "data/naca642015a_vic.txt"
data4 = "data/naca642015a_no_vis_low.txt"
data5 = "data/naca642015a_no_vis_high.txt"

list1 = np.genfromtxt(data1, dtype='float', skip_header=2, skip_footer=10, usecols=(1, 2, 3, 4))
list2 = np.genfromtxt(data2, dtype='float', skip_header=12, usecols=(0, 1, 2, 4, 5))
list3 = np.genfromtxt(data3, dtype='float', skip_header=12, usecols=(0, 1, 2, 4, 5))
list4 = np.genfromtxt(data4, dtype='float', skip_header=12, usecols=(0, 1, 2, 4, 5))
list5 = np.genfromtxt(data5, dtype='float', skip_header=12, usecols=(0, 1, 2, 4, 5))

alpha_test = list1[:, 0].tolist()
cl_test = list1[:, 2].tolist()
cd_test = list1[:, 1].tolist()
cm_test = list1[:, 3].tolist()


alpha_vis = list3[:, 0].tolist()
cl_vis = list3[:, 1].tolist()
cd_vis = list3[:, 2].tolist()
cm_vis = list3[:, 3].tolist()
x_tran_vis = list3[:, 4].tolist()


alpha_no_vis = list2[:, 0].tolist()
cl_no_vis = list2[:, 1].tolist()
cd_no_vis = list2[:, 2].tolist()
cm_no_vis = list2[:, 3].tolist()

alpha_no_vis_low = list4[:, 0].tolist()
cl_no_vis_low = list4[:, 1].tolist()
cd_no_vis_low = list4[:, 2].tolist()
cm_no_vis_low = list4[:, 3].tolist()

alpha_no_vis_high = list5[:, 0].tolist()
cl_no_vis_high = list5[:, 1].tolist()
cd_no_vis_high = list5[:, 2].tolist()
cm_no_vis_high = list5[:, 3].tolist()

# Transition stuff

medians = [0.32688836565848545, 0.34453558034012555, 0.373888419243947, 0.38337678326727126, 0.40090643295083384,
           0.43038932902419214, 0.4426316173382495, 0.47131767650996914, 0.49549065029091, 0.5623238909360257,
           0.7255066982171113, 0.8207503980943998, 0.9270464005157034, 0.9448716250598717, 0.9631451717857009,
           0.9608805576770914, 0.9700927738049774, 0.9769427369266158, 0.9757458620190147, 0.9759057128834981,
           0.9704199540761738, 0.9809245380106282, 0.975263522380702, 0.9785757165430538, 0.9730852595447957,
           0.9762991625478167, 0.9688328030877711, 0.9832511849900484, 0.9788907118202986, 0.983767072360875,
           0.9888150004588816, 0.9903111392643691]
angles = [-2, -1, 0, 1, 2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5,
          14, 14.5, 15, 15.5, 16.5, 17.5]

for a in range(0, len(angles)):
    medians[a] = abs(medians[a] - 1)
'''
plt.plot(angles, medians)
plt.plot(alpha_vis, x_tran_vis)
plt.show()
'''

# Lift plot

'''
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
plt.plot(alpha_test, cl_test, marker='x', label="Test data")
# plt.plot(alpha_vis, cl_vis, label="XFOIL with viscosity")
plt.plot(alpha_no_vis, cl_no_vis, label="XFOIL without viscosity")
# plt.plot(alpha_no_vis_low, cl_no_vis_low, label="XFOIL without viscosity Low")
# plt.plot(alpha_no_vis_high, cl_no_vis_high, label="XFOIL without viscosity High")
plt.plot([-180 / math.pi, 180 / math.pi], [-2 * math.pi, 2 * math.pi], label=r'$2\pi$ slope', linestyle="--")
plt.title(r'Lift Coefficient vs. Angle of attack')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
'''
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
# plt.plot(alpha_vis, cm_vis, label="XFOIL with viscosity")
plt.plot(alpha_no_vis, cm_no_vis, label="XFOIL without viscosity")
plt.title(r'Moment Coefficient vs. Angle of attack')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

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
