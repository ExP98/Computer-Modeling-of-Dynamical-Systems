import numpy as np
import matplotlib.pyplot as plt


def distance(pt1, pt2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# h, w = 3, 5
# # mx = np.zeros((3, 4))
# mx = np.random.rand(h, w)
# ind = np.argsort(mx, axis=None)[::-1][:10]
# true_ind = []
# for i in ind:
#     row = i // w
#     col = i % w
#     true_ind.append((row, col))
# tc = np.array(true_ind)
# np.savetxt('test.out', tc, delimiter=';')
points = np.loadtxt('test.out', delimiter=';')
dots = [list(points[0])]

for i, point in enumerate(points):
    print(len(dots))
    flag = True
    for d in dots.copy():
        if distance(point, d) < 0.2:
            flag = False
            break
    if flag:
        dots.append(list(point))

print(len(dots), dots)
# dots = np.array(dots)
# np.savetxt('pivot_dots.out', dots, delimiter=';')

fig, ax = plt.subplots()
ax.scatter([_[0] for _ in dots], [_[1] for _ in dots])
plt.show()
