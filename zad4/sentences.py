import sys
import re

text = open(sys.argv[1],'r').read()

sent = re.split('\.|\!|\?', text)
t = []
for s in sent:
    t.append(s.capitalize())
print(t)