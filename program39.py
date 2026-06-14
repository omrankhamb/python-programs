"""OOP reating class and object"""

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Inside constructor")
    
    def display(self):
        print(f"Name : {self.name}\nmarks : {self.marks}")

sobj = student("soham",98)
sobj.display()
        