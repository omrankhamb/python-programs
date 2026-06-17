"""
    CountEven IN list
"""

def Maximum(lis :list)->int:
    iMax = lis[0]
    flag = False 
    for i in range(1,len(lis)):
        if iMax < lis[i]:
            iMax = lis[i]
    return iMax

lLis = list(map(int,input("Enter elemets of list : ").split(',')))

iRet = Maximum(lLis)
print(f"Maximum number in List : {iRet}")