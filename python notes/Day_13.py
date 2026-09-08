### 1. Even or Odd

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
### 2. Positive, Negative or Zero
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
### 3. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest:", a)
elif b > a and b > c:
    print("Largest:", b)
else:
    print("Largest:", c)
### 4. Multiplication Table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)
### 5. Sum of N Numbers
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum:", sum)
### 6. Factorial
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)
### 7. Reverse a Number
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reverse:", reverse)
### 8. Sum of Digits
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum:", sum)
### 9. Count Digits
n = int(input("Enter a number: "))

count = 0

while n > 0:
    count = count + 1
    n = n // 10

print("Digits:", count)
### 10. Palindrome Number
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
### 11. Prime Number
n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")
### 12. Factors of a Number
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
### 13. Perfect Number
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")

### 14. Armstrong Number
n = int(input("Enter a number: "))

original = n
digits = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")
### 15. Fibonacci Series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
### 16. Reverse a String
s = input("Enter a string: ")
reverse = s[::-1]
print("Reverse:", reverse)
### 17. Palindrome String
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

### 18. Count Vowels
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Vowels:", count)

### 19. Find Largest in a List
numbers = [10, 25, 5, 40, 15]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest:", largest)

### 20. Remove Duplicates from List
numbers = [1, 2, 2, 3, 4, 4, 5]

result = []

for n in numbers:
    if n not in result:
        result.append(n)

print(result)