# Display average of positive numbers
total = 0
count = 0
while True:
    num = int(input("Enter a number [0 to stop]:"))
    if num == 0:
        break
    if num > 0:
        total += num
        count += 1

print(f"The average of positive digits is {total / count}")