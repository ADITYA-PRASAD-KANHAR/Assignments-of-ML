# 19.  Implement a bank account system with deposit and withdrawal methods. 
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Example
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.balance)
