# Positional only args
def wish(user, message, /):
    print(message, user)


# Positional
wish('Larry', "Hi")

# Keyword
#wish(message="Hello", user="Bob")


