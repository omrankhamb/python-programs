"""
    5 4 3 2 1....
"""

def DisplayReverse(iNo : int):
    for i in range(iNo,0,-1):
        print(i,end = " ")

    
iValue = int(input("Enter Number : "))
iRet = DisplayReverse(iValue)
