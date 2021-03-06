class BalanceError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

    def get_amount(self):
        return self.amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Withdraw amount is {self.amount}, but available balance is {self.balance}"


class SavingsAccount:
    # class attribute / static attribute
    minbal = 5000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    def __init__(self, acno, customer, balance=0):
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance - SavingsAccount.minbal:
            self.balance -= amount
        else:
            raise BalanceError(amount, self.balance)

    def getbalance(self):
        return self.balance


a1 = SavingsAccount(1, "Jack", 10000)
a2 = SavingsAccount(2, "Steve")
a1.deposit(10000)
a1.withdraw(50000)
print(a1.getbalance())
