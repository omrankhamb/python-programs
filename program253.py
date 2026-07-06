import sys

class NODE:
    def __init__(self,value):
        self.data = value
        self.next = None

    def display(self,first):
        while first != None:
            print(first.data)
            first = first.next

    def Count(self,first):
        iCnt = 0
        while first != None:
            first = first.next
            iCnt +=1
        return iCnt
    
    

    


def main():
    nobj = NODE(11)
    nobj2 = NODE(21)
    nobj3 = NODE(51)
    nobj4 = NODE(101)

    nobj.next = nobj2
    nobj2.next = nobj3
    nobj3.next = nobj4

    iRet = 0

    nobj.display(nobj)
    iRet = nobj.Count(nobj)
    print(f"Number of nodes in linkelist is : {iRet}")

if __name__ == "__main__":
    main()
