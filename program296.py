class node :
    def __init__(self):
        self.data = None
        self.next = None

class Queue :
    def __init__(self):
       self.head = None
       self.iCount = 0

    def Enqueue(self,iNo)->None :   # adding element at last
        newn = node()
        self.data = iNo
        self.next = None
        
        if self.head == None :
            self.head = newn
        else :
            newn.next = self.head
            self.head = newn
        self.iCount +=1
    
    def Dequeue(self)->None:
        temp = None
    
    def Display(self)->None:
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

    iRet = obj.Count()
    print(f"Element in Queue is : {iRet}")
    


    

if __name__ == "__main__":
    main()