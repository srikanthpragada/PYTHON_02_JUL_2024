data = [(1, 80), (1, 89), (2, 50), (2, 60), (3, 45), (1, 60), (3, 44)]

students = {}

for rollno, marks in data:
    students[rollno] = students.get(rollno, 0) + marks

for rollno, total in sorted(students.items()):
    print(f"{rollno:3}  {total:3}")
