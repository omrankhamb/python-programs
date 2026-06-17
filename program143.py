"""
    CountEven IN list
"""

def SumOfEven(lis :list)->int:
    iCount = 0
    for i in lis :
        if i % 2 == 0:
            iCount += i
    return iCount


lLis = list(map(int,input("Enter elemets of list : ").split(',')))
iRet = SumOfEven(lLis)

print(f"Sum of even Number in array :  {iRet}")