"""
    iRow = 5 iCol = 5
    1
    1       2
    1       2       3
    1       2       3       4
    1       2       3       4       5
"""

def Pattern(iRow,iCol):
    for i in range(1,iRow+1):
        j = 1
        while j <= i:
            print(f"{j}\t",end="")
            j+=1
        print()
        
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)