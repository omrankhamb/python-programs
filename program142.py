"""
    CountEven IN list
"""

def CountEven(lis :list)->int:
    iCount = 0
    for i in lis :
        if i % 2 == 0:
            iCount +=1
    return iCount


lLis = list(map(int,input("Enter elemets of list : ").split(',')))
iRet = CountEven(lLis)

print(f"Even number in array :  {iRet}")