from __future__ import print_function
import os
import glob
import matplotlib
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from AdaptivePELE.atomset import atomset
plt.switch_backend("qt5agg")
plt.style.use("ggplot")
matplotlib.rcParams.update({'font.size': 28})

receptor = "ERK2"
temperature = 1500
if not os.path.exists(receptor):
    os.makedirs(receptor)
path = "/gpfs/scratch/bsc72/bsc72328/SCRIPT_MSM/ERK2"

ligands = ["EK2", "EK3", "EK6", "EK9", "E63"]
experimental = [-7.57, -6.95, -9.62, -9.57, -9.72]
limits = [6, 8, 6, 6, 8]
calculated = []
calculated_err = []
template = "%ssoft9_T%d*"
found = []
show_plots = False
for i, lig in enumerate(ligands):
    path_lig = os.path.join(path, template % (lig, temperature))
    folders = glob.glob(path_lig)
    if not len(folders):
        print("Path %s not found" % path_lig)
        continue
    index = None
    for ind_opt, fold in enumerate(folders):
        if not os.path.exists(os.path.join(fold, "output_pele", "MSM_%d" % (2), "results_summary.txt")):
            continue
        index = ind_opt
    if index is None:
        continue
    path_lig = folders[index]
    print("Processing", path_lig)
    pdb_native = atomset.PDB()
    pdb_native.initialise(os.path.join(path_lig, "ERK2_INIT_complex_processed.pdb"), resname=lig)
    minim = pdb_native.getCOM()
    iterations = glob.glob(os.path.join(path_lig, "output_pele", "MSM_*"))
    n_iterations = len(iterations)
    if not n_iterations:
        print("No iterations found in %s" % path_lig)
        continue
    found.append(i)
    # for ij, it in enumerate(sorted(iterations, key=lambda x: int(x.rsplit("_")[-1]))):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(25, 12))
    for ij, it in enumerate(sorted(iterations, key=lambda x: int(x.rsplit("_")[-1]))[:3]):
        data = np.loadtxt(os.path.join(path_lig, "output_pele", it, "pmf_xyzg_0.dat"))
        clusters = data[:, :3]
        distance = np.linalg.norm(clusters-minim, axis=1)
        g = data[:, -1]
        axes[ij].plot(distance, g, 'o', label="Iteration %d" % (ij+1), markersize=8)
        if ij > 0:
            axes[ij].set_yticklabels([])
        axes[ij].set_ylim(top=limits[i])
        axes[ij].text(1, limits[i]-0.5, chr(65+ij), fontsize=60)
    axes[1].set_xlabel(r"Distance to minima ($\AA$)")
    axes[0].set_ylabel("PMF (kcal/mol)")
    # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, markerscale=2)
    fig.savefig(os.path.join(receptor, "pmf_%s_%s.png" % (receptor, lig)), bbox_inches='tight', dpi=300)
    # with open(os.path.join(path_lig, "output_pele", "MSM_%d" % (n_iterations-1), "results_summary.txt")) as f:
    last = n_iterations - 1
    with open(os.path.join(path_lig, "output_pele", "MSM_%d" % (last), "results_summary.txt")) as f:
        for line in f:
            if line.startswith("dG = "):
                dG, std = [float(el) for el in line[5:].split(" +- ")]
                calculated.append(dG)
                calculated_err.append(std)
    # with open(os.path.join(path_lig, "results", "results.txt")) as f:
    #     for line in f:
    #         if not line.startswith("#"):
    #             dG = float(line.split()[1])
    #     calculated.append(dG)


experimental = [experimental[j] for j in found]
slope, intercept, r_value, p_value, stderr = stats.linregress(experimental, calculated)
print("R2 value of %.3f" % (r_value**2))
error = np.array(experimental)-np.array(calculated)
print("Mean square error is", np.sqrt(np.mean(error**2)))
plt.figure(figsize=(12, 12))
# plt.plot(experimental, calculated, 'o', markersize=12)
plt.errorbar(experimental, calculated, yerr=calculated_err, fmt='o', markersize=12)
plt.ylabel(r"Estimated $\Delta G$ (kcal/mol)")
plt.xlabel(r"Experimental $\Delta G$ (kcal/mol)")
plt.savefig(os.path.join(receptor, "correlation_%s.png" % receptor), bbox_inches='tight', dpi=300)
if show_plots:
    plt.show()
