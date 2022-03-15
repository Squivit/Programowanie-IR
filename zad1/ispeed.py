import timeit as t

def ispeed(func, *pars):
    vals = []
    durs = []
    for par in pars:
        sum = 0
        for i in range(0, 5):
            start = t.default_timer()
            func(par)
            sum += t.default_timer() - start
        av = sum/5
        vals.append(func(par))
        durs.append(av)

    print('Values: {0}, durations: {1}'.format(vals, durs))

def pow2(x):
    return x**2

ispeed(pow2, 4, 2, 7, 11, 75)