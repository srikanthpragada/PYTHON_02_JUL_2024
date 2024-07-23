def numbers():
    for n in range(1, 4):
        yield n


def password():
    while True:
        # generate password
        yield "password"


n = numbers()
print(n)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
