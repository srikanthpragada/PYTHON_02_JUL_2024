class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def getbalance(self):
        return self.__balance


a1 = SavingsAccount(1, "Richards", 10000)
a1.deposit(5000)
a1.withdraw(10000)

print(a1.__dict__)

#print(a1.__balance)
print(a1._SavingsAccount__balance)
print(a1.getbalance())




