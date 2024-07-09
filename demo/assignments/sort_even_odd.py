evens = []
odds = []

while True:
    num = int(input("Enter a number [0 to stop]:"))
    if num == 0:
        break

    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

evens.sort()
odds.sort()

for n in evens + odds:
    print(n, end=' ')
