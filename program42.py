class Demo:
    def __init__(self):
        print("Inside Constructror")

    @staticmethod
    def static(iNo1,iNo2):
        return iNo1 + iNo2
    
    def Addition(self,x,y):
        return x+y
    
dobj = Demo()

iRet = dobj.static(12,12)
print(f"Static method is : {iRet}")

iRet = dobj.Addition(10,12)
print(f"Non- Static Method is :{iRet}")


        