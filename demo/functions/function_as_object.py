a = 100
b = a

print(id(a), id(b))


def fun():
    print("Function")


fun2 = fun

fun()
fun2()