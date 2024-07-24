
f = open("marks.txt", "rt")

for line in f.readlines():
    if len(line.strip()) == 0:
        continue

    parts = line.split(",")
    name = parts[0]
    total = sum(map(int, parts[1:]))
    print(f"{name:15} {total:3}")

f.close()