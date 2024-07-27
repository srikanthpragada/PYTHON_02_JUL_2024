from datetime import *

f = open("players.txt", "rt")
players = []
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue
    try:
        dob = datetime.strptime(parts[1], "%d-%m-%Y")
        years = (datetime.today() - dob).days // 365
        players.append((parts[0], years))
    except:
        pass

f.close()

for (name, age) in sorted(players, key=lambda t: t[1]):
    print(f"{name:20}  {age:2}")
