"""
    iRow = 4 iCol = 4
    *       *       *       *
    *       *       *       *
    *       *       *       *
    *       *       *       *
"""

def Pattern(iRow,iCol):
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            print(f"*\t",end="")
        print()
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)