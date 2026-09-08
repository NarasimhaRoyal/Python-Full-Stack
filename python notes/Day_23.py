class Student:

    college = "fjufdhfu College"       # Class variable

    # Constructor
    def __init__(self, name, marks):
        self.name = name          # Instance variable
        self.marks = marks

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Class Method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static Method
    @staticmethod
    def check_pass(marks):
        if marks >= 40:
            return "PASS"
        else:
            return "FAIL"


# Creating objects
s1 = Student("Narasimha", 85)
s2 = Student("simha", 35)

# Instance methods
s1.display()
print("Result:", Student.check_pass(s1.marks))

print()

s2.display()
print("Result:", Student.check_pass(s2.marks))

print()

# Class method
Student.show_college()