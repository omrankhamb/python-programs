
def Minimum(lis :list)->int:
    iMin = lis[0]
    flag = False 
    for i in range(1,len(lis)):
        if iMin > lis[i]:
            iMin =  lis[i]
    return iMin

lLis = list(map(int,input("Enter elemets of list : ").split(',')))

iRet = Minimum(lLis)
print(f"Minimum number in List : {iRet}")