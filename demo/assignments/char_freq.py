st = "how do you do"

char_used = []
for c in st:
    if c not in char_used:
        print(c, st.count(c))
        char_used.append(c)
