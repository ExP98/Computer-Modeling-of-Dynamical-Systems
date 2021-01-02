import matplotlib.pyplot as plt

x, y = 0.01, 0.01
p1, p2, p3 = 2.68, -0.1, 0.9

# ------------ пошаговое вычисление и показ ------------
plt.ion()
plt.suptitle("Mira1")
plt.text(-0.75, 0.5, f"p1 = {p1}\np2 = {p2}\np3 = {p3}")

for j in range(100):
    x_list = []
    y_list = []
    # для более быстрой работы обновление графика происходит каждые 100 новых точек
    for i in range(100):
        x, y = (1 - p1) * x + y, p1 * p2 * x + p3 * y - p1 * x ** 3
        x_list.append(x)
        y_list.append(y)
    plt.scatter(x_list, y_list, s=1, c='k')

    plt.draw()
    plt.gcf().canvas.flush_events()
print('end')
plt.ioff()
plt.show()
