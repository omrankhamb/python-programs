"""
    iRow = 4 iCol = 4
    a       b       c       d
    1       2       3       4
    a       b       c       d
    1       2       3       4
"""

def Pattern(iRow,iCol):
    ch = ord('A')
    for i in range(1,iRow+1):
        ch = ord('a')
        for j in range(1,iCol+1):
            if i % 2 == 1:
                print(f"{chr(ch)}\t",end="")
                ch +=1
            else :
                print(f"{j}\t",end="")
        print()
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)