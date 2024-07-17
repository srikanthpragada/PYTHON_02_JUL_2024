class Counter:
    # Constructor
    def __init__(self, value=0):
        # Object Attributes
        self.value = value

    # Methods
    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def getvalue(self):
        return self.value


c = Counter()  # Create an object
print(c.getvalue())
c.inc()
print(c.getvalue())

c2 = Counter(100)  # Create an object
c2.inc()
print(c2.getvalue())
