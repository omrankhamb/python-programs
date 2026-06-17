"""
    Write a python program to find the roots of a quadratic equation. The standard 
form of quadratic equation is  
"""

import math
def RootOfEquation(a : int,b : int,c : int)->int:
    if (b**2) - (4*a*c) < 0 :
        print("Enter Root are not real")
        return "Not real","Not real"
    root1 = (-b) + math.sqrt( (b**2) - (4*a*c))
    root2 = (-b) - math.sqrt( (b**2) - (4*a*c))
    return root1,root2

a,b,c = map(int,input("Enter coefficint a,b,c By comma Separatedd : ").split(","))

r1,r2 = RootOfEquation(a,b,c)
print(f"Root of equation is : {r1} and {r2}")
