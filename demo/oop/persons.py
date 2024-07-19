from abc import ABC, abstractmethod


# Abstract class
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name)
        print(self.email)

    def setemail(self, email):
        self.email = email

    # Abstract method
    @abstractmethod
    def getoccupation(self):
        pass


class Student(Person):
    def __init__(self, name, email, course, college):
        # pass values to super class's constructor
        super().__init__(name, email)
        self.course = course
        self.college = college

    def show(self):
        super().show()
        print(self.course)
        print(self.college)

    def setcourse(self, course):
        self.course = course

    def setcollege(self, college):
        self.college = college

    def getoccupation(self):
        return f"Studying {self.course} at {self.college}"


class Employee(Person):
    def __init__(self, name, email, job, company):
        # pass values to super class's constructor
        super().__init__(name, email)
        self.job = job
        self.company = company

    def show(self):
        super().show()
        print(self.job)
        print(self.company)

    def setcourse(self, job):
        self.job = job

    def setcollege(self, company):
        self.company = company

    def getoccupation(self):
        return f"Working as {self.job} at {self.company}"


s = Student("Mark", "mark@gmail.com", "MS CS", "Stanford")
s.setemail("mark@facebook.com")
s.show()
print(s.getoccupation())

e = Employee("Jason", "jason@gmail.com", "Programmer", "Google")
e.show()
