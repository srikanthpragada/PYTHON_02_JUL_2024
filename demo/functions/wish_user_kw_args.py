def wish(user: str, message: str) -> None:
    print(message, user)


# Positional
wish('Larry', "Hi")

# Keyword
wish(message="Hello", user="Bob")

# Mixed
wish("Jack", message="Hi")
