import sys

class NODE:
    def __init__(self,value):
        self.data = value
        self.next = None



def main():
    nobj = NODE(11)
    nobj2 = NODE(21)
    nobj3 = NODE(51)
    nobj4 = NODE(101)

    nobj.next = nobj2
    nobj2.next = nobj3
    nobj3.next = nobj4

    no = nobj
    while no != None:
        print(no.data)
        no = no.next

if __name__ == "__main__":
    main()
