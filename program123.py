"""
    Python Program to Display Powers of 2 Using Anonymous Function  
"""

Addition = lambda x : x**2

iStart,iend = map(int,input("Enter Range : ").split(','))

for i in range(iStart,iend+1):
    print(Addition(i))
