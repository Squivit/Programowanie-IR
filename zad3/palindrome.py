import sys

words = sys.argv[1:]

use = [x for x in words if x.__contains__('/') or x.__contains__('-')]
switch = False

print(type(words))
print(use)

for u in use:
    if u == '/a' or u == '/all' or u == '-all' or u == '-a':
        print(words.__contains__(u))
        words = words.remove(u)
        switch = True


palidromes = words
dromes = []
for w in sys.argv[1:]:
    for i in range(len(w)):
        if w[i] != w[-i-1]:
            palidromes.remove(w)
            if switch:
                dromes.append(w)
            break

print(palidromes)
if switch:
    print(dromes)