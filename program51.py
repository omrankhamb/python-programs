""" Public Access Specifiers"""

class Demo:
    def __init__(self,name,age):
        # Publbic Access Specifer
        self.name = name
        self.age = age
        print(f"Inside Constructor")

    def display(self):
        print(f"Hello My name is :{self.name}\nMy age is : {self.age} ")

    def __del__(self):
        del self.name
        del self.age
        print("Inside Destructor")

dobj = Demo("Soham",21)
dobj.display()

del dobj
print("Inside End Programlass")



        