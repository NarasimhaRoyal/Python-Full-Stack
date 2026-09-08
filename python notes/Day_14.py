n = 5

# 1. Hollow Square
print("\n1. HOLLOW SQUARE")

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 2. Hollow Rectangle
print("\n2. HOLLOW RECTANGLE")

rows = 4
cols = 7

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 3. Hollow Right Triangle
print("\n3. HOLLOW RIGHT TRIANGLE")

for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 4. Hollow Inverted Right Triangle
print("\n4. HOLLOW INVERTED RIGHT TRIANGLE")

for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 5. Hollow Pyramid
print("\n5. HOLLOW PYRAMID")

for i in range(1, n+1):

    for j in range(n-i):
        print(" ", end=" ")

    for j in range(2*i-1):
        if j == 0 or j == 2*i-2 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 6. Hollow Inverted Pyramid
print("\n6. HOLLOW INVERTED PYRAMID")

for i in range(n, 0, -1):

    for j in range(n-i):
        print(" ", end=" ")

    for j in range(2*i-1):
        if j == 0 or j == 2*i-2 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 7. Hollow Diamond
print("\n7. HOLLOW DIAMOND")

for i in range(1, n+1):

    for j in range(n-i):
        print(" ", end=" ")

    for j in range(2*i-1):
        if j == 0 or j == 2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(n-1, 0, -1):

    for j in range(n-i):
        print(" ", end=" ")

    for j in range(2*i-1):
        if j == 0 or j == 2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 8. Hollow Hourglass
print("\n8. HOLLOW HOURGLASS")

for i in range(n, 0, -1):

    for j in range(n-i):
        print(" ", end=" ")

    for j in range(2*i-1):
        if j == 0 or j == 2*i-2 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(2, n+1):

    for j in range(n-i):
        print(" ", end=" ")

    for j in range(2*i-1):
        if j == 0 or j == 2*i-2 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 9. Hollow X
print("\n9. HOLLOW X")

for i in range(n):
    for j in range(n):
        if j == i or j == n-i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 10. Hollow Plus
print("\n10. HOLLOW PLUS")

mid = n // 2

for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()