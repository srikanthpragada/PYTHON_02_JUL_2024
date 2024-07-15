g = 100  # Global variable


def f1():
    global g
    a = 1
    g = g + 1

    # Local function
    def f2():
        nonlocal a
        b = 2
        a = a + 1
        print(g, a, b)

    f2()
    print(a)  # ?


f1()
