"""
    Program to Find all Numbers in a Range which are Perfect Squares and Sum of 
    all Digits in the Number is Less than 10.
"""

import math
# Cheack SSquareroot
def Isquare_root(iNo )->bool:
    root = math.sqrt(iNo)
    return root.is_integer()

# Check Sum is Less than 10
def SumIsLessThanTen(iNo : int)->bool:
    sum = 0
    while iNo != 0:
        sum = sum + (iNo % 10)
        iNo = iNo//10
        if(sum > 10) : 
            return False
    
    return True

def Function(iNo :int)->bool:
    if Isquare_root(iNo) :
        if SumIsLessThanTen(iNo):
            return True
    else:
        return False

    
# Taking Range
iStart,iend = map(int,(input("Enter Range By Comma : ").split(',')))

for i in range(iStart,iend+1):
    print("The Rule sould follow")
    if(Function(i)):
        print(i,end=" ")



