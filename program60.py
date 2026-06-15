class Base:
    def __init__(self):
        print("Inside Base Constrctor")

    def __Show(self):
        print("Private Function")

    def __del__(self):
        print("Inside Base Destructor")

bobj = Base()
bobj.__Show()   #Error