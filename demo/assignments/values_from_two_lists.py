# Assume we have 2 lists and display the corresponding values for the both the lists but if the corresponding value not present display null.
# First list can be bigger than second.

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30]

for idx, v in enumerate(l1):
    if idx < len(l2):
        print(v, l2[idx])
    else:
        print(v, 'Null')
