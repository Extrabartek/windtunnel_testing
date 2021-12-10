import numpy as np
import matplotlib.pyplot as plt

data1 = "data/corr_test.txt"
data2 = "data/naca642015a_no_vis.txt"
data3 = "data/naca642015a_vic.txt"

list1 = np.genfromtxt(data1, dtype='float', skip_header=2, skip_footer=10, usecols=(1, 2, 3, 4))
list2 = np.genfromtxt(data2, dtype='float', skip_header=12, usecols=(0, 1, 2, 4))
list3 = np.genfromtxt(data3, dtype='float', skip_header=12, usecols=(0, 1, 2, 4))


alpha_test = list1[:, 0].tolist()
cl_test = list1[:, 2].tolist()
cd_list = list1[:, 1].tolist()
cm_list = list1[:, 3].tolist()

alpha_vis = list3[:, 0].tolist()
cl_vis = list3[:, 1].tolist()
cd_vis = list3[:, 2].tolist()
cm_vis = list3[:, 3].tolist()

alpha_no_vis = list2[:, 0].tolist()
cl_no_vis = list2[:, 1].tolist()
cd_no_vis = list2[:, 2].tolist()
cm_no_vis = list2[:, 3].tolist()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.axhline(color='black')
ax1.axvline(color='black')
ax1.set_xlim(-5, 20)
ax1.set_ylim(-0.5, 1.25)
ax1.set_xticks(np.arange(-5, 21, 2.5))
ax1.set_yticks(np.arange(-0.5, 1.26, 0.25))
ax1.set_xlabel("X label")
ax1.set_ylabel("Y label")
plt.plot(alpha_test, cl_test, marker='+')
plt.plot(alpha_vis, cl_vis)
plt.title("Title")
plt.grid(True)
plt.show()
