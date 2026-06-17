"""
    Function to check if a number is even or odd and return the result to the function.
"""


def CheckEvenOrOdd(iNo :int)->bool:
    if iNo % 2 == 0 :
        return True
    else :
        return False
    
iValue = int(input("Enter Number : "))
iRet = CheckEvenOrOdd(iValue)

if iRet :
    print("Number is EVEN")
else :
    print("Number is ODD")
