"""
   Write a program to reverse 4-digit number using % and // operators. 
"""


def Reverse(iNo : int)->int:
    if iNo < 0:
        iNo = -iNo

    iRev = 0
    while iNo != 0:
        iRev = (iRev*10) + (iNo %10)
        iNo = iNo // 10
    return iRev

iValue = int(input("Enter Number : "))
iRet = Reverse(iValue)
print(f"Reverse of number is : {iRet}")