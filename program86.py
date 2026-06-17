"""
    Program to Remove the Duplicate Items from a List.
"""

# using List To remove Duplicate
def duplicate(Lis : list)->list:
    Lis = set(Lis)
    Lis = list(Lis)
    return Lis


lLis = list(map(int,input("Enter List by Comma : ").split(",")))
Lis = duplicate(lLis)
print(Lis)
