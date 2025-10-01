class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Поповнення рахунку"""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Зняття коштів з рахунку"""
        if amount > self.balance:
            print("Сума завелика!")
        else:
            self.balance -= amount
        return self.balance


user1 = BankAccount(1, 1500)
user2 = BankAccount(2, 1000)

print(user1.deposit(900))
print(user1.withdraw(1900))

print(user2.withdraw(257))
print(user2.deposit(3783))
