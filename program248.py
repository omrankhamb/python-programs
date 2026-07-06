import sys

class NODE:
    def __init__(self,value):
        self.data = value
        self.next = None



def main():
    nobj = NODE(12)
    print(f"Size of node is : {sys.getsizeof(nobj)}")



if __name__ == "__main__":
    main()