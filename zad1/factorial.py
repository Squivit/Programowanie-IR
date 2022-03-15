import timeit as t

# calculates the factorial of natural number n
# returns: factorial value
def ifactorial(n):
    i = 0 
    f = 1
    while i != n:
        i += 1
        f = fact(i, f)
    return f    


def fact(n, fac):
    return fac*n

print(ifactorial(7))

def rfactorial(n):
    return next_factorial(1,n,1)

def next_factorial(start, finish, fac):
    f = fac * start
    if start != finish:
        f = next_factorial(start+1, finish, f)
    return f

print(rfactorial(7))

def factorial(n):
    start = t.default_timer()
    fi = ifactorial(n)
    dur1 = t.default_timer() - start

    start = t.default_timer()
    fr = rfactorial(n)
    dur2 = t.default_timer() - start

    return fi, fr, dur1, dur2

fi, fr, dur1, dur2 = factorial(10)
print('Silnia z 10 wynosi: {0} = {1}, czas wykonywania operacji: iter: {2}, rek: {3}'.format(fi,fr,dur1,dur2))