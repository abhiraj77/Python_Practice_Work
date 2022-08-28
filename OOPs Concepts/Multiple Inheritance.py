# Unlike Java, C++ and Python support Multiple Inheritance.
# Derived class is inheriting Base1 and Base2 classes attributes.

class Base1:
    def __init__(self):
        self.str1 = "str1"
        print("Base1")

class Base2:
    def __init__(self):
        self.str2 = "str2"
        print("Base2")
        
class Derived(Base1,Base2):
    def __init__(self):
        self.str3 = "str3"
        Base1.__init__(self)
        Base2.__ini_t_(self)
        print("Derived")

    def printV(self):
        print(f"str1 = {self.str1}\nstr2 = {self.str2}\nstr3 = {self.str3}")

A = Base1()
B = Base2()
C = Derived()
C.printV()