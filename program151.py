# Class contaning array

class ArrayX:
    def __init__(self):
        self.lLis = []
        print(type(self.lLis))

    def inputX(self,*args):
        for i in args:
            self.lLis.append(i)

    def Display(self):
        print(self.lLis)

    def __del__(self):
        print("Inside destructor")


aobj= ArrayX()
aobj.inputX(1,2,3,4,5,6)
aobj.Display()

        