"""
   Sorting Of list by userdefined Function Bubble sort
"""


def Sort_List(Lis :str)->str:
    Lis = list(Lis)
    for i in range(0,len(Lis)):
        for j in range(0,len((Lis))):
            if (Lis[j]) > (Lis[i]):
                temp =  Lis[j]
                Lis[j] =  Lis[i]
                Lis[i] = temp
    return ''.join(Lis)



sStr = str(input("Enter List By coma seprated Values : "))
lRet = Sort_List(sStr)
print(f"Sorting of string is : {lRet}")