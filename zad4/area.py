import sys
import math as m

argv = sys.argv[1:4]

class NieTrojkat(Exception):
    pass

def calc_area(a, b ,c):
    p = (a+b+c)/2
    return m.sqrt(p*(p-a)*(p-b)*(p-c))

a, b, c = argv
try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    print('wrong type')
else:
    try:
        if a < 0 or b < 0 or c < 0:
            raise NieTrojkat
        elif a + b < c or a + c < b or b + c < a:
            raise NieTrojkat 
    except NieTrojkat:
        print('Z podanych długości boków nie skonstruujesz trójkąta!')
    except:
        print('no')
    else:
        print(f'Pole trójkąta wynosi: {calc_area(a,b,c)}')