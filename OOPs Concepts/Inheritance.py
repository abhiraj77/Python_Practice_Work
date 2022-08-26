# Here Person(the base class) is inherited by Employee(the derived class) which goes ahead and uses the variables and functions of Person class.

class Person:

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def details(self):
        print(self.name)
        print(self.ID)

    def display(self):
        print(f"My name is {self.name}")
        print(f"ID: {self.ID}")

class Employee(Person):

    def __init__(self, name, ID, salary, position):
        self.salary = salary
        self.position = position

        Person.__init__(self, name, ID)

    def display(self):
        print(f"Position: {self.position}")

# David = Person("David", 123)
David = Employee("David", 123, 9000, "Developer")
David.details()
David.display()