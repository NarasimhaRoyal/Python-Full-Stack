students = []


def add_student():
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))

    marks = []

    for i in range(3):
        mark = float(input("Enter mark for subject " + str(i + 1) + ": "))
        marks.append(mark)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def calculate_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


def calculate_percentage(marks):
    total = calculate_total(marks)
    percentage = total / len(marks)

    return percentage


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def display_student(student):

    total = calculate_total(student["marks"])
    percentage = calculate_percentage(student["marks"])
    grade = calculate_grade(percentage)

    print("\n-------------------------")
    print("Name       :", student["name"])
    print("Roll Number:", student["roll"])
    print("Marks      :", student["marks"])
    print("Total      :", total)
    print("Percentage :", percentage)
    print("Grade      :", grade)
    print("-------------------------")


def search_student():
    roll = int(input("Enter roll number to search: "))

    for student in students:
        if student["roll"] == roll:
            display_student(student)
            return

    print("Student not found!")


def display_all():

    if len(students) == 0:
        print("No students available.")
    else:
        for student in students:
            display_student(student)


def highest_student():

    if len(students) == 0:
        print("No students available.")
        return

    highest = students[0]

    for student in students:
        if calculate_percentage(student["marks"]) > calculate_percentage(highest["marks"]):
            highest = student

    print("\nHighest Scoring Student:")
    display_student(highest)


while True:

    print("\n========== STUDENT MANAGEMENT ==========")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Find Highest Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        search_student()

    elif choice == 3:
        display_all()

    elif choice == 4:
        highest_student()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid choice!")