import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

w, h = 128, 128
initial_text = "10"
matrix = np.random.random_sample((h, w))

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.2)
ax.imshow(matrix, vmin=0, vmax=1)

def submit(text, mtr=matrix):
    coef = float(text)
    matrix = mtr * coef
    for i in range(h):
        for j in range(w):
            if matrix[i, j] > 1:
                matrix[i, j] = 1
    ax.imshow(matrix)
    ax.set_title(str(coef))
    plt.draw()

textbox_add = plt.axes([0.55, 0.05, 0.22, 0.075])
text_box = TextBox(textbox_add, 'Parameter', initial=initial_text)
text_box.on_submit(submit)

# addPlot(graph_axes, current_sigma, current_mu)

plt.show()

