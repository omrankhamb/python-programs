"""
    Python program to accept the base and perpendicular and find the hypotenuse 
of a right-angled triangle.
"""

import math
def Side(fBase : float ,fHeight : float)->float:
    fAns = math.sqrt( (fHeight**2) + (fBase**2))
    return fAns

fBase = float(input("Enter Base : "))
fHeight = float(input("Enter Height : "))

fRet = Side(fBase,fHeight)
print(f"Hypotenuse side is : {fRet}")
