class Base:
    #Base Constructor
    def __init__(self):
        print("Inside Base Constructor")

    # Protected Functionn 
    def _show(self):
        print("Base Protected Function")

    # Base Destructor
    def __del__(self):
        print("inside Base Destructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Insode Derived Constructor")

    def fun(self):
        # calling Base function Self._show()
        self._show()

    def __del__(self):
        print("Inside Derived Destructor")
        # Call Of base Destructor
        return super().__del__()


dobj = Derived()
dobj.fun()      # Good Progammimg Practise
dobj._show()    # NOt Good Programming Practise


    