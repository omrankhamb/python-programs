class Base:
    def __init__(self):
        print("Inside Demo Constructor")

    def Addition(self,iNo1,iNO2):
        return iNo1 + iNO2

    def __del__(self):
        print("Inside Destructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside Demo2 Constructor")
    

dobj = Derived()

