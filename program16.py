"""Tuple in python """
import sys
tup = (1,2,3,4,5,3,4)

'''Tuple is immutable 
once written no one can add and remove element from tuple no one can edit tuple
'''


print(tup)
print(sys.getsizeof(tup))                   # Size of tuple is
print(tup.count(4))                         # Count the Particular index
print(tup.index(2))                         # Give the first index of element
print(id(tup))                              # Address in pyton
print(tup[2:8])                             # Slicing in tuple
tup3 = (1,2,3) + tup                        # adding two tuple

print(tup3)

del tuple                                   # deleting the tuple Important step
