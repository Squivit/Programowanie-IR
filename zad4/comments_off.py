import sys

comment_s = sys.argv[1][0]
file_source = sys.argv[2]
file_print = sys.argv[3]

f = open(file_print, 'w')

for line in open(file_source, 'r').readlines():
    if line[0] != comment_s:
        f.write(line)

f.close()
