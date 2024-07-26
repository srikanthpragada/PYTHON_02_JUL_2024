import re

with open("text.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"\w+", contents)

for w in sorted(set(words), key=str.upper):
    print(f"{w:15}  {words.count(w):2}")
