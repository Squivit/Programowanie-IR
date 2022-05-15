memo = {1: 1, 2: 1}

def fiblambda(n):
    n = int(n)
    f = []
    y = lambda i: memo[i-1] + memo[i]
    for i in range(1, n+1):
        if i not in memo.keys():
            k = max(memo.keys())
            for span in range(k, i):
                memo[span + 1] = y(span)
        f.append(memo[i])
    return f

def fibSum(n):
    return sum(fiblambda(n))

def fibOdd(n):
    return [a for a in fiblambda(n) if a % 2 == 1]

def fibEven(n):
    return [a for a in fiblambda(n) if a % 2 == 0]
    

import sys

_n = sys.argv[1]

print(fiblambda(_n))
print(fibSum(_n))
print(fibOdd(_n))
print(fibEven(_n))