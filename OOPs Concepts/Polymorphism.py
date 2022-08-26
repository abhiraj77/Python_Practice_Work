# The Eagle and Ostrich class change the function flight which is derived from the Bird Class.

class Bird:
    def intro(self):
        print("I am a Bird.")

    def flight(self):
        print("There are many birds that can fly and many that can not.")

class Eagle(Bird):
    def flight(self):
        print(f"I am {Eagle.__name__}. I can Fly!")

class Ostrich(Bird):
    def flight(self):
        print(f"I am {Ostrich.__name__}. I can not fly. :(")

obj_Bird = Bird()
obj_Eagle = Eagle()
obj_Ostrich = Ostrich()

obj_Bird.intro()
obj_Bird.flight()

obj_Eagle.intro()
obj_Eagle.flight()

obj_Ostrich.intro()
obj_Ostrich.flight()