import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import Position

def plotAstar(length, width, height, paths, gates):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = cm.rainbow(np.linspace(0, 1, len(paths)))

    for path, c in zip(paths, colors):
        x = path[0]
        y = path[1]
        z = path[2]

        ax.plot(x, y, z, color=c, marker='o')
    x = []
    y = []
    z = []
    for gate in gates:
        x.append(gate.getX())
        y.append(gate.getY())
        z.append(gate.getZ())

    ax.scatter(x, y, z, color="k", marker='o')



    ax.set_xlim3d([0, length-1])
    ax.set_ylim3d([0, width-1])
    ax.set_zlim3d([0, height-1])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    
    plt.show()
    
    