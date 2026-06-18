"""
    iRow = 4 iCol = 4
    A       B       C       D
    A       B       C       D
    A       B       C       D
    A       B       C       D
"""

def Pattern(iRow,iCol):
    ch = ord('A')
    for i in range(1,iRow+1):
        ch = ord('A')
        for j in range(1,iCol+1):
            print(f"{chr(ch)}\t",end="")
            ch +=1
        print()
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)