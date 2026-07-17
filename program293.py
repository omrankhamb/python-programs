class node:
    def __init__(self,data : int):
        self.data = data
        self.next = None

class Stack :
    def __init__(self):
        self.head = None
        self.iCount = 0

    def Display(self)->None :
        temp = None
        temp = self.head

        while temp != None :
            print(f"|  {temp.data}  |")
            temp = temp.next
        print(f"|______|")
        
        

    def Push(self,iNo :int)->None :
        newn = None

        newn = node(iNo)
        
        if self.head == None:
            self.head = newn
        else :
            newn.next = self.head
            self.head = newn
        
        self.iCount+=1

    def Pop(self)->int:
        iValue = 0
        target = None
        if self.head == None:
            print(f"Stack is Empty")
            return -1
        else :
            iValue = self.head.data
            target = self.head
            self.head = self.head.next
            del target
            self.iCount-=1

        return iValue
    
    def Pip(self)->None:

        if self.head == None :
            print(f"Stack is empty")
            return 
        
        return self.head.data

    def Count(self)->int:
        return self.iCount



    
def main():
    obj = Stack()
    iRet = 0

    obj.Push(11)
    obj.Push(21)
    obj.Push(51)
    obj.Push(81)

    obj.Display()
    iRet  = obj.iCount
    print(f"Number of element in stack in {iRet}")

    iRet = obj.Pop()

    obj.Display()
    print(f"Popped Element is : {iRet}")
    iRet  = obj.iCount
    print(f"Number of element in stack in {iRet}")

    iRet = obj.Pip()

    obj.Display()
    print(f"Pipped Element is : {iRet}")
    iRet  = obj.iCount
    print(f"Number of element in stack in {iRet}")



if __name__ == "__main__":
    main()