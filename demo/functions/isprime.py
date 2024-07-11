def isprime(num):
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            return False

    return True


print(isprime(11), isprime(255))
