"""
    .WAP to test whether a number is divisible by 3 and 15 or by 3 and 15. 
"""


def CheckDivisibleBy3And15(iNo :int)->bool:
    if iNo % 3 == 0 and iNo % 15 == 0:
        return True
    else :
        return False
    
iValue = int(input("Enter Number : "))
iRet = CheckDivisibleBy3And15(iValue)

if iRet :
    print("Number is Divisible by 3 and 15")
else :
    print("Number is NOT Divisible by 3 and 15")
