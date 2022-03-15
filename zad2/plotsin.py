import numpy as np
import matplotlib.pyplot as plt


def frange(a, b, d):
    return np.arange(a, b, d)

print(frange(0, 1, 0.1))


def plotf(func, a, b, d):
    x = frange(a, b, d)
    plt.axes(xlabel='Argumenty x', ylabel='Wartość funkcji')
    plt.title('Wykres funkcji')
    plt.plot(x, func(x))
    plt.show()



def fun(x):
    return x*np.sin(x) - x**2


plotf(fun, -10, 10, 0.1)