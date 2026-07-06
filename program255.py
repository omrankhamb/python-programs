class NODE:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def InsertFirst(self,data):
        newn = NODE(data)

        if self.head == None:
            self.head = newn
        else:
            newn.next = self.head
            self.head = newn

    def InsertLast(self,data):
        newn = NODE(data)

        if self.head == None:
            self.head = newn
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newn

    def display(self):
        temp = self.head

        while temp != None:
            print(f"|{temp.data}|->",end="")
            temp = temp.next

        print(f"NULL")

    def Count(self):
        temp = self.head
        iCnt = 1

        while temp.next != None:
            iCnt +=1
            temp = temp.next
            
        
        return iCnt



def main():
    head = Linkedlist()
    iRet = 0

    head.InsertFirst(101)
    head.InsertFirst(51)
    head.InsertFirst(21)
    head.InsertFirst(11)

    head.display()
    iRet = head.Count()
    print(f"Number of Node in Linkedlist is : {iRet}")

    head.InsertLast(121)
    
    head.display()
    iRet = head.Count()
    print(f"Number of Node in Linkedlist is : {iRet}")

if __name__ == "__main__":
    main()