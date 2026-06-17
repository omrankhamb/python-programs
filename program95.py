"""
    Program to check if a year is leap year or not. consider century year also.
"""

def LeapYearOrNot(year : int)->bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        return False
    else :
        return False

iyear = int(input("Entee Year to check leap or not : "))
iRet = LeapYearOrNot(iyear)

if iRet :
    print(f"{iyear} is leap year")
else:
    print(f"Is not a leap year")
    
