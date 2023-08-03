import re

fh = open('mbox.txt')

for line in fh:
    line = line.rstrip()
    if re.search('^From :', line):
        print(line)
