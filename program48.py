class Demo:
    def __init__(self,iNo1,iNo2):
        self.iNo1 = iNo1
        self.iNo2 = iNo2
        print("Inside Demo1 Construtor")

    def Addition(self):
        return self.iNo1 + self.iNo2
    
    def Multiplication(self):
        return self.iNo1 * self.iNo2

    def __del__(self):
        print("Inside Demo1 Destructor")

class Demo2(Demo):
    def __init__(self,iNo1,iNo2):
        self.iNo1 = iNo1
        self.iNo2 = iNo2
        super().__init__(self.iNo1,self.iNo2)
        print("Inside Demo2 Constructor")

    def Substraction(self):
        return self.iNo1 - self.iNo2
    
    def Division(self):
        return self.iNo1 / self.iNo2


    def __del__(self):
        print("Inside Demo2 Destructor")
        return super().__del__()

class Demo3(Demo2):
    def __init__(self,iNo1,iNo2):
        self.iNo1 = iNo1
        self.iNo2 = iNo2
        super().__init__(self.iNo1,self.iNo2)
        print("Inside Demo3 Constructor")

    def __del__(self):
        print("Inside Demo3 Destructor")
        return super().__del__()
    
dobj = Demo3(11,21)
# Addition From Demo
iret = dobj.Addition()
print(iret)

# Multiplcation From Demo
iret = dobj.Multiplication()
print(iret)

# Substraction Frmo Demo2
iret = dobj.Substraction()
print(iret)

# Division From Demo2
iret = dobj.Division()
print(iret)

del dobj
print("End Of Programme")


