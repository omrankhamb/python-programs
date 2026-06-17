"""
    Summation of array
"""

def Summation(lis :list)->int:
    iSum = 0
    for i in lis :
        iSum = iSum + i

    return iSum


lLis = list(map(int,input("Enter elemets of list : ").split(',')))
iRet = Summation(lLis)

print(f"Addition of Array is {iRet}")