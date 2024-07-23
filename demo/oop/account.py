class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount  = amount

    def __str__(self):
        return f"Insufficient balance {self.balance} for withdraw of {self.amount} amount"

class SavingsAccount:
    # static attribute
    minbal = 10000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - SavingsAccount.minbal >= amount:
            self.__balance -= amount
        else:
            #raise ValueError("Insufficient Balance!")
            raise InsufficientBalanceError(self.__balance - SavingsAccount.minbal, amount)

    @property
    def balance(self):
        return self.__balance


print(SavingsAccount.getminbal())

a1 = SavingsAccount(1, "Richards", 10000)
a1.deposit(5000)
a1.withdraw(10000)

print(a1.__dict__)

#print(a1.__balance)
print(a1._SavingsAccount__balance)
print(a1.balance)




