"""
    CountEven IN list
"""

def Linearsearch(lis :list,iValue : int)->bool:
    iCount = 0
    flag = False 
    for i in lis :
        if i == iValue :
            break
        iCount +=1


    if iCount < len(lis):
        return True
    else :
        return False
    


lLis = list(map(int,input("Enter elemets of list : ").split(',')))
iValue = int(input("Eneter Number to find in array : "))

iRet = Linearsearch(lLis,iValue)

if iRet:
    print(f"Number present in List")
else:
    print("Number not present in list")