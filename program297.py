class node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
       self.head = None
       self.iCount = 0

    def Enqueue(self,iNo)->None :   # adding element at last
        newn = node(iNo)
        
        if self.head == None :
            self.head = newn
        else :
            newn.next = self.head
            self.head = newn
        self.iCount +=1
    
    def Dequeue(self)->None:
        temp = None

        temp = self.head

        while temp.next.next != None :
            temp = temp.next

        del temp.next
        temp.next = None
        self.iCount -=1
    
    def Display(self)->None:
        temp = None
        temp = self.head

        while temp != None :
            print(f"|  {temp.data}  |")
            temp = temp.next
        print(f"|______|")
        return 0
    
    def Count(self)->int:
        return self.iCount

    

def main():
    print("Queue")

    obj = Queue()
    iRet = 0

    obj.Enqueue(11)
    obj.Enqueue(21)
    obj.Enqueue(51)
    obj.Enqueue(81)

    obj.Display()
    iRet = obj.Count()
    print(f"Element in Queue is : {iRet}")

    obj.Dequeue()

    obj.Display()
    iRet = obj.Count()
    print(f"Element in Queue is : {iRet}")
    


    

if __name__ == "__main__":
    main()