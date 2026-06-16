"""Overiding"""

class Base:
    def __init__(self):
        print("Inside Base Constructor")

    def show(self):
        print("Inside Base Show")

    def __del__(self):
        print("Inside Base Destructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived Constructor")

    def show(self):
        super().show()
        print("Inside Dreived Show")

    def __del__(self):
        print("Inside Derivred Destructor")
        return super().__del__()

bobj = Derived() 
Base.show(bobj)
