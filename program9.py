""" List in python """
import sys

numbers = []

print(type(numbers))                        # class of type List
print(sys.getsizeof(numbers))               # Size of List 56 Byte

numbers = [1,2,3,4,5]
print(numbers.append(4))                    #Add to List from start
print(numbers.pop())                        # Manually remove from otherwise required from index
print(numbers.count(3))                     # Get number and count Number of presence
print(numbers.extend([1,2,2]))              # To add more than one elements

print(numbers)

numbers2 = numbers.copy()
print(f"numbers2 id Copy {numbers2}")       # Shllow copy

print(id(numbers2))
print(id(numbers))

print(numbers2 == numbers)                  # Compares Content
print(numbers is numbers2)                  # Compares refreance

numbers = numbers2                          # Now refrence becomes equal
print(numbers2 is numbers)
