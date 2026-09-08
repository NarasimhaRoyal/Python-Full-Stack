#elif

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

#Nested if Program — ATM

pin = int(input("Enter PIN: "))

if pin == 1234:
    print("PIN correct")

    balance = 50000
    amount = int(input("Enter amount: "))

    if amount <= balance:
        print("Withdrawal successful")
        balance = balance - amount
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

else:
    print("Wrong PIN")    

#for Loop Program — Multiplication Table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)