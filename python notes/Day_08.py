#String Methods Program:
s = input("Enter a string: ")

print("Capitalize:", s.capitalize())
print("Title:", s.title())
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Swapcase:", s.swapcase())
print("Startswith:", s.startswith("A"))
print("Endswith:", s.endswith("a"))
print("Strip:", s.strip())
print("Count:", s.count("a"))
print("Find:", s.find("a"))
print("Index:", s.index("a") if "a" in s else -1)
print("Replace:", s.replace("a", "A"))
print("Split:", s.split())
print("Is Alpha:", s.isalpha())
print("Is Digit:", s.isdigit())
print("Is Alnum:", s.isalnum())
print("Is Space:", s.isspace())
print("Is Lower:", s.islower())
print("Is Upper:", s.isupper())
print("Is Title:", s.istitle())
print("Is Identifier:", s.isidentifier())

words = s.split()

print("\nList:", words)

words.append("Python")
print("Append:", words)

words.insert(0, "Hello")
print("Insert:", words)

if "Python" in words:
    words.remove("Python")
print("Remove:", words)

if len(words) > 0:
    words.pop()
print("Pop:", words)

words.extend(["Java", "C"])
print("Extend:", words)

print("Count:", words.count("Java"))
print("Index:", words.index("Java"))

words.reverse()
print("Reverse:", words)

words.sort()
print("Sort:", words)

copy_list = words.copy()
print("Copy:", copy_list)

words.clear()
print("Clear:", words)


# list Methods Program:

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

print("\nList Operations")

print("Indexing:", numbers[0])
print("Negative Indexing:", numbers[-1])
print("Slicing:", numbers[1:4])
print("Concatenation:", numbers + [60, 70])
print("Repetition:", numbers * 2)
print("Membership:", 30 in numbers)
print("Not Membership:", 100 not in numbers)

print("\nList Functions")

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

print("\nList Methods")

numbers.append(60)
print("Append:", numbers)

numbers.insert(2, 25)
print("Insert:", numbers)

numbers.extend([70, 80])
print("Extend:", numbers)

numbers.remove(30)
print("Remove:", numbers)

numbers.pop()
print("Pop:", numbers)

print("Count:", numbers.count(20))
print("Index:", numbers.index(40))

numbers.sort()
print("Sort:", numbers)

numbers.reverse()
print("Reverse:", numbers)

new_list = numbers.copy()
print("Copy:", new_list)

numbers.clear()
print("Clear:", numbers)