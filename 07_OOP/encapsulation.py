# Encapsulation

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Namratha", 5000)

account.deposit(1000)
account.withdraw(2000)

print("Balance:", account.get_balance())