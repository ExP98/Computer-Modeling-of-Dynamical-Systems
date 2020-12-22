import numpy as np
import matplotlib.pyplot as plt

'''
Найти приближения к периодическим орбитам функции Ньютона для функции
f(z)=z^3+(A-1)z-A, для значений параметра A=0.310+1.620i; (период 2) A=0.275+1.650i (период 4)
'''
A, per = (0.310 + 1.620j), 2
# A, per = (0.275 + 1.650j), 4


def func(_z):
    return _z ** 3 + (A - 1) * _z - A


def der_func(_z):
    return 3 * _z ** 2 + A - 1


def N_func(_z):
    return _z - func(_z) / der_func(_z)


h, w = 600, 600
xa, xb = 0.75, 1.5
ya, yb = -0.25, 0.5


def plot_newton(eps, ax):
    matrix = np.zeros((w, h))

    for x, re in enumerate(np.linspace(xa, xb, w)):
        for y, im in enumerate(np.linspace(ya, yb, h)):
            z = re + 1j * im
            if abs(N_func(z) ** per - z) < eps:
                matrix[x, y] = 1

    ax.imshow(matrix)
    ax.set_title(f"eps = {eps}")
    ax.set_xticks([])
    ax.set_yticks([])
    return ax


e = [0.1, 0.075, 0.05, 0.025, 0.01, 0.005]
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(11.69, 8.27))
fig.suptitle(f"Newton, period {per}, A = {A}")
for i, axs in enumerate(axes.flat):
    plot_newton(e[i], axs)
# fig.savefig('ex5/newton_per' + str(per) + '.png')
plt.show()
