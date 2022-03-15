

#oblicza n-ty wyraz ciągu fibonacciego
def fib(n):
    if n==1 or n == 2:
        return 1
    else:
        p, o = 1, 1
        i = 3
        while i < n:
            p, o = o, p + o
            i += 1
        return o + p


def fibsum():
    s = 0
    i = 1
    k = 0
    while k < 3000000:
        k = fib(2*i)
        i += 1
        if k<3000000:
            s += k
    return s

print(fib(4))