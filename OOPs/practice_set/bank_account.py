# Create a BankAccount class with:
# Object attributes: account_holder, balance
# Methods:
# deposit(amount)
# withdraw(amount)
# show_balance()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        return self.balance


account = BankAccount("Md Ashfak Alam", 4500)
bal = account.show_balance()
print(f"Total balance in your account: {bal}")

withdraw_money = int(input("Enter money you want to withdraw: "))
account.withdraw(withdraw_money)
print(f"After withdrawing your total balance is: {account.show_balance()}")

deposit_money = int(input("Enter money you want to deposit: "))
account.deposit(deposit_money)
print(f"After depositing your total balance is: {account.show_balance()}")
