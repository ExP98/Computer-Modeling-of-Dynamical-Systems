import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

w, h = 100, 100
# cp in [0; 1000], gn in [250; 1000]
gn, cp = 631, 711
r = gn / 250
img = Image.new('RGB', (w, h))
pixels = img.load()
matrix = np.random.random_sample((h, w))
print(matrix)

for k in range(15):
    copy_m = np.copy(matrix)
    for i in range(h):
        for j in range(w):
            avg = (copy_m[i - 1, j] + copy_m[(i + 1) % h, j] + copy_m[i, j - 1] + copy_m[i, (j + 1) % w]) / 4
            c = cp * (avg - copy_m[i, j]) / 1000
            x = r * copy_m[i, j] * (1 - copy_m[i, j]) + c
            if x > 1:
                matrix[i, j] = 1
            elif x < 0:
                matrix[i, j] = 0
            else:
                matrix[i, j] = x
            clr = int(matrix[i, j] * 255)

            pixels[i, j] = (clr, clr, 0)
    print(matrix)
    img.show()

print('end')
