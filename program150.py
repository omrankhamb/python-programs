# Pass by refreance
def Update(lis :list)->int:
    iMin = lis[0]
    flag = False 
    for i in range(1,len(lis)):
        lis[i] = lis[i]**2

    

lLis = list(map(int,input("Enter elemets of list : ").split(',')))

Update(lLis)
print(f"Minimum number in List : {lLis}")