name = input("Enter name: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

numbers = [a, b]

print("Name:", name)
print("Length:", len(name))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Absolute:", abs(-a))
print("Power:", pow(a, 2))
print("Type:", type(a))
print("Sorted:", sorted(numbers))