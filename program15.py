import sys
"""String Inbuilt method in python"""
Str = "Jay ganesh"

print(Str)

print(Str[1:4])                                     # String slicing
print(Str[::-1])                                    # Revesing the string
print(f"Length Of string is : {len(str)}")          # Length of string
print(f"Converting upper to string : {str.upper()}")# Upper character of string
print(f"Converting Lower to string : {str.lower()}")# Lower character of string


Str2 = 'A' + Str                                    # String cancatenation
print(Str2)                     


str = "Omprasad"
str2 = "Omprasad"

print(str == str2)                                  # Refreces Of string are equal    
print(sys.getsizeof(str))                           # Size of string
print(id(str),id(str2))                             # Compairing id's 


a = list(str)                                       # Converting list to string


