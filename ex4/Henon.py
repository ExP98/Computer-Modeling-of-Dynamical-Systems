from PIL import Image
from math import cos, sin, pi

x, y = 0.6, 0.459
# x, y = 0.62, 0.359
p1 = 6

h, w = 600, 600
b = 0.85
img = Image.new('RGB', (w, h))
pixels = img.load()

for j in range(10000):
    angle = 2 * pi / p1
    x, y = -(y - x**2) * sin(angle) + x * cos(angle), (y - x**2) * cos(angle) + x * sin(angle)
    pixels[round((x + b) * w / 2 / b), round(-(y + b) * h / 2 / b)] = (255, 255, 0)
# img.show()
img.save('output/henon_2.png')
