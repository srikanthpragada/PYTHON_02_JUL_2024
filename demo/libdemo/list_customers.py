import re

f = open("customers.txt", "rt")

for line in f.readlines():
    m = re.search(r"\d+", line)
    if m is not None:
        print(m.group())


f.close()

