def remove_character(string_value, character_value=' '):
    return string_value.replace(character_value, "")


print(remove_character("Python is a high-level programming language"))
print(remove_character("hello", "l"))

