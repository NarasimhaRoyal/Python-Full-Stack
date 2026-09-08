class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog: Bark")


class Cat(Animal):

    def sound(self):
        print("Cat: Meow")


class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


# Method Overriding
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# Method Overloading style
c = Calculator()

print(c.add(10))
print(c.add(10, 20))
print(c.add(10, 20, 30))


# Operator Polymorphism
print(10 + 20)
print("Hello " + "Python")