class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def update_odometer(self, mileage):
        self.odometer_reading = mileage    

    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it.")
    def fill_gas_tank(self):
        print(f"The car's gas tank has been filled.")

class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The battery size of is {self.battery_size} kWh")

    def range(self, battery_size = 75):
        if battery_size == 75:
            range = 260
        elif battery_size == 100:
            range = 315
        print(f"The car can go about {range} miles on a full charge.")

#Inheritance

class ElectricCar(Car):
    def __init__(self, make, model, year):
        # Initialize the parent class attributes
        super().__init__(make, year, model)
        #Attributes of child class
        #...
        #Instances as Attributes
        self.battery = Battery(100)
    
    #Overriding methods from the Parent class
    def fill_gas_tank(self):
        print("Electric cars have no gas tanks!")
    #Other child class methods
    

#Car Instance
my_new_car = Car('audi',  'a4', 2019)
#ElectricCar Instance
my_tesla = ElectricCar('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.range()


"""
## Importing multiple classes from a module
from car import Car, ElectricCar

## Importing an entire module
from car import *

## Importing a module in a module
from car import Car
from electric_car import ElectricCar as EC

## Using Aliases
from car import Car as C
"""






