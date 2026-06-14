class Demo:
    def __init__(self,iNo1,iNo2):
        print(f"Inside Constructor")
    
    def Addition(self,*args):
        return sum(args)
    
    def __del__(self):
        print(f"Destructor Called")

dobj = Demo(10,12)
dobj.Addition(10,12,13,14)

del dobj
print("End of Program")


        