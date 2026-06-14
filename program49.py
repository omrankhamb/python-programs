"""Hierarchical Inheritance OOP"""

class Base:
    def __init__(self):
        print("Inside Base Constructor")

    def __del__(self):
        print("Inside Base Destructor")

class Derived1(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived1 Constructor")

    def __del__(self):
        print("Inside Derived1 Destructor")
        return super().__del__()
    

class Dervied2(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived2 Constructor")

    def __del__(self):
        print("Inside Derived2 Destructor")
        return super().__del__()
    
# Creting object Of Dreived1
print(f"Object Of Derived1 :")
dobj = Derived1()
del dobj

# Creting Object Of Derived2
print(f"Object Of Derived2 :")
dobj2 = Dervied2()
del dobj2

print("End Of Programme")
