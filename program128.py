"""
    1 2 3 4 5 ....
"""

def Display(iNo : int):
    for i in range(1,iNo+1):
        print(i,end = " ")

    
iValue = int(input("Enter Number : "))
iRet = Display(iValue)
