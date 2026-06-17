"""
    CountEven IN list
"""

def CountOdd(lis :list)->int:
    iCount = 0
    for i in lis :
        if i % 2 != 0:
            iCount +=1
    return iCount


lLis = list(map(int,input("Enter elemets of list : ").split(',')))
iRet = CountOdd(lLis)

print(f"Odd number in array :  {iRet}")