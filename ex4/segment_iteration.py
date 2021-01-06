from PIL import Image, ImageDraw, ImageFont
import numpy as np


def cathala(pt):
    par1, par2 = 0.7, -0.82
    return par1 * pt[0] + pt[1], par2 + pt[0] ** 2


def distance(pt1, pt2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


h = 0.0001  # 0.001 for cathala_pivot
nodes_number = 3
# p_list = [(-1.38, 0.076), (-0.896, 1.28648), (-0.19113, 0.85053), (0.6, 0.1121), (0.731, -0.82206), (0.3, -0.3943),
#           (-0.075, -0.7686), (-0.261, -0.34164), (-1.196, -0.5), (0.23793, -0.27046), (0.43, 0.29), (0, 0.05872)]
p_list = np.loadtxt('pivot_dots.out', delimiter=';')
points_list = []


def fragmentation(pt_start, pt_end):
    d = distance(pt_start, pt_end)
    if d < h:
        points_list.append(pt_start)
        points_list.append(pt_end)
    elif d < 2:
        pt_list = [pt_start]
        for multiplier in range(1, nodes_number-1):
            pt_list.append((pt_start[0] + (pt_end[0] - pt_start[0]) * multiplier / (nodes_number - 1),
                            pt_start[1] + (pt_end[1] - pt_start[1]) * multiplier / (nodes_number - 1)))
        pt_list.append(pt_end)
        for idx in range(1, len(pt_list)):
            fragmentation(cathala(pt_list[idx-1]), cathala(pt_list[idx]))


for i in range(len(p_list)):
    for j in range(len(p_list)):
        if i != j:
            fragmentation(p_list[i], p_list[j])

print(len(points_list))
left, right, top, bottom = -1.49, 0.85, 1.36, -0.89
height, width = 1200, 1200

img = Image.new('RGB', (width, height))
pixels = img.load()

x_div, y_div = right - left, top - bottom
for x, y in points_list:
    x_pixel = round(((x - left) / x_div) * width)
    y_pixel = round(((top - y) / y_div) * height)
    pixels[x_pixel, y_pixel] = (255, 255, 0)

font = ImageFont.truetype("arial.ttf", size=50)
ImageDraw.Draw(img).text((2 * width // 3, 10), f"Cathala\nnodes = {nodes_number}", font=font)
img.show()
# img.save(f'output/cathala_pil_h{h}_nodes{nodes_number}.png')
# img.save(f'output/cathala_pil_pivot_h{h}_nodes{nodes_number}.png')
