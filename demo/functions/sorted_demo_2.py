def extract_2_chars(st):
    return st[:2].upper()


def extract_number(st):
    return int(st[1:])


names = ['jason', 'scott', 'Ben', 'Joe', 'Larry', 'Li']
code = ['a123', 'e345', 'd12', 'c56', 'f1234', 'a5678']

# for n in sorted(names, key=extract_2_chars):
#     print(n, end=' ')


for n in sorted(code, key=extract_number):
    print(n, end=' ')
