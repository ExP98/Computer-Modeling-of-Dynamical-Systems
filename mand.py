from PIL import Image
import numpy as np


h, w = 600, 600
border = 1.5
img = Image.new('RGB', (w, h))
pixels = img.load()
max_iter, curr_iter = 300, 0
for x, re in enumerate(np.linspace(-border, border, w)):
    for y, im in enumerate(np.linspace(-border, border, h)):
        c = re + 1j * im
        z = 0
        for i in range(max_iter):
            curr_iter = i
            z = z ** 3 + c
            if abs(z) > 2:
                # pixels[x, y] = (i, i, i)    # only borders
                break
        pixels[x, y] = (curr_iter, curr_iter, curr_iter)
img.show()
# img.save('ex3/mand.png')
