from functools import reduce

# Global variable
company = "ABC Technologies"


def employee_details(name, salaries):

    # Local variable
    employee_name = name

    # Enclosing scope
    tax_rate = 0.10

    print("\nCompany:", company)
    print("Employee:", employee_name)

    # Lambda function
    bonus = lambda salary: salary + 5000

    # map() - Add bonus to every salary
    updated_salaries = list(map(bonus, salaries))

    print("Original Salaries:", salaries)
    print("Salaries After Bonus:", updated_salaries)

    # filter() - Find salaries greater than 30000
    high_salary = list(filter(lambda salary: salary > 30000, updated_salaries))

    print("Salaries Above 30000:", high_salary)

    # reduce() - Find total salary
    total_salary = reduce(lambda a, b: a + b, updated_salaries)

    print("Total Salary:", total_salary)

    # Average salary
    average = total_salary / len(updated_salaries)

    print("Average Salary:", average)

    # Calculate tax
    tax = total_salary * tax_rate

    print("Tax:", tax)

    # Final salary
    final_salary = total_salary - tax

    print("Salary After Tax:", final_salary)


# Input
name = input("Enter employee name: ")

salaries = []

n = int(input("Enter number of salaries: "))

for i in range(n):
    salary = int(input("Enter salary: "))
    salaries.append(salary)

employee_details(name, salaries)