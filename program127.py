"""
    Sum Of Factor
"""

def CheckPerfect(iNo : int)->bool:
    iSum = 0
    if iNo < 0 :
        iNo = -iNo
    for i in range(1,iNo//2 + 1):
        if iNo % i == 0:
            iSum = iSum + i
    
    if iSum == iNo:
        return True
    else : 
        return False

iValue = int(input("Enter NuUmber : "))
iRet = CheckPerfect(iValue)

if iRet == True :
    print("Number is perfect")
else:
    print("Number is not perfect")
