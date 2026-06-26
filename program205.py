"""
    iRow = 5 iCol = 5
            *        *
            **      **
            ***    ***
            ****  ****
            **********
            ****  ****
            ***    ***
            **      **
            *        *
    
"""


def Pattern(ino : int):
    for i in range(1,ino):
        print("*" * i + " " *(ino - i),end="")
        print(" " *(ino - i) + "*" * i)
    for i in range(ino,0,-1):
        print("*" * i + " " *(ino - i),end="")
        print(" " *(ino - i) + "*" * i)
def main():
    iValue = int(input("Enter Rows : "))
    Pattern(iValue)



if __name__ == "__main__" : 
    main()