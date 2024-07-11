ratings = [1, 1, 2, 3, 4, 5, 3, 2, 1, 4, 5, 5, 3, 2, 1]

counts = {}

for r in set(ratings):
    counts[r] = ratings.count(r)

print(counts)