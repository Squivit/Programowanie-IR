import numpy as np
import matplotlib.pyplot as plt


def frange(a, b, d):
    return np.arange(a, b, d)


def trigplot(a, b, d):
    x = frange(a, b, d)
    plt.plot(x, x, c='blue')
    plt.plot(x, np.tan(x), c = 'red')
    plt.plot(x, np.sin(x), c = 'green')
    plt.legend(['y = x', 'y = tg(x)', 'y = sin(x)'])
    plt.show()

trigplot(-3.14, 3.14, 1)