import timeit as t

# function taking a function and arguments executing this function with given arguments and measuring the time of execution
# par: func - function to be executed; x - first argument; a - second argument
# returns: value of function, duration of function work time
def fspeed(func, x, a):
    start = t.default_timer()
    val = func(x, a)
    stop = t.default_timer()
    dur = stop - start

    return val, dur


def trulin(x, a):
    return a*x

def powa(x,a):
    return x**a

v, d = fspeed(trulin, 2, 2)
v2, d2 = fspeed(powa, 2, 2)

print('Value {0} and duration {1} s'.format(v, d))
print('Value {0} and duration {1} s'.format(v2, d2))
