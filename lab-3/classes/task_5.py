class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        print("Your balance:", self.balance)
    def withdraw(self, money):
        if self.balance < abs(money):
            print("You cannot overdrawn your balance")
        else:
            self.balance -= abs(money)

person1 = Account("Dima", 200)
person1.deposit(100)
person1.withdraw(301)