"""
    WAP to check whether the number is Armstrong number or not. 
"""

def CheckArmstrong(iNo : int) ->True:
    isum = 0
    iNo2 = iNo
    while iNo != 0 :
        isum = isum + ((iNo % 10 )**3)
        iNo = iNo//10
    if isum == iNo2:
        return  True
    else :
        return False

iValue = int(input("Enter Number : "))
iRet = CheckArmstrong(iValue)

if iRet :
    print("Number is Armstrong")
else :
    print("Number is not armstrong")