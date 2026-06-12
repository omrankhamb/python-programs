"""String slicing"""

s = "Hello world"
print(s[0])
print(s[:11])               #String slicing
print(s[::-1])              # Print String in reverse manner

print('Python'.center(30, '-'))

# String method
# Lower to string
print(s.lower())     
print(s.upper())
print(s.capitalize())       # Only first character of all world
print(s.endswith("world"))  # endswith
print(s.startswith("H"))    # Startswith
print(s.find('o'))          # Returns Lowest index in string
print('omprasad'.islower()) # Returns true or not 

print(s.split())            # Split the world


print(len(s.encode('utf-8')))   # ENcodes number of byte required for string

