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

    
def main()->None:
    iRet = 0
    head = DobulyLinkedlist()

    head.InsertFirst(151)
    head.InsertFirst(111)
    head.InsertFirst(101)
    head.InsertFirst(51)
    head.InsertFirst(21)
    head.InsertFirst(11)

    head.Display()
    iRet = head.Count()
    print(f"Number of Node In Likelist are :{iRet}")

    
    





if __name__== "__main__":
    main()