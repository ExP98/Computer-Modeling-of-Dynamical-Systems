import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from math import cos, sin, pi, ceil


def cathala(pt):
    par1, par2 = 0.7, -0.82
    return par1 * pt[0] + pt[1], par2 + pt[0] ** 2


def mira3(pt):
    par1, par2 = 1, -0.5952
    return par1 * pt[0] + pt[1], par2 + pt[0] ** 2


def henon(pt):
    p1 = 6
    angle = 2 * pi / p1
    return -(pt[1] - pt[0]**2) * sin(angle) + pt[0] * cos(angle), (pt[1] - pt[0]**2) * cos(angle) + pt[0] * sin(angle)


def distance(pt1, pt2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


h = 0.001  # 0.0001 for cathala_pil_3
p_list = [(-1.38, 0.076), (-0.896, 1.28648), (-0.19113, 0.85053), (0.6, 0.1121), (0.731, -0.82206),
          (0.3, -0.3943), (-0.075, -0.7686), (-0.261, -0.34164), (-1.196, -0.5)]
# p_list = [(-1.41, 0.71), (0.5, 0.395), (0.95, -0.5), (-0.1, -0.5), (0.5, -0.41), (0.57, -0.43), (0.36, 0.24), (0.69, -0.41), (0.29, -0.43)]
pts_set = []

def fragmentation(pt_start, pt_end):
    d = distance(pt_start, pt_end)
    if d < h:
        pts_set.append(pt_start)
        pts_set.append(pt_end)
    elif d < 2:
        pt3 = (pt_start[0] + (pt_end[0] - pt_start[0]) / 3, pt_start[1] + (pt_end[1] - pt_start[1]) / 3)
        pt4 = (pt_start[0] + (pt_end[0] - pt_start[0]) * 2 / 4, pt_start[1] + (pt_end[1] - pt_start[1]) * 2 / 4)
        pt5 = (pt_start[0] + (pt_end[0] - pt_start[0]) * 3 / 4, pt_start[1] + (pt_end[1] - pt_start[1]) * 3 / 4)
        func = cathala
        fragmentation(func(pt_start), func(pt3))
        fragmentation(func(pt3), func(pt4))
        fragmentation(func(pt4), func(pt5))
        fragmentation(func(pt5), func(pt_end))


for i in range(len(p_list)):
    for j in range(len(p_list)):
        if i != j:
          fragmentation(p_list[i], p_list[j])

print(len(pts_set))
left, right, top, bottom = -1.49, 0.85, 1.36, -0.89 # Cathala
# left, right, top, bottom = -2, 1.5, 1.7, -1   # Mira3
height, width = 1200, 1200

img = Image.new('RGB', (width, height))
pixels = img.load()

x_div, y_div = right - left, top - bottom
for x, y in pts_set:
    x_pixel = round(((x - left) / x_div) * width)
    y_pixel = round(((top - y) / y_div) * height)
    pixels[x_pixel, y_pixel] = (255, 255, 0)
img.show()
# img.save('testtt.png')
