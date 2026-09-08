#While Loop
for i in range(1, 11):
    if i == 6:
        break
    print(i)

 #Jumping Statement:
 #break
for i in range(1, 11):
    if i == 6:
        break
    print(i)
#continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
#pass
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
#for else
numbers = [10, 20, 30, 40, 50]

search = int(input("Enter number: "))

for i in numbers:
    if i == search:
        print("Number found")
        break
else:
    print("Number not found")
#While-Else
i = 1
search = int(input("Enter number: "))

while i <= 10:
    if i == search:
        print("Number found")
        break
    i = i + 1
else:
    print("Number not found")
#Assert
age = int(input("Enter age: "))

assert age >= 18, "Age must be 18 or above"

print("Eligible for voting")
# Nested For Loop
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()        
   