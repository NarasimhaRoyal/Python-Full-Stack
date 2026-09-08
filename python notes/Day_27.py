rom abc import ABC, abstractmethod


# Abstract class
class Vehicle(ABC):

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    # Abstract method
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # Normal method
    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


# Child class
class Car(Vehicle):

    def start(self):
        print("Car starts using a key or button")

    def stop(self):
        print("Car stops using brakes")

    def drive(self):
        print("Car is driving")


# Child class
class Bike(Vehicle):

    def start(self):
        print("Bike starts using self-start or kick")

    def stop(self):
        print("Bike stops using brakes")

    def ride(self):
        print("Bike is riding")


# Creating objects
car = Car("Toyota", 1500000)
bike = Bike("Honda", 120000)

print("----- CAR -----")
car.display()
car.start()
car.drive()
car.stop()

print("\n----- BIKE -----")
bike.display()
bike.start()
bike.ride()
bike.stop()