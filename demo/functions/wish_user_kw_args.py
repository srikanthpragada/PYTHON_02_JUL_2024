def wish(user, message):
    print(message, user)


# Positional
wish('Larry', "Hi")

# Keyword
wish(message="Hello", user="Bob")

# Mixed
wish("Jack", message="Hi")
