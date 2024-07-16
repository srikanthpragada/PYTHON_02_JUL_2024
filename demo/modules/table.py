# Take a number from command line and display table
import sys
if len(sys.argv) < 2:
    print("Missing number. Please rerun with number as follows!")
    print("Usage : python table.py  <number>  [length]")
    exit(1)

if len(sys.argv) > 2:
    length = int(sys.argv[2])
else:
    length = 10   # Def length

num = int(sys.argv[1])
for n in range(1, length + 1):
    print(f"{num:3} * {n:2} = {num * n:6}")
