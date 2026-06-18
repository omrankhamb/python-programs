"""
    iRow = 5 iCol = 5
    *
    *       *
    *       $       *
    *       $       $       *
    *       $       $       $       *
    *       *       *       *       *       *
"""

def Pattern(iRow,iCol):
    ch = ord('a')
    
    for i in range(1,iRow+1):
        j = 1
        while j <=i :
            if i == j or j == 1 or i == iRow:
                print(f"*\t",end="")
            else:
                print(f"$\t",end="")
            j+=1

        print()
        
        
        

iValue,iValue2 = map(int,input("Enter Number of Rows and Column : ").split())
Pattern(iValue,iValue2)