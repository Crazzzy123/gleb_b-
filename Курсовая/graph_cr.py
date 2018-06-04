import pylab
import numpy as np
import numexpr as ne  # парсит ввод
import matplotlib.pyplot as plt  # рисует график
from matplotlib import mlab  # делает интервал

import calculate_graph as calc

marker = None
marker_x = None
marker_y = None


def onMouseClick(event):
    """Реагирует на клик мыши по графику"""
    axes = event.inaxes

    # Если кликнули вне графика, то не будем ничего делать
    if axes is None:
        return

    global marker
    global marker_x
    global marker_y
    # Если маркер с текстом уже был создан, то удалим его и все остальные
    if marker is not None:
        marker_x.remove()
        marker_y.remove()
        marker.remove()

    # В качестве текущих выберем оси, внутри которых кликнули мышью
    pylab.sca(axes)

    # Координаты клика в системе координат осей
    xx = event.xdata
    yy = event.ydata
    text = u'({:.3f}; {:.3f})'.format(xx, yy)

    # Выведем текст в точку, куда кликнули и рисуем перекрестье
    marker = pylab.text(xx, yy, text)
    marker_x = pylab.axvline(x=xx, c='r')
    marker_y = pylab.axhline(y=yy, c='r')

    # Обновим график
    pylab.show()


if __name__ == '__main__':
    # готовим данные для графика
    xmin = -20.0
    xmax = 20
    dx = 0.01
    x = mlab.frange(xmin, xmax, dx)  # определяем интервал для графика и шаг
    print(len(x))
    f = input('f(x)=')  # вводим функию
    y = calc.start_calculate(f, xmin, xmax, dx)
    # Создадим окно с графиком
    fig = pylab.figure()

    # Нарисуем график
    pylab.plot(x, y, linewidth=1.5)  # парсим ввод и заготавливаем график
    plt.xlabel('x')  # подписываем оси и легенду
    plt.ylabel('y')
    plt.legend(['График функции: f(x) = {}'.format(f)])
    pylab.grid()

    # Подписка на событие
    fig.canvas.mpl_connect('button_press_event', onMouseClick)

    pylab.show()  # рисуем график