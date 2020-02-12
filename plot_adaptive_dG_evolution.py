import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cycler
plt.style.use("ggplot")
matplotlib.rcParams.update({'font.size': 14})
# colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD'])
plt.rc('axes', prop_cycle=colors)


def parse_results(file_name):
    delta_G = []
    errors = []
    with open(file_name) as f:
        f.readline()
        f.readline()
        for line in f:
            values = line.rstrip().split()
            delta_G.append(float(values[1]))
            errors.append(float(values[2]))
    return delta_G, errors

dG_1f5k, err_1f5k = parse_results("/home/jgilaber/urokinases_free_energy/1f5k_adaptive_sampl_sameR_2/100/100cl/results.txt")
dG_1o3p, err_1o3p = parse_results("/home/jgilaber/urokinases_free_energy/1o3p_adaptive_sampl_sameR_2/100/100cl/results.txt")
dG_1sqa, err_1sqa = parse_results("/home/jgilaber/urokinases_free_energy/1sqa_adaptive_sampl_sameR_2/100/100cl/results.txt")

plt.figure(figsize=(6, 6))
plt.errorbar(range(len(dG_1f5k)), dG_1f5k, yerr=err_1f5k, label="Calc. BAM")
plt.errorbar(range(len(dG_1o3p)), dG_1o3p, yerr=err_1o3p, label="Calc. 655")
plt.errorbar(range(len(dG_1sqa)), dG_1sqa, yerr=err_1sqa, label="Calc. UI1")
plt.axhline(-5.2, label="Exp. BAM", color="#EE6666")
plt.axhline(-9.2, label="Exp. 655", color="#3388BB")
plt.axhline(-12.7, label="Exp. UI1", color="#9988DD")
plt.xlabel("Epoch")
plt.ylabel(r"$\Delta G$ (kcal/mol)")
plt.legend(loc="lower right")
plt.savefig("evolution_adaptive_uro_steps.png", dpi=300, bbox_inches='tight')
plt.show()
