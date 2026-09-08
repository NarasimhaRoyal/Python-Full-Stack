class BankAccount:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.__balance = balance       # Private variable

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Amount withdrawn:", amount)

    # Check balance
    def get_balance(self):
        return self.__balance

    # Display account details
    def display(self):
        print("\n----- Account Details -----")
        print("Account Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.__balance)


# Creating object
account = BankAccount("ACC101", "Rafi", 10000)

account.display()

# Deposit
account.deposit(5000)

# Withdraw
account.withdraw(3000)

# Display updated balance
print("\nCurrent Balance:", account.get_balance())

# Trying to access private variable directly
# print(account.__balance)   # Error