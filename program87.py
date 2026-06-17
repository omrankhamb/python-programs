"""
    Program to Remove the Duplicate Items from a List.
"""

# using List To remove Duplicate
def duplicate(Lis : list,x : int)->list:
    count = 0
    for i in range(0,len(Lis)):
        if x == Lis[i]:
            count +=1
            if count == 2:
                return True
            
    return False


lLis = list(map(int,input("Enter List by Comma : ").split(",")))
lLis2 = []
for _ in lLis :
    if duplicate(lLis,_):
        print(_)
        continue
    else :
        lLis2.append(_)
print(lLis2)
