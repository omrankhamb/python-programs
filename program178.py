"""
    iRow = 4 iCol = 4
    4       4       4       4
    3       3       3       3
    2       2       2       2
    1       1       1       1
"""

def Pattern(iRow,iCol):
    ch = ord('A')
    for i in range(iRow,0,-1):
        ch = ord('a')
        for j in range(1,iCol+1):
            print(f"{i}\t",end="")
        print()
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)