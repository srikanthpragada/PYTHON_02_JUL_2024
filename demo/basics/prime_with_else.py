# Whether number is prime

num = int(input("Enter a number :"))
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print("Not a Prime Number!")
        break
else:
    print("Prime Number")
