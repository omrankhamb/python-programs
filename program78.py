"""Sin function in Python"""

import math

def Side(fBase : float ,fHeight : float)->float:
    fAns = math.sqrt( (fHeight**2) + (fBase**2))
    return fAns

fBase = float(input("Enter Base : "))
fHeight = float(input("Enter Height : "))

fRet = Side(fBase,fHeight)
print(f"Hypotenuse side is : {fRet}")
