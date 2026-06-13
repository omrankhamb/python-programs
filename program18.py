"""Dictionaries in python"""
import sys
dict = {}
# Dictionaries is akey value pairs
print(type(dict))                           # Type is dict
print(sys.getsizeof(dict))                  # Size of Empty dictionary is 64 Byte


book ={
    "BigBangTeorey" : 2000,
    "MissileMan"    : 1000
}

for key, value in book.items():
    print("Key :",key,"Values:",value)

print(book)                                 # Printing String
print(book.keys())                          # printing only keys
print(book.values())                        # Printing Values of Dictionary
print(book.get("MissileMan"))               # Getting value of a key not present no error
print(f"Dictionary is {book}")
print(book["MissileMan"])
#print(book["omprasad"]) ERROR
print(book.get("omprasad"))                 # No error
print(book.pop("MissileMan"))               # Remove key value pair from dictionary
print(book.popitem( ))                      # Returns last Key valued pair

for key in book:
    print(key,end=" ")                      # Iterate thorugh Dictionary Keys

for key in book.values():
    print(key,end=" ")                      # Iterate thorugh Dictionary Values

del book                                    # Delting the book


