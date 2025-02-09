# Base class: BankAccount
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.account_holder} Deposited: ${amount}, New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} Withdrew: ${amount}, New Balance: ${self.balance}")
        else:
            print(f"{self.account_holder} - Insufficient funds or invalid amount.")

    def get_balance(self):
        return f"{self.account_holder}'s Balance: ${self.balance}"

# Derived class: SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.account_holder} - Interest Applied: ${interest}, New Balance: ${self.balance}")

# Derived class: CheckingAccount (inherits from BankAccount)
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=50):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.account_holder} Withdrew: ${amount}, New Balance: ${self.balance}")
        else:
            print(f"{self.account_holder} - Overdraft limit exceeded.")

# Polymorphism demonstration
def transaction(account, amount, transaction_type="deposit"):
    if transaction_type == "deposit":
        account.deposit(amount)
    elif transaction_type == "withdraw":
        account.withdraw(amount)

# Creating multiple instances
acc1 = SavingsAccount("Alice", 500)
acc2 = CheckingAccount("Bob", 200)
acc3 = BankAccount("Charlie", 1000)

# Performing transactions
transaction(acc1, 200, "deposit")
transaction(acc1, 100, "withdraw")
acc1.apply_interest()  # Interest applied for savings account

transaction(acc2, 300, "withdraw")  # Overdraft limit allows withdrawal
transaction(acc3, 150, "withdraw")

# Checking balances
print(acc1.get_balance())
print(acc2.get_balance())
print(acc3.get_balance())
