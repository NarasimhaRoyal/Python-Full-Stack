import math
import random
import statistics
import calendar

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("\n--- Results ---")

# Math module
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Square root of first number:", math.sqrt(numbers[0]))

# Statistics module
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))

# Random module
print("Random number from 1 to 100:", random.randint(1, 100))

# Calendar module
year = int(input("\nEnter year: "))
month = int(input("Enter month: "))

print("\nCalendar:")
print(calendar.month(year, month))