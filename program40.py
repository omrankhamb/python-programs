"""OOP reating class and object"""

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Inside constructor")
    
    def display(self):
        print(f"Name : {self.name}\nmarks : {self.marks}")

    def __del__(self):
        print("Destructor called")

sobj = student("soham",98)
sobj.display()

del sobj
print("End of Programs")
        