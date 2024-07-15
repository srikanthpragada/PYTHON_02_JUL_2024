def fun(a):
    print(id(a))
    a = 0
    print(id(a))


v = 100
print(id(v))
fun(v)
print(v)

