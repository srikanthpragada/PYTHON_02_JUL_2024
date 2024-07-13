def ispositive(n):
    return n > 0


nums = [10, -20, 55, 30, -44, 5, 5, 9, -3]

for n in filter(ispositive, nums):
    print(n, end=' ')
