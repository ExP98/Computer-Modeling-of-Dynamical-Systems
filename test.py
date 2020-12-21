import numpy as np
import matplotlib.pyplot as plt
import copy
import time

w, h = 128, 128
# cp in [0; 1000], gn in [250; 1000]
gn, cp = 250, 0
r = gn / 250
matrix = np.random.random_sample((h, w))

# plt.ion()
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, nrows=1)

for k in range(500):
    # plt.clf()
    ax1.cla()
    ax2.cla()
    ax3.cla()

    plt.suptitle(f"Logistic lattice, step {k}, CP = {cp}, GN = {gn}")
    copy_m = copy.deepcopy(matrix)
    for i in range(h):
        for j in range(w):
            # avg, count = 0, 0
            # if i > 0:
            #     avg += copy_m[i-1, j]
            #     count += 1
            # if i < h-1:
            #     avg += copy_m[i+1, j]
            #     count += 1
            # if j > 0:
            #     avg += copy_m[i, j-1]
            #     count += 1
            # if j < w-1:
            #     avg += copy_m[i, j+1]
            #     count += 1
            # avg = avg  / count
            avg = (copy_m[i - 1, j] + copy_m[(i + 1) % h, j] + copy_m[i, j - 1] + copy_m[i, (j + 1) % w]) / 4
            c = cp * (avg - copy_m[i, j]) / 1000
            x = r * copy_m[i, j] * (1 - copy_m[i, j]) + c
            if x > 1:
                matrix[i, j] = 1
            elif x < 0:
                matrix[i, j] = 0
            else:
                matrix[i, j] = x
            # print(avg, c, x)

    ax1.imshow(matrix, interpolation='nearest', vmin=0, vmax=1)
    ax2.contour(matrix)
    ax3.contourf(matrix)

    plt.pause(0.005)
    # print(matrix)
    # plt.draw()
    # plt.gcf().canvas.flush_events()

print('end')
plt.ioff()
plt.show()
