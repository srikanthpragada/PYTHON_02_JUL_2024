# print factors for given numbers on command line
import sys

if len(sys.argv) < 2:
    print("Usage : python factors.py  number1 [number2] ...")
    exit(1)

for n in sys.argv[1:]:
    print(f"{n:4}", end=' -> ')
    if not n.isdigit():   # not a number
        print('Not a valid number!')
    else:
        n = int(n)
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                print(i, end=' ')

        print()  # go to next line
