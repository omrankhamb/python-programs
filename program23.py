"""Function with multiple return values"""

def Custom (iNO,iNO2):
    return iNO-iNO2,iNO2 + iNO


a,b = Custom(12,13)

print(a,b)