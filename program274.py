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


    def InsertLast(self,iNo : int)->None:
        newn  = None

        newn = node()
        newn.data = iNo
        newn.next = None

        if self.first == None and self.last == None :
            self.first = newn
            self.last = newn
        else:
            self.last.next = newn
            self.last = self.last.next

        self.last.next = self.first
        self.iCount+=1

    def InsertAtPos(self,iNo : int,iPos:int)->None :
        newn = None
        temp = None
        i = 0

        if iPos < 1 or iPos > self.iCount + 1:
            print(f"Invalid Position")
            return
        
        if iPos == 1 :
            self.InsertFirst(iNo)
        elif iPos == self.iCount + 1:
            self.InsertLast(iNo)
        else :
            temp = self.first

            for _ in range(1,iPos-1,1):
                temp = temp.next
            
            newn = node()

            newn.data = iNo
            newn.next = None

            newn.next = temp.next
            temp.next = newn
            self.iCount +=1


    def DeleteFirst(self):
        
        if self.first == None and self.last == None:
            return
        elif self.first == self.last:
            del self.first
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            del self.last.next
            self.last.next = self.first
        self.iCount -=1


    def DeleteLast(self):
        temp = None

        if self.first == None and self.last == None:
            return
        elif self.first == self.last:
            del self.first
            self.first = None
            self.last = None
        else:
            temp = self.first

            while temp.next != self.last:
                temp = temp.next

            del temp.next
            self.last = temp
            self.last.next = self.first


        self.iCount -=1

    def DeleteAtPos(self,iPos)->None:
        temp = None
        target = None
        i = 0

        if iPos < 1 or iPos > self.iCount + 1:
            print(f"Invalid Position")
            return
        
        if iPos == 1 :
            self.DeleteFirst()
        elif iPos == self.iCount:
            self.DeleteLast()
        else :
            temp = self.first

            for _ in range(1,iPos-1,1):
                temp = temp.next

            target = temp.next

            temp.next = target.next
            del target

            self.iCount -=1
            


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

    sobj.InsertLast(111)

    sobj.Display()
    iRet = sobj.Count()
    print(f"Numbe of Node are : {iRet}")

    sobj.DeleteFirst()

    sobj.Display()
    iRet = sobj.Count()
    print(f"Numbe of Node are : {iRet}")

    sobj.DeleteLast()

    sobj.Display()
    iRet = sobj.Count()
    print(f"Numbe of Node are : {iRet}")

    sobj.InsertAtPos(1000,2)

    sobj.Display()
    iRet = sobj.Count()
    print(f"Numbe of Node are : {iRet}")

    sobj.DeleteAtPos(2)

    sobj.Display()
    iRet = sobj.Count()
    print(f"Numbe of Node are : {iRet}")


if __name__ == "__main__":
    main()