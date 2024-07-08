# Take 2 numbers and print their factors

n1, n2 = 24, 50

smallest = n1 if n1 < n2 else n2

for n in range(2, smallest // 2 + 1):
    if n1 % n == 0 and n2 % n == 0:
        print(n, end=' ')
