class Parent :
    def __init__(self,Name):
        self.Name = Name
        print(f"Call for Constructor Parent \nHello {Name}")

    def __del__(self):
        print("Inside Parent Class Destructor")
        del self.Name


class Child(Parent):
    def __init__(self, Name):
        super().__init__(Name)
        print("Inside Child Constuctor")

    def __del__(self):
        print("Inside Base Class Destructor")
        super().__del__()
    
cobj = Child("omprasad")
del cobj

print("End Of Programme")
       
        