def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def showall(*args, **kwargs):
    print(args)
    print(kwargs)


show(a=10, b=20, name='Python')
show(x=1, y=2, z=30)
showall(10, 20, x=1, y=2)
showall()

