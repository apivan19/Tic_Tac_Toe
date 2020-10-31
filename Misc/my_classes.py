# Written in Python 3.7 (I only update when necessary or an extraordinary features comes out)

# Classes: The blueprints for how an instance / object should look and behave
# Each class has methods that unique to objects of that class - type("Hello")
#       Methods are functions that are unique to a certain class
class Vehicle:

    # Class Variable Namespace has information that is common to ALL objects of the class
    has_engine = True

    # Instance Variable Namespace - Attributes that can be unique to each instance
    # These attributes are uniquely set at the time of creation of the instance/object
    # The Initialization Method - Known as a constructor in most other languages
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    # Method is a function that is available to all instances of the class
    def getSpeed(self):
        return


# Parent Class goes in the parenthases!
# Child Class will run the Parent class's init function / methods, unless the child class overwrites them
class Land_Vehicle(Vehicle):
    def __init__(self):
        super().__init__()
        print("This Vehicle Will ride on the land")


class Water_Vehicle(Vehicle):
    pass


class SpeedBoat(Water_Vehicle):
    pass


# Classes can inherit from multiple parent classes - If both parent classes have the same method name, only the first parent class's method gets inherited
class Duck_Boat(Land_Vehicle, Water_Vehicle):
    pass


class Air_Vehicle(Vehicle):
    pass


# An outer class
class Student:
    def __init__(self, first_name, middle_name, last_name, age):
        self.first = first_name
        self.middle = middle_name
        self.last = last_name
        self.full = first_name + " " + middle_name + " " + last_name
        self.age = age
        self.laptop = self.Laptop("Dell", "i5", "Ryzen", 16)

    def say_full_name(self):
        print(f"HI! My name is {self.full}!")

    # An inner class / nested class
    class Laptop:
        def __init__(self, brand, CPU, GPU, RAM):
            self.brand = brand
            self.CPU = CPU
            self.GPU = GPU
            self.RAM = f"{RAM} GB"

        def process(self):
            print("Your data is processing")


# ----------------------------------------------------------------------------------------------------------
class Universe:

    universal_poem = "Infinite, Unknown, Unknowable"

    def __init__(self, age_billions, num_known_galaxies):
        self.age = age_billions
        self.num_known_galaxies = num_known_galaxies

    def get_age(self):
        print(f"The Universe is {self.age} Billion Years Old")

    # Can I avoid using @classmethods using this way?
    def recite_poem(self):
        print(Universe.universal_poem)

    class Galaxy:
        def __init__(self, num_solar_systems):
            self.num_solar_systems = num_solar_systems

            class SolarSystem:
                def __init__(self, name, planets):
                    self.name = name
                    self.planets = planets

                class Planet:
                    shape = "Spherical"

                    def __init__(
                        self,
                        name,
                        radius,
                        gravity,
                        life_present,
                        year_length,
                        day_length,
                        spin_velocity,
                    ):
                        self.name = name
                        self.radius = radius
                        self.gravity = gravity
                        self.life_present = life_present
                        self.year_length = year_length
                        self.day_length = day_length
                        self.spin_velocity = spin_velocity
                        self.solar_system = SolarSystem.name

                    def orbit(self):
                        return (
                            f"{self.name} is orbiting in the {self.solar_system} System"
                        )

                    class Satellite:
                        pass

                class Star:
                    pass


# ---------------------------------------------------------------------------------------------------
class Employee:

    # class variables common to all instances / employees
    raise_amount = 1.04
    number_of_employees = 0  # Universal counter of all existing employees

    # Instance Variables unique to each employee
    # Init function runs on creation of a new instance / employee
    def __init__(self, first, middle, last, age, ID, position, salary):
        self.first = first
        self.middle = middle
        self.last = last
        self.age = age
        self.ID = ID
        self.position = position
        self.salary = salary
        Employee.number_of_employees += 1

    # Methods
    def apply_raise(self):
        self.salary *= Employee.raise_amount

    # define this method as a property
    # This will be updated if any of the properties are changed... having it in init will not change because that only runs at instantiation.
    @property
    def fullname(self):
        return {self.first + " " + self.middle + " " + self.last}

    # Allows you to change multiple values and update them in the instance
    @fullname.setter
    def fullname(self, name):
        first, middle, last = name.split(" ")
        self.first = first
        self.middle = middle
        self.last = last

    # Deleter Method
    @fullname.deleter
    def fullname(self):
        print("Deleting Name")
        self.first = None
        self.middle = None
        self.last = None


emp1 = Employee("Alex", "Paul", "Ivan", 22, 234234234, "Researcher", 90000)
print(emp1.full)
emp1.first = "Christ"
print(emp1.first)
