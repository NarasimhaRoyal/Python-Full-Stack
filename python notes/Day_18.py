# Student Marks Program
# List Comprehension + Generator


students = {
    "Ravi": [78, 85, 92],
    "Rahul": [65, 72, 80],
    "Anil": [35, 42, 38],
    "Sita": [90, 95, 88],
    "Priya": [25, 30, 28]
}


# List Comprehension
averages = {
    name: sum(marks) / len(marks)
    for name, marks in students.items()
}

print("Student Averages:")
for name, average in averages.items():
    print(name, ":", average)


# List Comprehension to find passed students
passed_students = [
    name for name, average in averages.items()
    if average >= 40
]

print("\nPassed Students:")
print(passed_students)


# List Comprehension to find failed students
failed_students = [
    name for name, average in averages.items()
    if average < 40
]

print("\nFailed Students:")
print(failed_students)


# Generator
def result_generator(students):
    for name, marks in students.items():

        total = sum(marks)
        average = total / len(marks)

        if average >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        yield name, total, average, result


# Using Generator
print("\nStudent Results:")

for name, total, average, result in result_generator(students):
    print(name)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)