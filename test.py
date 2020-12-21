import numpy as np
import matplotlib.pyplot as plt

w, h = 128, 128
# cp in [0; 1000], gn in [250; 1000]
gn, cp = 650, 650
r, c_div, step_lim = gn / 250, 750, 500
matrix = np.random.random_sample((h, w))

fig, ax = plt.subplots()

for k in range(step_lim):
    ax.cla()
    plt.suptitle(f"Logistic lattice, step {k+1}, CP = {cp}, GN = {gn}")

    copy_m = matrix.copy()
    for i in range(h):
        for j in range(w):
            avg = (copy_m[i - 1, j] + copy_m[(i + 1) % h, j] + copy_m[i, j - 1] + copy_m[i, (j + 1) % w]) / 4
            c = cp * (avg - copy_m[i, j]) / c_div
            x = r * copy_m[i, j] * (1 - copy_m[i, j]) + c
            if x > 1:
                matrix[i, j] = 1
            elif x < 0:
                matrix[i, j] = 0
            else:
                matrix[i, j] = x

    ax.imshow(matrix, interpolation='nearest', vmin=0, vmax=1)
    plt.pause(0.005)
