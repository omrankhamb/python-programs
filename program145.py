"""
    CountEven IN list
"""

def LinearSearch(lis :list,iValue : int)->int:
    iCount = 0
    flag = False 
    for i in lis :
        if i == iValue :
            flag = True
            break

    return flag
    


lLis = list(map(int,input("Enter elemets of list : ").split(',')))
iValue = int(input("Eneter Number to find in array : "))

iRet = LinearSearch(lLis,iValue)

if iRet:
    print(f"Number present in List")
else:
    print("Number not present in list")