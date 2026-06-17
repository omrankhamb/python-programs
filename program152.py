# Class contaning array

class ArrayX:
    def __init__(self):
        print("Inside Constructor")
        self.lLis = []
        print(type(self.lLis))

    def inputX(self,*args):
        for i in args:
            self.lLis.append(i)

    def Display(self):
        print(self.lLis)

    def GetSize(self):
        return len(self.lLis)

    def __del__(self):
        del self.lLis
        print("Inside destructor")


aobj= ArrayX()
aobj.inputX(1,2,3,4,5,6)
aobj.Display()
print(aobj.GetSize())

del aobj



        