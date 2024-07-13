names = ['jason', 'scott', 'Ben', 'Joe', 'Larry', 'Li']

for n in sorted(names):
    print(n, end=' ')

print()

for n in sorted(names, key=len):
    print(n, end=' ')
