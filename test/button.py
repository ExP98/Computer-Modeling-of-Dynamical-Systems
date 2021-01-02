import numpy
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider


def gauss(param1, param2, x):
    '''Отображаемая фукнция'''
    return (1.0 / (param1 * numpy.sqrt(2.0 * numpy.pi)) *
            numpy.exp(-((x - param2) ** 2) / (2 * param1 * param1)))


def addPlot(graph_axes, param1, param2):
    '''Добавить график к осям'''
    x = numpy.arange(-5.0, 5.0, 0.01)
    y = gauss(param1, param2, x)
    graph_axes.clear()
    graph_axes.grid()
    graph_axes.plot(x, y)


    # Нужно для обновления графика
    plt.draw()


if __name__ == '__main__':
    def onButtonAddClicked(event):
        '''Обработчик события для кнопки "Добавить"'''
        # Будем использовать param1 и param2, установленные с помощью слайдеров
        global slider_param1
        global slider_param2
        global graph_axes

        # Используем атрибут val, чтобы получить значение слайдеров
        addPlot(graph_axes, slider_param1.val, slider_param2.val)

    # Создадим окно с графиком
    fig, graph_axes = plt.subplots()
    graph_axes.grid()

    # Оставим снизу от графика место для виджетов
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    # Создание кнопки "Добавить"
    axes_button_add = plt.axes([0.55, 0.05, 0.4, 0.075])
    button_add = Button(axes_button_add, 'Добавить')
    button_add.on_clicked(onButtonAddClicked)

    # Создание слайдера для задания param1
    axes_slider_param1 = plt.axes([0.05, 0.25, 0.85, 0.04])
    slider_param1 = Slider(axes_slider_param1,
                          label='σ',
                          valmin=0.1,
                          valmax=1.0,
                          valinit=0.5,
                          valfmt='%1.2f')

    # Создание слайдера для задания param2
    axes_slider_param2 = plt.axes([0.05, 0.17, 0.85, 0.04])
    slider_param2 = Slider(axes_slider_param2,
                       label='μ',
                       valmin=-4.0,
                       valmax=4.0,
                       valinit=0.0,
                       valfmt='%1.2f')

    plt.show()