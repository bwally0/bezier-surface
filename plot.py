import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def bernstein_poly(i, n, t):
    from math import comb

    return comb(n, i) * (t**i) * ((1 - t) ** (n - i))


def bezier_patch(control_points, resolution=30):
    u = np.linspace(0, 1, resolution)
    v = np.linspace(0, 1, resolution)
    X, Y, Z = (
        np.zeros((resolution, resolution)),
        np.zeros((resolution, resolution)),
        np.zeros((resolution, resolution)),
    )

    for i in range(4):
        for j in range(4):
            bu = bernstein_poly(i, 3, u)
            bv = bernstein_poly(j, 3, v)
            X += np.outer(bu, bv) * control_points[i][j][0]
            Y += np.outer(bu, bv) * control_points[i][j][1]
            Z += np.outer(bu, bv) * control_points[i][j][2]
    return X, Y, Z


control_points = np.array(
    [
        [[0, 0, 0], [0, 1, 1], [0, 2, 1], [0, 3, 0]],
        [[1, 0, -1], [1, 1, 0], [1, 2, 0], [1, 3, -1]],
        [[2, 0, 0], [2, 1, 1], [2, 2, 1], [2, 3, 0]],
        [[3, 0, -1], [3, 1, 0], [3, 2, 0], [3, 3, -1]],
    ]
)

X, Y, Z = bezier_patch(control_points)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(
    X,
    Y,
    Z,
    facecolors=plt.cm.viridis((Z - Z.min()) / (Z.max() - Z.min())),
    rstride=1,
    cstride=1,
    linewidth=0,
    antialiased=True,
)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
