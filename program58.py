class Base:
    def __init__(self):
        print("Inside Base Constructor")

    # Protected Functionn 
    def _show(self):
        print("Base Protected Function")

    def __del__(self):
        print("inside Base Destructor")


bobj = Base()
bobj._show()    # Not Good Programming Practise



    