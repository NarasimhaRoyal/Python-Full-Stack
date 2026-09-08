class Student:

    college = "ABC College"       

    def __init__(self, name, marks):
        self.name = name           
        self.marks = marks         
    def display(self):
        message = "Student Details"    
        print(message)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("College:", Student.college)


s1 = Student("Rafi", 85)
s2 = Student("Navya", 74)

s1.display()

print()

s2.display()