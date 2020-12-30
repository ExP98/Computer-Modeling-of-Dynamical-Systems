import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from math import ceil


par1, par2 = 0.7, -0.82
def func(pt):
    return par1 * pt[0] + pt[1], par2 + pt[0] ** 2


def distance(pt1, pt2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

h = 0.001
p_list = [(-1.38, 0.076), (-0.896, 1.28648), (-0.19113, 0.85053), (0.6, 0.1121), (0.731, -0.82206),
          (0.3, -0.3943), (-0.075, -0.7686), (-0.261, -0.34164), (-1.196, -0.5)]
pts_set = []

def fragmentation(pt1, pt2):
    d = distance(pt1, pt2)
    if d < h:
        pts_set.append(pt1)
        pts_set.append(pt2)
    elif d < 5:
        count = ceil(d / h)
        temp_list = []
        for i in range(1, count):
            pt = (pt1[0] + i / count * (pt2[0] - pt1[0]), pt1[1] + i / count * (pt2[1] - pt1[1]))
            temp_list.append(pt)
        pairs = []
        for i in range(1, len(temp_list)):
            pairs.append((temp_list[i-1], temp_list[i]))
        for p1, p2 in pairs.copy():
            fragmentation(func(p1), func(p2))


for i in range(len(p_list)):
    for j in range(len(p_list)):
        if i != j:
          fragmentation(p_list[i], p_list[j])

print(len(pts_set))
left, right, top, bottom = -1.49, 0.85, 1.36, -0.89
height, width = 1200, 1200

img = Image.new('RGB', (width, height))
pixels = img.load()

x_div, y_div = right - left, top - bottom
for x, y in pts_set:
    x_pixel = round(((x - left) / x_div) * width)
    y_pixel = round(((top - y)/ y_div) * height)
    pixels[x_pixel, y_pixel] = (255, 255, 0)
img.show()
# img.save('ex4/cathala_pil.png')
