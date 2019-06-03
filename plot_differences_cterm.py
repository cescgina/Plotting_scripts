import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# cterm backbone
plt.title("Cterm backbone")
data = np.genfromtxt("../PK2_evoCt_md/rmsd_backbone_cterm.dat", missing_values="NA", filling_values=0)
plt.hist(data, bins=50, density=True, label="evoCt", alpha=0.5)
data = np.genfromtxt("rmsd_backbone_cterm.dat", missing_values="NA", filling_values=0)
plt.hist(data, bins=50, density=True, label="PK2", alpha=0.5)
plt.legend()
plt.xlabel(r"RMSD$(\AA)$")

plt.figure()
plt.title("Cterm noh")
# cterm noh
data = np.genfromtxt("../PK2_evoCt_md/rmsd_noh_cterm.dat", missing_values="NA", filling_values=0)
plt.hist(data, bins=50, density=True, label="evoCt", alpha=0.5)
data = np.genfromtxt("rmsd_noh_cterm.dat", missing_values="NA", filling_values=0)
plt.hist(data, bins=50, density=True, label="PK2", alpha=0.5)
plt.legend()
plt.xlabel(r"RMSD$(\AA)$")

plt.figure()
# global backbone
plt.title("Global backbone")
data = np.genfromtxt("../PK2_evoCt_md/rmsd_backbone_global.dat", missing_values="NA", filling_values=0)
plt.hist(data, bins=50, density=True, label="evoCt", alpha=0.5)
data = np.genfromtxt("rmsd_backbone_global.dat", missing_values="NA", filling_values=0)
plt.hist(data, bins=50, density=True, label="PK2", alpha=0.5)
plt.legend()
plt.xlabel(r"RMSD$(\AA)$")

plt.figure()
# noh global
plt.title("Global noh")
data = np.genfromtxt("../PK2_evoCt_md/rmsd_noh_global.dat", missing_values="NA", filling_values=0)
plt.hist(data, bins=50, density=True, label="evoCt", alpha=0.5)
data = np.genfromtxt("rmsd_noh_global.dat", missing_values="NA", filling_values=0)
plt.hist(data, bins=50, density=True, label="PK2", alpha=0.5)
plt.legend()
plt.xlabel(r"RMSD$(\AA)$")

plt.figure()
all_data = []
for i in range(1, 5):
    data = np.loadtxt("0/backbone_cterm_rmsd_%d" % i)
    all_data.append(data.tolist())
all_data = np.array(all_data)
plt.imshow(all_data, aspect="auto")
plt.yticks(range(4), ["Trajectory %d" % (i+1) for i in range(4)])
loc, _ = plt.xticks()
plt.xticks(loc[1:], [i*100 for i in range(6)])
plt.xlabel("Time (ns)")
plt.ylabel("Trajectory")
plt.grid(b=None)
cbar = plt.colorbar()
cbar.set_label(r"RMSD$(\AA)$")
plt.title("PK2 backbone cterm")

plt.figure()
all_data = []
for i in range(1, 5):
    data = np.loadtxt("../PK2_evoCt_md/0/backbone_cterm_rmsd_%d" % i)
    all_data.append(data.tolist())
all_data = np.array(all_data)
plt.imshow(all_data, aspect="auto")
plt.yticks(range(4), ["Trajectory %d" % (i+1) for i in range(4)])
loc, _ = plt.xticks()
plt.xticks(loc[1:], [i*100 for i in range(6)])
plt.xlabel("Time (ns)")
plt.ylabel("Trajectory")
plt.grid(b=None)
cbar = plt.colorbar()
cbar.set_label(r"RMSD$(\AA)$")
plt.title("PK2evoCt backbone cterm")
plt.show()
