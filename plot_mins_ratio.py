import os
import numpy as np
import matplotlib.pyplot as plt
from AdaptivePELE.utilities import utilities
back = utilities.get_available_backend()
if back is not None:
    plt.switch_backend(back)
plt.style.use("ggplot")
plt.rcParams.update({'font.size': 14})


def autolabel(rects, xpos='center'):
    """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(offset[xpos]*3, 3),  # use 3 points offset
                     textcoords="offset points",  # in both directions
                     ha=ha[xpos], va='bottom')

population = {'WT': (4834, 4489), 'F454H': (4873, 3498), 'F454T': (8583, 1836), 'F454S': (4131, 2691), 'F454P': (4942, 1240)}
labels = ["WT", "F454H", "F454T", "F454S", "F454P"]
min1 = []
min2 = []
width = 0.35
x = []
for i, k in enumerate(labels):
    min1.append(population[k][0])
    min2.append(population[k][1])
    x.append(i)
x = np.array(x)
plt.figure(figsize=(7, 7))
rects1 = plt.bar(x-width/2, min1, width, label="Min A")
rects2 = plt.bar(x+width/2, min2, width, label="Min B")
autolabel(rects1)
autolabel(rects2)
plt.ylabel("Population")
plt.xticks(x, labels)
plt.legend()
plt.savefig("population_ratios.png", bbox_inches='tight', dpi=300)
plt.show()
