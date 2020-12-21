import numpy as np
import matplotlib.pyplot as plt

w, h = 128, 128
# cp in [0; 1000], gn in [250; 1000]
gn, cp = 650, 650
r, c_div = gn / 250, 750
matrix = np.random.random_sample((h, w))

plt.ion()

for k in range(500):
    plt.clf()
    plt.suptitle(f"Logistic lattice, step {k}, CP = {cp}, GN = {gn}")
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
    if k == 10:
        break
    plt.imshow(matrix, vmin=0, vmax=1)
    plt.draw()
    plt.gcf().canvas.flush_events()

print('end')
plt.ioff()
plt.show()
