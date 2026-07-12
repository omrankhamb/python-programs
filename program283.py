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

    def Count(self):
        return self.iCount
    
    

    





def main()->None:
    print("Hello")

if __name__ == "__main__":
    main()