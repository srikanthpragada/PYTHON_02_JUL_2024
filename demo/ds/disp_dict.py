d = {1 : 'Java', 2 : 'Python',  3 : 'JavaScript'}

for key in iter(d):
    print(key, d[key])

for key in d.keys():
    print(key, d[key])

for key, value in d.items():
    print(key, value)