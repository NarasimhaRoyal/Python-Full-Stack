from abc import ABC, abstractmethod


# ==============================
# ABSTRACT CLASS
# ==============================

class BankAccount(ABC):

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.__balance = balance       # Encapsulation

    # Getter
    def get_balance(self):
        return self.__balance

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    # Withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Please collect your cash")

    # Abstract method
    @abstractmethod
    def account_type(self):
        pass

    # Display account information
    def display(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Name       :", self.name)
        print("Account No :", self.account_no)
        print("Account Type:", self.account_type())
        print("Balance    :", self.__balance)


# ==============================
# SAVINGS ACCOUNT
# ==============================

class SavingsAccount(BankAccount):

    def account_type(self):
        return "Savings Account"

    def withdraw(self, amount):
        if amount > self.get_balance():
            print("Savings Account: Insufficient balance")
        else:
            super().withdraw(amount)


# ==============================
# CURRENT ACCOUNT
# ==============================

class CurrentAccount(BankAccount):

    def account_type(self):
        return "Current Account"

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            super().withdraw(amount)


# ==============================
# ATM CLASS
# ==============================

class ATM:

    def __init__(self, account, pin):
        self.account = account
        self.__pin = pin

    def verify_pin(self):
        entered_pin = int(input("Enter PIN: "))

        if entered_pin == self.__pin:
            return True
        else:
            print("Incorrect PIN")
            return False

    def menu(self):

        while True:

            print("\n========== ATM MENU ==========")
            print("1. Account Details")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.account.display()

            elif choice == 2:
                print("Current Balance:",
                      self.account.get_balance())

            elif choice == 3:
                amount = float(input("Enter deposit amount: "))
                self.account.deposit(amount)

            elif choice == 4:
                amount = float(input("Enter withdrawal amount: "))
                self.account.withdraw(amount)

            elif choice == 5:
                print("Thank you for using ATM")
                break

            else:
                print("Invalid choice")


# ==============================
# OBJECT CREATION
# ==============================

account = SavingsAccount(
    "Rafi",
    "ACC1001",
    10000
)

atm = ATM(account, 1234)


# ==============================
# ATM START
# ==============================

print("================================")
print("       WELCOME TO ATM")
print("================================")

if atm.verify_pin():
    atm.menu()