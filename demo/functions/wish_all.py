def wish(*names, message='Hi'):
    for n in names:
        print(message, n)


wish('Jack', 'Mark', 'Tom')
wish('Andy', "Jessy", message="Hello")
