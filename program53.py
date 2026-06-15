""" Protected Access Specifiers"""

class Base :
    def __init__(self):
        self._iNo1 = 11
        self._iNO2 = 21

    def fun(self):
        print("Inside Non-static Method Display Of class Base")
    
    def __del__(self):
        del self._iNo1,self._iNO2
        print("Inside Base Destructor")

class Derived(Base):
    def __init__(self):
        super().__init__()

    def gun(self):
        print(f"Accessing from Derived class iNO1 = {self._iNo1},iNO2 = {self._iNO2}")
        super().fun()       # Calling base class fun method using super().fun()

    def __del__(self):
        print("Inside Derived Destructor")
        return super().__del__()
    
dobj = Derived()
dobj.gun()
    
        