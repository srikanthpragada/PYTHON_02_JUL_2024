st = "how do you do today"

charfreq = {}
for c in st:
    charfreq[c] = st.count(c)

print(charfreq)

charfreq = {}
for c in set(st):
    charfreq[c] = st.count(c)

for char, count in sorted(charfreq.items()):
    print(char, count)


