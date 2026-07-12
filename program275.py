class node:
    def __init__(self):
        self.data = 0
        self.next = None

class SinglyCL:
    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0

    def Display(self)->None:
        temp = self.first

        while temp != self.last:
            print(f"| {temp.data} | ->",end="")
            temp = temp.next
        print(f"| {temp.data} | ->",end="")
        print("")

    def Count(self)->int:
        return self.iCount
        

    
def main()->None:

    sobj = SinglyCL()
    iRet = 0

    
if __name__ == "__main__":
    main()