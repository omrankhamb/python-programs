class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCL:
    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0

    def Display(self)->None:
        temp = self.first

        print(f"<=> ",end="")
        while temp != self.last:
            print(f"| {temp.data} | <=> ",end="")
            temp = temp.next
        print(f"| {temp.data} | <=> ",end="")
        print()
        

    def Count(self):
        return self.iCount
    
    def InsertFirst(self,iNo : int):
        newn  = None
        newn = node(iNo)

        if((self.first == None) and (self.last == None)):
            self.first = newn
            self.last = newn
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn
        self.last.next = self.first
        self.first.prev = self.last
        self.iCount+=1
    

    





def main()->None:
    dobj = DoublyCL()
    iRet = 0

    dobj.InsertFirst(51)
    dobj.InsertFirst(21)
    dobj.InsertFirst(11)

    dobj.Display()
    iRet = dobj.Count()
    print(f"Number of Node Are : {iRet}")

if __name__ == "__main__":
    main()