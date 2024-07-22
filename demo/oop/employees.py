from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, mobile, email):
        self.name = name
        self.mobile = mobile
        self.email = email

    @abstractmethod
    def getsalary(self):
        pass


class SalariedEmployee(Employee):
    def __init__(self, name, mobile, email, salary, comm_rate, total_sales):
        super().__init__(name, mobile, email)
        self.salary = salary
        self.comm_rate = comm_rate
        self.total_sales = total_sales

    def getsalary(self):
        return self.salary + self.total_sales * self.comm_rate / 100


class CommissionEmployee(Employee):
    def __init__(self, name, mobile, email, units_sold, comm_per_unit):
        super().__init__(name, mobile, email)
        self.unit_sold = units_sold
        self.comm_per_unit = comm_per_unit

    def getsalary(self):
        return self.unit_sold * self.comm_per_unit


se = SalariedEmployee("Eric", "39393933", "eric@sales.com", 20000, 2, 200000)
print(se.getsalary())

ce = CommissionEmployee("Jason", "22323333", "jason@sales.com", 8, 2000)
print(ce.getsalary())
