from PIL import Image, ImageFont, ImageDraw
import numpy as np

h, w = 100, 100
img = Image.new('RGB', (w, h))
# draw = ImageDraw.Draw(img)
pixels = img.load()
num, blob_size = 50, 10
for x in range(-blob_size, blob_size):
    for y in range(-blob_size, blob_size):
        pixels[num+x, num+y] = (100000, 255, 0)
ImageDraw.Draw(img).text((0, 90), f"Julia, w {w}, h = {h}", (255, 255, 255))
img.show()