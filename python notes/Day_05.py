# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
marks = float(input("Enter your marks: "))

# Output Formatting
print("\n---------- STUDENT DETAILS ----------")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Course : {course}")
print(f"Marks  : {marks:.2f}")
print("-------------------------------------")
