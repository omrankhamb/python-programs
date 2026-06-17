"""
    A 
    A   B
    A   B   C
    A   B   C    D   
    A   B   C    D   E   
"""

def Display(iRow : int,iCol : int):
    ch = 'A'
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            if(j <= i):
                print(f"{(chr(64+j))}\t",end="")
        print()

iValue1 ,iValue2 = map(int,input("Enter rows and columns : ").split(','))
Display(iValue1,iValue2)

