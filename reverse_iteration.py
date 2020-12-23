from PIL import Image

c = 0.285 + 0.01j

counter = 0
points_list = []


def calculation(_z, ctr):
    new_z = (_z - c) ** 0.5
    points_list.append(new_z)
    points_list.append(-new_z)
    ctr += 1
    if ctr < 20:
        calculation(new_z, ctr)
        calculation(-new_z, ctr)


calculation(c, counter)

w, h = 1000, 1000
img = Image.new('RGB', (w, h))
pixels = img.load()

mx = [[0 for _ in range(w)] for _ in range(h)]
for pt in points_list:
    x = round((pt.real / 3 + 0.5) * w)
    y = round((pt.imag / 3 + 0.5) * h)
    mx[x][y] += 1
for x_coord in range(w):
    for y_coord in range(h):
        color = mx[x_coord][y_coord]
        pixels[x_coord, y_coord] = (color, color, color)
img.show()
# img.save('reverse_iter/rev_20_coloring.png')
