# ALL TYPES OF INHERITANCE


# 1. Single Inheritance
class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


print("----- SINGLE INHERITANCE -----")
dog = Dog()
dog.eat()
dog.bark()


# 2. Multiple Inheritance
class Father:
    def car(self):
        print("Father has a car")


class Mother:
    def house(self):
        print("Mother has a house")


class Child(Father, Mother):
    def bike(self):
        print("Child has a bike")


print("\n----- MULTIPLE INHERITANCE -----")
child = Child()
child.car()
child.house()
child.bike()


# 3. Multilevel Inheritance
class Grandparent:
    def land(self):
        print("Grandparent has land")


class Parent(Grandparent):
    def home(self):
        print("Parent has a home")


class Son(Parent):
    def study(self):
        print("Son is studying")


print("\n----- MULTILEVEL INHERITANCE -----")
son = Son()
son.land()
son.home()
son.study()


# 4. Hierarchical Inheritance
class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


print("\n----- HIERARCHICAL INHERITANCE -----")

car = Car()
car.start()
car.drive()

bike = Bike()
bike.start()
bike.ride()


# 5. Hybrid Inheritance
class Person:
    def walk(self):
        print("Person can walk")


class Student(Person):
    def study(self):
        print("Student is studying")


class Employee(Person):
    def work(self):
        print("Employee is working")


class WorkingStudent(Student, Employee):
    def earn(self):
        print("Working student earns money")


print("\n----- HYBRID INHERITANCE -----")

ws = WorkingStudent()

ws.walk()
ws.study()
ws.work()
ws.earn()