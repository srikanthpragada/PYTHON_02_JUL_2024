class Course:
    # Static attributes or class attributes
    taxrate = 18

    def __init__(self, title, fee):
        # Object attributes
        self.title = title
        self.fee = fee

    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate / 100

    @staticmethod     # Decorator
    def gettaxrate():
        return Course.taxrate

    def setfee(self, newfee):
        self.fee = newfee

    def show(self):
        print(f"Title   : {self.title}")
        print(f"Fee     : {self.fee}")


c = Course("Data Science", 10000)
print(Course.gettaxrate())

# c.fee = 15000
c.setfee(15000)
c.show()
print(c.getnetfee())

courses = [
    Course("Java", 10000),
    Course("Power BI", 12000),
    Course("AWS", 5000)
]

for c in courses:
    c.show()
