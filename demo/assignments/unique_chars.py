names = ['java', 'javascript', 'c', 'sql', 'python']

chars = set()

for n in names:
    chars = chars | set(n)

print(chars)
