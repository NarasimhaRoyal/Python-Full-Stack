# ATM PROJECT

accounts = {
    "1001": {
        "name": "Narasimha",
        "pin": "143",
        "balance": 10000
    },
    "1002": {
        "name": "simha",
        "pin": "5678",
        "balance": 15000
    }
}


def login():
    print("\n===== ATM LOGIN =====")

    account_number = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome", accounts[account_number]["name"])
            return account_number
        else:
            print("Incorrect PIN!")
    else:
        print("Account not found!")

    return None


def check_balance(account_number):
    balance = accounts[account_number]["balance"]

    print("\nCurrent Balance: ₹", balance)


def deposit(account_number):
    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        accounts[account_number]["balance"] += amount
        print("Amount deposited successfully!")
        print("New Balance: ₹", accounts[account_number]["balance"])
    else:
        print("Invalid amount!")


def withdraw(account_number):
    amount = float(input("Enter withdrawal amount: ₹"))

    balance = accounts[account_number]["balance"]

    if amount <= 0:
        print("Invalid amount!")

    elif amount > balance:
        print("Insufficient balance!")

    else:
        accounts[account_number]["balance"] -= amount
        print("Please collect your cash.")
        print("Remaining Balance: ₹",
              accounts[account_number]["balance"])


def change_pin(account_number):
    old_pin = input("Enter old PIN: ")

    if old_pin == accounts[account_number]["pin"]:

        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")

        if new_pin == confirm_pin and len(new_pin) == 4:
            accounts[account_number]["pin"] = new_pin
            print("PIN changed successfully!")
        else:
            print("PINs do not match or PIN is not 4 digits.")

    else:
        print("Incorrect old PIN!")


def atm_menu(account_number):

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit(account_number)

        elif choice == "3":
            withdraw(account_number)

        elif choice == "4":
            change_pin(account_number)

        elif choice == "5":
            print("\nThank you for using the ATM!")
            break

        else:
            print("Invalid choice!")


# Main Program

print("*****************************")
print("       WELCOME TO ATM")
print("*****************************")

account = login()

if account is not None:
    atm_menu(account)
else:
    print("\nLogin failed.")