"""
    iRow = 5 iCol = 5
    a
    b       b
    c       c       c
    d       d       d       d
"""

def Pattern(iRow,iCol):
    ch = ord('a')
    
    for i in range(1,iRow+1):
        j = 1
        while j <= i:
            print(f"{chr(ch)}\t",end="")
            
            j+=1
        ch +=1
        print()
        
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)