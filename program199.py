"""
    iRow = 5 iCol = 5
                    *
                  * * *
                * * * * *
              * * * * * * *
            * * * * * * * * *
              * * * * * * *
                * * * * *
                  * * *
                    *
    
"""


def Pattern(ino : int):
    for i in range(1,ino):
        for j in range(1,(ino-i)+1):
            print(f" ",end=" ")
        for k in range(1,(2*i - 1)+1):
            print(f"*",end=" ")
        print()
    for i in range(ino,0,-1):
        for j in range(1,(ino - i)+1):
            print(" ",end=" ")
        for k in range(1,(2*i -1)+1):
            print("*",end=" ")

        print()

def main():
    iValue = int(input("Enter Rows : "))
    Pattern(iValue)



if __name__ == "__main__" : 
    main()