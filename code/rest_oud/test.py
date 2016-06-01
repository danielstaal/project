import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

data = [[[0 for x in range(4)] for x in range(4)] for x in range(4)]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [0, 0, 1, 1, 1, 2, 3]
y = [0, 1, 1, 2, 3, 3, 3]
z = [3, 3, 3, 3, 3, 3, 3]

ax.plot(x, y, z, c='r', marker='o')

x = [1, 2, 3, 3, 3, 4, 4]
y = [0, 0, 0, 1, 2, 2, 3]
z = [3, 3, 3, 3, 3, 3, 3]

ax.plot(x, y, z, c='b', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
