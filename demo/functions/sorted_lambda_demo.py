code = ['a123', 'e345', 'd12', 'c56', 'f1234', 'a5678']
for n in sorted(code, key=lambda v: int(v[1:])):
    print(n, end=' ')
