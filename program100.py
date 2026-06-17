"""
   Sorting Of list by userdefined Function Bubble sort
"""


def Sort_List(Lis :list)->list:
    for i in range(0,len(Lis)):
        for j in range(0,len((Lis))):
            if Lis[j] > Lis[i]:
                temp =  Lis[j]
                Lis[j] =  Lis[i]
                Lis[i] = temp
    return Lis



lLis = list(map(int,input("Enter List By coma seprated Values : ").split(',')))
lRet = Sort_List(lLis)
print(f"Sorting of string is : {lRet}")