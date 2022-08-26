# In Encapsulation we try to wrap up classes, methods and variables into one unit so that the user doesn't accidentaly change a variable value or code.
# In Python, encapsulation is present but is just customary rather than hard coded.
# In Python, we can call and edit protected and private variables outside the class but it is an understanding between programs to not do it.

class Base:
    __password = None # Private Variable
    _statement = None # Protected Variable

    def __init__(self):
        self.__password = "Pass"
        self._statement = "This is a protected Statement" # Protected variable can be called like normal variables.

    def setPassword(self, newPass):
        __password = newPass
        print(f"New Password = {__password}")

class Derived(Base):
    def __init__(self, A):
        self.A = A
        Base.__init__(self)

    def getPassword(self):
        print(f"calling __Password in a subclass = {self._Base__password}") # This is the way to access private variables but by custom should not be done.
        pass

obj1 = Base()
obj2 = Derived("Sub")

obj2.getPassword()
print(f"calling __Password outside class = {obj2._Base__password}")

print(f"calling _statement outside class = {obj2._statement}")

obj1.setPassword("ABCD")

# The below statement if run will give an Attribute Error as it is defined as 
# print(f"calling __Password directly = {obj2.__password}") 