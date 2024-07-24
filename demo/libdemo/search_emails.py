try:
    f = open("emails.txt", "rt")
except:
    print("Sorry! File not found!")
    exit(1)

name = input("Enter name :")

while True:
    line = f.readline()
    if len(line) == 0:  # EOF
        print("Sorry! Name not found!")
        break

    if '@' not in line:  # ignore line if it doesn't have @
        continue

    uname, server = line.split("@")
    if uname == name:
        print(line)
        break

f.close()

f.close()
