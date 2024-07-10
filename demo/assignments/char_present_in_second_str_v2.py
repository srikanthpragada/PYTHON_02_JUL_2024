s1 = "abcbbdea"
s2 = "befgha"

chars_used = []
for c in s1:
    if c not in chars_used:
        if c in s2:
            print(c)

        chars_used.append(c)
