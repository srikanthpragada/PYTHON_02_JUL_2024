
f = open("marks.txt", "rt")

for line in f.readlines():
    if len(line.strip()) == 0:
        continue

    parts = line.split(",")
    name = parts[0]
    valid_marks = filter(str.isdigit, parts[1:])
    marks = list(map(int, valid_marks))
    count = len(marks)
    total = sum(marks)
    print(f"{name:15} {total:3}  {total/count:5.2f}")

f.close()