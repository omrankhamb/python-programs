"""
    Sum Of Factor
"""

def SumOfFactor(iNo):
    iSum = 0
    if iNo < 0 :
        iNo = -iNo
    for i in range(1,iNo//2 + 1):
        if iNo % i == 0:
            iSum = iSum + i
    return iSum

iValue = int(input("Enter NuUmber : "))
iRet = SumOfFactor(iValue)
print(f"Sum of factor is : {iRet}")
