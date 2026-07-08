class NODE:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = None
        temp = self.head

        while temp != None:
            print(f"|{temp.data}|->",end="")
            temp = temp.next

        print(f"NULL")

    def Count(self):
        temp = None
        temp = self.head
        iCnt = 1

        while temp.next != None:
            iCnt +=1
            temp = temp.next
            
        return iCnt
    
    def InsertFirst(self,data):
        newn = None
        newn = NODE(data)

        if self.head == None:
            self.head = newn
        else:
            newn.next = self.head
            self.head = newn

    def InsertLast(self,data):
        newn = None
        newn = NODE(data)

        if self.head == None:
            self.head = newn
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newn

    def InsertAtPos(self,data : int ,Pos : int):
        temp = None
        newn = None
        iLength = 0
        iLength = self.Count()

        if Pos < 1 or Pos > iLength + 1:
            print(f"Invliad position")

        if Pos == 1:
            self.InsertFirst(data)
        elif Pos == iLength + 1:
            self.InsertLast(data)
        else:
            temp = self.head
            newn = NODE(data)
            for _ in range(1,Pos - 1,1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn       

    def DeleteFirst(self):
        temp = None
        temp = self.head
        self.head = self.head.next
        del temp

    def DeleteLast(self):
        temp = None
        temp = self.head

        while temp.next.next != None:
            temp = temp.next

        newn = temp.next
        temp.next = None
        del newn

    def DeleteAtPos(self,Pos):
        temp = None
        newn = None
        iLength = 0
        iLength = self.Count()
        
        if Pos < 1 or Pos > iLength + 1:
            print(f"Invliad position")

        if Pos == 1:
            self.DeleteFirst()
        elif Pos == iLength:
            self.DeleteLast()
        else:
            temp = self.head
            for i in range(1,Pos-1,1):
                temp = temp.next
            
            newn = temp.next
            temp.next = newn.next
            del newn

    def Search(self,iNo:int)->bool:
        temp = None
        temp = self.head
        bflag = False

        while temp != None:
            if(temp.data == iNo):
                bflag = True
                break
            temp = temp.next

        return bflag
    
    def CountEven(self)->int:
        temp = None
        iCnt = 0

        temp = self.head

        while temp != None:
            if temp.data % 2 == 0:
                iCnt +=1
            temp = temp.next

        return iCnt
    
    def CountOdd(self)->int:
        temp = None
        iCnt = 0

        temp = self.head

        while temp != None:
            if temp.data % 2 == 1:
                iCnt +=1
            temp = temp.next

        return iCnt
    
    def Frequency(self,iNo : int)->int :
        temp = None
        iCnt = 0

        temp = self.head

        while temp != None:
            if temp.data == iNo:
                iCnt+=1
            temp = temp.next

        return iCnt
    
    def DisplayEven(self)->None:
        temp = None
        temp = self.head

        while temp != None:
            if temp.data % 2 == 0:
                print(f"{temp.data}")
            temp = temp.next

    


    
def main():
    head = Linkedlist()
    iRet = 0

    head.InsertFirst(111)
    head.InsertFirst(101)
    head.InsertFirst(60)
    head.InsertFirst(51)
    head.InsertFirst(30)
    head.InsertFirst(21)
    head.InsertFirst(11)

    head.display()
    iRet = head.Count()
    print(f"Number of Node in Linkedlist is : {iRet}")

    head.InsertLast(121)
    
    head.display()
    iRet = head.Count()
    print(f"Number of Node in Linkedlist is : {iRet}")

    head.DeleteFirst()
    
    head.display()
    iRet = head.Count()
    print(f"Number of Node in Linkedlist is : {iRet}")

    head.DeleteLast()
    
    head.display()
    iRet = head.Count()
    print(f"Number of Node in Linkedlist is : {iRet}")

    head.InsertAtPos(41,3)
    
    head.display()
    iRet = head.Count()
    print(f"Number of Node in Linkedlist is : {iRet}")

    head.DeleteAtPos(3)
    
    head.display()
    iRet = head.Count()
    print(f"Number of Node in Linkedlist is : {iRet}")

    print(f"\n\n")

    bRet = head.CountEven()
    print(f"Even Node is {bRet}")


if __name__ == "__main__":
    main()