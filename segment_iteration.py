from math import cos, sin, pi
import matplotlib.pyplot as plt


K = 0.6
def func(pt):
    x = pt[0] + K * sin(pt[1])
    y = pt[1] + x
    return x, y

def distance(pt1, pt2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

h = 0.5
p1 = (-1, -1)
p2 = (1, 1)
pts_list = []
fig, ax = plt.subplots()

def fragmentation(pt1, pt2):
    d = distance(pt1, pt2)
    print(d)
    if d < h:
        pts_list.append(pt1)
        pts_list.append(pt2)
    else:
        plt.scatter([x[0] for x in pts_list], [x[1] for x in pts_list])
        plt.draw()
        pt3 = ((pt1[0] + pt2[0]) / 2, (pt1[1] + pt2[1]) / 2)
        fragmentation(func(pt1), func(pt3))
        fragmentation(func(pt2), func(pt3))

fragmentation(p1, p2)
print(pts_list)
plt.scatter([x[0] for x in pts_list], [x[1] for x in pts_list])
plt.show()
