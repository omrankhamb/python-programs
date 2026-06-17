"""
    Given a string. Delete from it all the characters whose indices are divisible by 3. 
"""

def StringDivisibleBy3(sStr : str)->str:
    str = '\0'
    for i in range(0,len(sStr)):
        if i % 3 != 0:
            str = str+ sStr[i]

    return str
    
    
sStr = str(input("Enter String : "))
iRet = StringDivisibleBy3(sStr)

print(f"String is :\n{iRet}")