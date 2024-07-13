nums = [10, -20, 55, 30, -44, 5, 5, 9, -3]

for n in filter(lambda v: v > 0, nums):
    print(n, end=' ')
