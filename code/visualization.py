import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import Position

from random import randint 

from pylab import *


def plotAstar(length, width, height, paths, gates):
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    colors = cm.nipy_spectral(np.linspace(0, 1, len(paths)))

    usedColors = []

    for path in paths:
        x = path[0]
        y = path[1]
        z = path[2]

        # to create a nice mix of colors: pick a random not used color
        randIndex = randint(0, len(colors))
        while randIndex in usedColors:
            randIndex = randint(0, len(colors))
        c = colors[randIndex]
        usedColors.append(randIndex)

        ax.plot(x, y, z, color=c, zorder=-1)
    x = []
    y = []
    z = []
    for gate in gates:
        x.append(gate.getX())
        y.append(gate.getY())
        z.append(gate.getZ())

    ax.scatter(x, y, z, c='black', marker="s", s=60, zorder=10)

    ax.set_xlim3d([0, length-1])
    ax.set_ylim3d([0, width-1])
    ax.set_zlim3d([0, height-1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    title = str(len(paths)) + " Random Connections"
    plt.title(title)

    # mngr = plt.get_current_fig_manager()
    # mngr.window.setGeometry(50,100,640,545)

    plt.show(block=False)
    
    