def get_largest_length(*names):
    largest_length = 0
    for name in names:
        if len(name) > largest_length:
            largest_length = len(name)

    return largest_length


largest_len = get_largest_length("Java", "Python", "C", "C#", "JavaScript")
print(largest_len)
