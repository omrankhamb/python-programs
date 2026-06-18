"""
    iRow = 5 iCol = 5
    a
    a       b
    a       b       c
    a       b       c       d
"""

def Pattern(iRow,iCol):
    for i in range(1,iRow+1):
        ch = ord('a')
        j = 1
        while j <= i:
            print(f"{chr(ch)}\t",end="")
            ch +=1
            j+=1
        print()
        
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)