"""
    Program to Find the Factorial of a Number Using Recursion. 
"""

def Factorail(iNo : int)->bool:
    # base case
    if iNo == 0 :
        return 0
    # recursion call
    return iNo * Factorail(iNo-1)
    
iNo = int(input("Enter Number to find factorial: "))
iRet = Factorail()

print(f"Factorail of Number is {iRet}")