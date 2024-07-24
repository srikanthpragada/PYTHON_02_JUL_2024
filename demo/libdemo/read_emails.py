with open("emails.txt", "rt") as f:
    for line in sorted(f.readlines()):
        print(line.strip())

