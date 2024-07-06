# Find largest of 5 numbers

largest = 0
for i in range(5):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num

print(f"The largest number is {largest}")
