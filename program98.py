"""
   Program to Update the first set with items that don’t exist in the second set. 
    Consider any 2 sets. 

"""

# remove Element from set2 which are present in set1
def Set_Difference(S1: set,S2 : set)->set:
    return S1.difference(S2)

# Taking input
s1 = set(map(int,input("Enter first set : ").split(',')))
s2 = set(map(int,input("Enter Second set : ").split(',')))

s3 = Set_Difference(s1,s2)
print(s3)