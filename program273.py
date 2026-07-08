# Implemetation Of Doubly LinkedList

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class DobulyLinkedlist:
    def __init__(self):
        self.head = None

    def Display(self)->None:
        temp = None
        temp = self.head

        print(f"NULL <=> ",end="")
        while temp != None:
            print(f"| {temp.data} | <=> ",end="")
            temp = temp.next
        print(f"NULL")

    def Count(self)->int:
        temp = None
        iCnt = 0
        temp = self.head

        while temp != None:
            iCnt +=1
            temp = temp.next

        return iCnt
    
    def InsertFirst(self,iNo : int)->None:
        newn = None
        newn = node(iNo)

        if self.head == None:
            self.head = newn
        else:
            newn.next = self.head
            self.head.prev = newn
            self.head = newn

    def InsertLast(self,iNo : int)->None:
        newn = None
        temp = None
        newn = node(iNo)

        if self.head == None:
            self.head = newn
        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next
            
            temp.next = newn
            newn.prev = temp

    def InsertAtPos(self,iNo : int ,iPos : int)->None:
        i = 0
        iCount = self.Count()
        newn = None
        temp = None

        if iPos < 1 or iPos > (iCount + 1):
            print("Invalid Position")

        if iPos == 1:
            self.InsertFirst(iNo)
        elif iPos == (iCount + 1):
            self.InsertLast(iNo)
        else:
            temp = self.head

            for _ in range(1,iPos - 1,1):
                temp = temp.next

            newn = node(iNo)

            newn.next = temp.next
            temp.next.prev = newn
            temp.next = newn
            newn.prev = temp

    def DeleteFirst(self):
        newn = None

        if self.head == None:
            return
        elif self.head.next == None:
            newn = self.head.next
            del newn
            self.head = None
        else :
            self.head = self.head.next

    def DeleteLast(self):
        newn = None
        temp = None

        if self.head == None:
            return
        elif self.head.next == None:
            newn = self.head.next
            del newn
            self.head = None
        else :
            temp = self.head

            while temp.next.next != None :
                temp = temp.next

            newn = temp.next
            del newn
            temp.next = None

    def DeleteAtPos(self,iPos : int)->None:
        temp = None
        iCount = self.Count()

        if iPos < 1 or iPos > iCount:
            print("Invalid Position")

        if iPos == 1:
            self.DeleteFirst()
        elif iPos == (iCount):
            self.DeleteLast()
        else:
            temp = self.head

            for i in range(1,iPos-1,1):
                temp = temp.next

            temp.next = temp.next.next
            temp.next.prev = temp
            
def main()->None:
    iRet = 0
    head = DobulyLinkedlist()

    head.InsertFirst(101)
    head.InsertFirst(51)
    head.InsertFirst(21)
    head.InsertFirst(11)

    head.Display()
    iRet = head.Count()
    print(f"Number of Node In Likelist are :{iRet}")

    head.InsertLast(111)
    head.InsertLast(151)

    head.Display()
    iRet = head.Count()
    print(f"Number of Node In Likelist are :{iRet}")  

    head.DeleteFirst()

    head.Display()
    iRet = head.Count()
    print(f"Number of Node In Likelist are :{iRet}")  

    head.DeleteLast()

    head.Display()
    iRet = head.Count()
    print(f"Number of Node In Likelist are :{iRet}")

    head.InsertAtPos(60,3)

    head.Display()
    iRet = head.Count()
    print(f"Number of Node In Likelist are :{iRet}")

    head.DeleteAtPos(3)

    head.Display()
    iRet = head.Count()
    print(f"Number of Node In Likelist are :{iRet}")

if __name__== "__main__":
    main()