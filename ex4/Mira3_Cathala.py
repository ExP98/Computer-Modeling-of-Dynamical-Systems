from PIL import Image
import matplotlib.pyplot as plt

x, y = -0.5, 0.7
# p1, p2 = 1, -0.5952   # Mira3
p1, p2 = 0.7, -0.82     # Cathala

# ------------ мгновенное вычисление и показ ------------
h, w = 600, 600
img = Image.new('RGB', (w, h))
pixels = img.load()

for j in range(10000):
    x, y = p1 * x + y, p2 + x * x
    pixels[x * 150 + w / 2, h / 2 - y * 150] = (255, 255, 0)
# img.show()
img.save('output/cathala.png')

# # ------------ пошаговое вычисление и показ ------------
# plt.ion()
# plt.suptitle("Cathala")
# plt.text(0.5, 1.2, f"p1 = {p1}\np2 = {p2}")
#
# for j in range(100):
#     x_list = []
#     y_list = []
#     # для более быстрой работы обновление графика происходит каждые 100 новых точек
#     for i in range(100):
#         x, y = p1 * x + y, p2 + x * x
#         x_list.append(x)
#         y_list.append(y)
#     plt.scatter(x_list, y_list, s=1, c='k')
#
#     plt.draw()
#     plt.gcf().canvas.flush_events()
# print('end')
# plt.ioff()
# plt.show()
