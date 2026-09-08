student = {
    "name": "Narasimha",
    "age": 21,
    "course": "Python",
    "marks": 88
}

print("Original Dictionary:", student)

print("\nDictionary Operations")

print("Access:", student["name"])
print("Membership:", "name" in student)
print("Not Membership:", "city" not in student)

student["city"] = "Hyderabad"
print("After Adding:", student)

student["marks"] = 90
print("After Updating:", student)

print("\nDictionary Functions")

print("Length:", len(student))
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

print("\nDictionary Methods")

print("Get Name:", student.get("name"))
print("Get City:", student.get("city"))

student.setdefault("phone", "9999999999")
print("Setdefault:", student)

student.update({"marks": 95, "college": "ABC College"})
print("Update:", student)

copy_student = student.copy()
print("Copy:", copy_student)

student.pop("phone")
print("Pop:", student)

student.popitem()
print("Popitem:", student)

# if and if-else Statement Program:

name = input("Enter student name: ")
age = int(input("Enter age: "))

maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))