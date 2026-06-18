"""
    iRow = 4 iCol = 4
    1       1       1       1
    2       2       2       2
    3       3       3       3
    4       4       4       4
"""

def Pattern(iRow,iCol):
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            print(f"{i}\t",end="")
        print()
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)