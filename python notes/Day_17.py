def total_marks(marks, n):
    if n == 0:
        return 0
    return marks[n - 1] + total_marks(marks, n - 1)


def highest_marks(marks, n):
    if n == 1:
        return marks[0]

    previous = highest_marks(marks, n - 1)

    if marks[n - 1] > previous:
        return marks[n - 1]
    else:
        return previous


def count_pass(marks, n):
    if n == 0:
        return 0

    if marks[n - 1] >= 35:
        return 1 + count_pass(marks, n - 1)
    else:
        return count_pass(marks, n - 1)


def display_marks(marks, n):
    if n == 0:
        return

    display_marks(marks, n - 1)
    print("Subject", n, ":", marks[n - 1])


# Main program
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)

print("\n--- Student Result ---")

display_marks(marks, n)

total = total_marks(marks, n)
average = total / n
highest = highest_marks(marks, n)
passed = count_pass(marks, n)

print("\nTotal Marks:", total)
print("Average:", average)
print("Highest Mark:", highest)
print("Subjects Passed:", passed)

if passed == n:
    print("Result: PASS")
else:
    print("Result: FAIL")