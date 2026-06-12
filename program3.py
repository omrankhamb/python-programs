"""Integer in pyhton"""

import sys

i = 11
print(type(i))                  # Type int
print(sys.getsizeof(i))         # size is 28 byte


char = ''
print(type(char))               # String comparsion
print(sys.getsizeof(char))      # size id 41 byte

No = 12345

print(No.__ceil__())