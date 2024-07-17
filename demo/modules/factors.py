# print fators for given numbers on command line

import sys

if len(sys.argv) < 2:
    print("Usage : python factors.py  number1 [number2] ...")
    exit(1)

nums = filter(str.isdigit, sys.argv[1:])  # select only numbers

for n in map(int, nums):
    print(f"{n:4}", end=' -> ')
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(i, end=' ')

    print()  # go to next line
