def extract_nonalpha(st):
    ns = []
    for c in st:
        if not (c.isalpha() or c.isspace()):
            ns.append(c)

    return ns


names = ["java 22", 'python  3.12', 'JavaScript 2018']

for n in map(extract_nonalpha, names):
    print(n)

for n in map(len, names):
    print(n)