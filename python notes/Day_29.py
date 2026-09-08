balance = 10000

try:

    pin = int(input("Enter PIN: "))

    if pin != 1234:
        raise ValueError("Incorrect PIN")

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise ValueError("Insufficient balance")

    balance -= amount

    print("Withdrawal successful")
    print("Remaining balance:", balance)

except ValueError as e:
    print("Transaction failed:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Thank you for using ATM")