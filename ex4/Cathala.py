from PIL import Image
import numpy as np

x, y = -0.5, 0.7
p1, p2 = 0.7, -0.82

height, width = 1200, 1200
img = Image.new('RGB', (width, height))
pixels = img.load()
points_list = []

for j in range(1000000):
    x, y = p1 * x + y, p2 + x * x
    points_list.append((x, y))

left, right, top, bottom = -1.49, 0.85, 1.36, -0.89
x_div, y_div = right - left, top - bottom
mx = np.zeros((height, width))

for x, y in points_list:
    x_pixel = round(((x - left) / x_div) * width)
    y_pixel = round(((top - y) / y_div) * height)
    mx[x_pixel, y_pixel] += 1

for x_coord in range(width):
    for y_coord in range(height):
        color = int(mx[x_coord, y_coord] * 200)
        pixels[x_coord, y_coord] = (color, color, 0)


# reduce the number of iterations to 100000 for the following code (10 times less)
# ind = np.argsort(mx, axis=None)[::-1][:500]
# true_ind = []
# true_coords = []
# for i in ind:
#     row = int(i // width)
#     col = int(i % width)
#     new_x = row / width * (right - left) + left
#     new_y = top - col / height * (top - bottom)
#     true_ind.append((row, col))
#     true_coords.append((new_x, new_y))
# print(true_ind)
# print(true_coords)
# tc = np.array(true_coords)
# np.savetxt('test.out', tc, delimiter=';')
# for ind in true_ind:
#     _x, _y = ind
#     pixels[_x, _y] = (255, 0, 0)
#     pixels[_x+1, _y] = (255, 0, 0)
#     pixels[_x-1, _y] = (255, 0, 0)
#     pixels[_x, _y+1] = (255, 0, 0)
#     pixels[_x, _y-1] = (255, 0, 0)
#
#     pixels[_x+1, _y+1] = (255, 0, 0)
#     pixels[_x+1, _y-1] = (255, 0, 0)
#     pixels[_x-1, _y+1] = (255, 0, 0)
#     pixels[_x-1, _y-1] = (255, 0, 0)

img.show()
# img.save('output/cathala_real.png')