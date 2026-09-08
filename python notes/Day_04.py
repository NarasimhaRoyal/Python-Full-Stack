# ==========================================
# SET
# ==========================================

numbers = {10, 20, 30, 20, 10}

print("Set:", numbers)

numbers.add(40)
numbers.remove(20)

print("After adding and removing:", numbers)


# ==========================================
# DICTIONARY
# ==========================================

student = {
    "name": "Narasimha",
    "age": 21,
    "course": "CSE"
}

print("\nDictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["city"] = "Hyderabad"

# Updating a value
student["age"] = 24

print("Updated Dictionary:", student)


# ==========================================
# BOOLEAN
# ==========================================

a = 10
b = 20

print("\nBoolean Examples:")
print(a > b)
print(a < b)
print(a == b)

is_student = True
is_employee = False

print("Is Student:", is_student)
print("Is Employee:", is_employee)


# ==========================================
# NONE
# ==========================================

result = None

print("\nNone Example:")
print("Result:", result)
print("Type of result:", type(result))

if result is None:
    print("No value is available")


# ==========================================
# TYPE()
# ==========================================

x = 100
y = 10.5
name = "Narasimha"
marks = [80, 83, 90]

print("\nType Examples:")
print(type(x))
print(type(y))
print(type(name))
print(type(marks))


# ==========================================
# IMPLICIT TYPE CONVERSION
# ==========================================

integer_number = 10
float_number = 5.5

result = integer_number + float_number

print("\nImplicit Conversion:")
print("Result:", result)
print("Type:", type(result))


# ==========================================
# EXPLICIT TYPE CONVERSION
# ==========================================

# String to Integer
age = "23"
age = int(age)

print("\nString to Integer:")
print(age)
print(type(age))


# Integer to Float
number = 10
number = float(number)

print("\nInteger to Float:")
print(number)
print(type(number))


# Integer to String
number = 100
text = str(number)

print("\nInteger to String:")
print(text)
print(type(text))


# List to Set
numbers_list = [10, 20, 20, 30, 30]
numbers_set = set(numbers_list)

print("\nList to Set:")
print(numbers_set)
print(type(numbers_set))