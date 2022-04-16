import sys

content = sys.argv[1]
file = open(content, 'r').read()
alfabet = 'abcdefghijklmnoprstuvwxyz'

count = [file.count(a) for a in alfabet]
print(count)

import matplotlib.pyplot as plt


plt.plot([*alfabet], count, ls='', marker='.')
plt.show()