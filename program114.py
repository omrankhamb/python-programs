"""
    Function to Find the Sum of the Digits of the Number Recursively.
"""

#recursion

def Sum(iNo : int)->int :
    if(iNo == 0 ):
        return 0
    
    sum = 0 
    sum = iNo%10 + Sum(iNo//10)
    return sum

iValue = int(input("Enter Number : "))
iRet = Sum(iValue)

print(f"Sum of {iValue} od digit is : {iRet}")
del iValue,iRet