# Take 5 numbers or until 0 is given and display average

total = count = 0
for i in range(5):
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break
    total += num
    count += 1      # count = count + 1

print(f"Average = {total/count}")
