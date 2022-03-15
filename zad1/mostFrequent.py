

list = [1, 2, 3, 4, 5 , 6, 5, 4, 5, 4,3, 5, 1, 2]

def box(pack):
    v = 0
    c = 0
    for cig in pack:
        if pack.count(cig) > c:
            c = pack.count(cig)
            v = cig
    return v, c

v, c = box(list)
print('W danej liście %s pojawiło się %d razy' % (v,c))