# Printing Objects using __str__ and __repr__.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # if there is no repr or str method then instance address gets returned.

    # if __str__ doesn't exist then __repr__ method will be called.
    def __repr__(self):
        return f"Repr called\nMy name is {self.name}.\nI am {self.age} years old."

    # if this keyword function is made, then it will be called when print function is used for this class.
    def __str__(self):
        return f"Str called\nMy name is {self.name}.\nI am {self.age} years old."

Abhiraj = Person("Abhiraj",22)
print(Abhiraj)