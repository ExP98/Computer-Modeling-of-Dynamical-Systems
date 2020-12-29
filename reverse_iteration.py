from PIL import Image, ImageDraw

c_list = [(-0.7055, -0.3842)]
# c_list = [(-0.7055, -0.3842), (-0.22, -0.74), (-0.8, 0.156), (-0.7, 0.27015), (0.285, 0.01), (-0.0085, 0.71), (-0.12375, 0.56508), (-0.12, 0.74), (-0.39054, -0.58679), (-1.25, 0.0), (0.11031, -0.67037), (-0.194, 0.6557)]
w, h = 1000, 1000
border = 2


def calculation(_z, _c, ctr):
    new_z = (_z - _c) ** 0.5
    points_list.append(new_z)
    points_list.append(-new_z)
    ctr += 1
    if ctr < 20:
        calculation(new_z, _c, ctr)
        calculation(-new_z, _c, ctr)


def visualization_rev(_c):
    calculation(_c, _c, 0)

    img = Image.new('RGB', (w, h))
    pixels = img.load()
    mx = [[0 for _ in range(w)] for _ in range(h)]
    for pt in points_list:
        x = round((pt.real / (2 * border) + 0.5) * w)
        y = round((pt.imag / (2 * border) + 0.5) * h)
        mx[x][y] += 1
    for x_coord in range(w):
        for y_coord in range(h):
            color = mx[x_coord][y_coord]
            pixels[x_coord, y_coord] = (color, color, color)
    ImageDraw.Draw(img).text((10, h - 20), f"Julia, c = {_c}", (255, 255, 255))
    img.show()
    # img.save('reverse_iter/rev_' + str(_c) + '.png')


for c in c_list:
    points_list = []
    visualization_rev(c[0] + 1j * c[1])
