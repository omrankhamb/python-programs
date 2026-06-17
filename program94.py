"""
    Create a function named count vowels that accepts a string and returns the number of 
    vowels in the string.
"""

def CountString(sStr : str)->int :
    # just it present in Vowels string or not
    Vowels = 'aeiouAEIOU'
    Count = 0
    for _ in sStr :
        if _ in Vowels:
            Count +=1

    return Count

sStr = str(input("Enter String to Count Vowels : "))
iRet = CountString(sStr)
print(f"Count Number Of String is : {iRet}")
