"""
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5  
"""

def Display(iRow : int,iCol : int):
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            if(j <= i):
                print(f"{j}\t",end="")
        print()

iValue1 ,iValue2 = map(int,input("Enter rows and columns : ").split(','))
Display(iValue1,iValue2)
