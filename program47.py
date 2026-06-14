class Demo:
    def __init__(self):
        print("Inside Demo1 Construtor")

    def __del__(self):
        print("Inside Demo1 Destructor")

class Demo2(Demo):
    def __init__(self):
        super().__init__()
        print("Inside Demo2 Constructor")

    def __del__(self):
        print("Inside Demo2 Destructor")
        return super().__del__()

class Demo3(Demo2):
    def __init__(self):
        super().__init__()
        print("Inside Demo3 Constructor")

    def __del__(self):
        print("Inside Demo3 Destructor")
        return super().__del__()
    
dobj = Demo3()
del dobj
print("End Of Programme")


