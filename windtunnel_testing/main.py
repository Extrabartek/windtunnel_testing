import numpy as np
import matplotlib.pyplot as plt

data1 = "data/corr_test.txt"
data2 = "data/naca642015a_no_vis.txt"
data3 = "data/naca642015a_vic.txt"

list1 = np.genfromtxt(data1, dtype='float', skip_header=2, usecols=(1, 2, 3, 4))
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

plt.plot(alpha_no_vis, cl_no_vis)
plt.show()
