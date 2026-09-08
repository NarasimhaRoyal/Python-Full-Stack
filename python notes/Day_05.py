# ==========================================
# PYTHON OPERATORS - COMPLETE PROGRAM
# ==========================================

a = 20
b = 10

# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================

print("----- Arithmetic Operators -----")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# ==========================================
# 2. COMPARISON OPERATORS
# ==========================================

print("\n----- Comparison Operators -----")

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# ==========================================
# 3. ASSIGNMENT OPERATORS
# ==========================================

print("\n----- Assignment Operators -----")

x = 10
print("Initial x:", x)

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 4
print("x /= 4:", x)

x //= 2
print("x //= 2:", x)

x %= 3
print("x %= 3:", x)


# ==========================================
# 4. LOGICAL OPERATORS
# ==========================================

print("\n----- Logical Operators -----")

age = 23
has_id = True

print("age >= 18 and has_id:", age >= 18 and has_id)
print("age < 18 or has_id:", age < 18 or has_id)
print("not has_id:", not has_id)


# ==========================================
# 5. BITWISE OPERATORS
# ==========================================

print("\n----- Bitwise Operators -----")

p = 5
q = 3

print("p & q:", p & q)
print("p | q:", p | q)
print("p ^ q:", p ^ q)
print("~p:", ~p)
print("p << 1:", p << 1)
print("p >> 1:", p >> 1)


# ==========================================
# 6. MEMBERSHIP OPERATORS
# ==========================================

print("\n----- Membership Operators -----")

fruits = ["Apple", "Banana", "Mango"]

print("'Apple' in fruits:", "Apple" in fruits)
print("'Orange' in fruits:", "Orange" in fruits)
print("'Orange' not in fruits:", "Orange" not in fruits)


# ==========================================
# 7. IDENTITY OPERATORS
# ==========================================

print("\n----- Identity Operators -----")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 == list3:", list1 == list3)


# ==========================================
# 8. CONDITIONAL / TERNARY OPERATOR
# ==========================================

print("\n----- Conditional Operator -----")

marks = 75

result = "Pass" if marks >= 40 else "Fail"

print("Marks:", marks)
print("Result:", result)