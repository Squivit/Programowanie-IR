import timeit

a = 4
b = 72

start = timeit.default_timer()

s = a+b

stop = timeit.default_timer()
duration1 = stop - start

start = timeit.default_timer()

p = a*b

duration2 = timeit.default_timer() - start

print('Czas dodawania {0} s, czas mnożenia {1} s, różnica czasów {2} s'.format(duration1, duration2, duration2 - duration1))