import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return 3*(x-1)

def f2(x):
    return 3*(x-1)*(x-2)

def f3(x):
    return 3*(x-1)*(x-2)*(x-3)

def f4(x):
    return 3*(x-1)*(x-2)*(x-3)*(x-4)

def f5(x):
    return 3*(x-1)*(x-2)*(x-3)*(x-4)*(x-5)

x = np.arange(1, 5, .05)

plt.title('Wielomiany')
plt.plot(x, f1(x), c = 'blue')
plt.plot(x, f2(x), c = 'green')
plt.plot(x, f3(x), c = 'red')
plt.plot(x, f4(x), c = 'black')
plt.plot(x, f5(x), c = 'violet')
plt.legend(['f1', 'f2','f3','f4','f5'])

plt.show()