class Dog:
    
    #class attribute
    attr1 = "Mammal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")

Tom = Dog("Tommy")
Rod = Dog("Rodger")

# accessing Public variables
print(f"Accesing public variable of the class {Tom.attr1}")

# accessing Instance Variables
print(f"Calling attribute name {Tom.name}")

Tom.speak()