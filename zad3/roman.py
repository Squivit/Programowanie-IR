import sys

R_TO_A_DICT = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
A_TO_R_DICT = {1000 : 'M', 500 : 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

def arabic_to_roman(w):
    w = int(w)
    m = ''
    if w > 5000:
        print('no')
        return 0
    while w > 999:
        m += A_TO_R_DICT[1000]
        w -= 1000
    if w > 899:
        m += A_TO_R_DICT[100] + A_TO_R_DICT[1000]
        w -= 900
    while w > 499:
        m+= A_TO_R_DICT[500]
        w -= 500
    if w > 399:
        m += A_TO_R_DICT[100] + A_TO_R_DICT[500]
        w -= 400
    while w > 99:
        m += A_TO_R_DICT[100]
        w -= 100
    if w > 89:
        m += A_TO_R_DICT[10] + A_TO_R_DICT[100]
        w -= 90
    while w > 49:
        m += A_TO_R_DICT[50]
        w -= 50
    if w > 39:
        m += A_TO_R_DICT[10] + A_TO_R_DICT[50]
        w -= 40
    while w > 9:
        m += A_TO_R_DICT[10]
        w -= 10
    if w == 9:
        m += A_TO_R_DICT[1] + A_TO_R_DICT[10]
        w -= 9
    while w > 4:
        m += A_TO_R_DICT[5]
        w -= 5
    if w == 4:
        m += A_TO_R_DICT[1] + A_TO_R_DICT[5]
        w -= 4
    while w > 0:
        m += A_TO_R_DICT[1]
        w -= 1
    print(m)

def roman_to_a(w):
    n = sum([R_TO_A_DICT[x] for x in w])
    print(n)

argv = sys.argv[1:]

t = argv[0]
w = argv[1]

if t == 'a':
    roman_to_a(w)
elif t == 'r':
    arabic_to_roman(w)