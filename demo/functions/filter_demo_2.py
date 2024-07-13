def hasUpper(st):
    for c in st:
        if c.isupper():
            return True

    return False


def hasNoUpper(st):
    return not hasUpper(st)


names = ['Jason', 'Scott', 'ben', 'joe', 'Larry']

for n in filter(hasUpper, names):
    print(n)

for n in filter(hasNoUpper, names):
    print(n)
