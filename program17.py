import sys
"""Set in python"""

#Set is used to store unique values
set = {1,2,3,4}

print(type(set))                        #
#print(set[1])                          Not alloewd
print(set.add(12))                      # Adding element to set at last

for i in set :
    print(i,end=" ")                    # Printing whole set

print()
"""Set properties"""
set1 = {1,2,3,4,6,8}
set2 = {5,6,7,8,4,2}

print(set1.union(set2))                 # all values present in setq and set2
print(set1.difference(set2))            # Uniuque values only on set 1
print(set1.intersection(set2))          # Common values Between set1 and set2
print(set1.symmetric_difference(set2))  # Opposite of Union
print(sys.getsizeof(set.clear()))       # Size of set

dict = set({})

print(type(dict))                           # Type is set

