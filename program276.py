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
        

    def InsertFirst(self,iNo : int)->None:
        newn = None

        newn = node()
        newn.data = iNo
        newn.next = None

        if self.first == None and self.last == None :
            self.first = newn
            self.last  = newn
        else :
            newn.next = self.first
            self.first = newn

        self.last.next = self.first
        self.iCount+=1


    
def main()->None:

    sobj = SinglyCL()
    iRet = 0

    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    sobj.Display()
    iRet = sobj.Count()
    print(f"Numbe of Node are : {iRet}")

if __name__ == "__main__":
    main()