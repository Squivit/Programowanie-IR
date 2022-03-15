def coll(k):
    list =[int(k)]
    i = int(assign(k))
    while i != 1:
        list.append(i)
        i = int(assign(i))
    list.append(1)
    return list


def assign(k):
    if k % 2 == 1:
        return 3 * k + 1
    else:
        return k / 2


print(coll(127))