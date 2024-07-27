from datetime import *

f = open("players.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue
    try:
        dob = datetime.strptime(parts[1], "%d-%m-%Y")
        years = (datetime.today() - dob).days // 365

        print(f"{parts[0]:20}  {years:2}")
    except:
        pass

f.close()



