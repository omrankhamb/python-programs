class Base:
    def __init__(self):
        print("Inside Base Constrctor")

    def __Show(self):
        print("Private Function")

    def fun(self):
        print("Call from object")
        # call to Private function
        self.__Show()
        

    def __del__(self):
        print("Inside Base Destructor")

bobj = Base()
#bobj.__Show()
bobj.fun()