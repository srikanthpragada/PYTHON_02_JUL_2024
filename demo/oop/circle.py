class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Radius = {self.radius}"

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        # print(">")
        return self.radius > other.radius

    def __int__(self):
        return self.radius

    def __mul__(self, other):
        return Circle(self.radius * other)


c1 = Circle(10)
c2 = Circle(10)
c3 = Circle(20)

print(c1)
print(str(c1))  # c1.__str__()
print(c1 == c2)  # c1.__eq__(c2)
# print(c1 > c3)
# print(c1 < c3)

print(int(c1) + int(c2))  # c1.__int__()

circles = [c1, c2, c3, Circle(5), Circle(15)]

for c in sorted(circles):
    print(c)

nc = c1 * 3   # c1.__mul__(3)
print(nc)