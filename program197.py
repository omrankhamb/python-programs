"""
    iRow = 5 iCol = 5
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    
"""


def Pattern(ino : int):
    for i in range(1,ino+1):
        for j in range(1,(ino-i)+1):
            print(f" ",end=" ")
        for k in range(1,(2*i - 1)+1):
            print(f"*",end=" ")
        print("\n")

def main():
    iValue = int(input("Enter Rows : "))
    Pattern(iValue)



if __name__ == "__main__" : 
    main()