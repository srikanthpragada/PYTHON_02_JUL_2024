# Find largest of numbers given until 0

largest = 0
while True:
    num = int(input("Enter a number [0 to stop]: "))
    if num == 0:
        break
    if num > largest:
        largest = num

print(f"The largest number is : {largest}")
