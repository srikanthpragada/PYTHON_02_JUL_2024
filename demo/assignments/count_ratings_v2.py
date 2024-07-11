ratings = [1, 1, 2, 3, 4, 5, 3, 2, 1, 4, 5, 5, 3, 2, 1]

counts = {}

for r in ratings:
    counts[r] = counts.get(r, 0) + 1

print(counts)