# Creating and using a custom exception

class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance for this withdrawal."
            )

        self.balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance:", self.balance)


account = BankAccount(5000)

try:
    amount = float(input("Enter withdrawal amount: "))
    account.withdraw(amount)

except InsufficientBalanceError as error:
    print("Error:", error)

except ValueError:
    print("Please enter a valid amount.")