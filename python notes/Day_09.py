#Tuple Program

numbers = (10, 20, 30, 40, 50)

print("Original Tuple:", numbers)

print("\nTuple Operations")

print("Indexing:", numbers[0])
print("Negative Indexing:", numbers[-1])
print("Slicing:", numbers[1:4])
print("Concatenation:", numbers + (60, 70))
print("Repetition:", numbers * 2)
print("Membership:", 30 in numbers)
print("Not Membership:", 100 not in numbers)

print("\nTuple Functions")

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

print("\nTuple Methods")

print("Count:", numbers.count(20))
print("Index:", numbers.index(40))

#Set Program

numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)

print("\nSet Operations")

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

print("Membership:", 20 in numbers)
print("Not Membership:", 100 not in numbers)

print("\nSet Functions")

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

print("\nSet Methods")

numbers.add(60)
print("Add:", numbers)

numbers.update([70, 80])
print("Update:", numbers)

numbers.remove(30)
print("Remove:", numbers)

numbers.discard(100)
print("Discard:", numbers)

numbers.pop()
print("Pop:", numbers)

copy_set = numbers.copy()
print("Copy:", copy_set)

print("Is subset:", {10, 20}.issubset(numbers))
print("Is superset:", numbers.issuperset({10, 20}))

numbers.clear()
print("Clear:", numbers)