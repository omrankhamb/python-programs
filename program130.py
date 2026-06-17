"""
    0 2 4 6 8 10....
"""

def Display(iNo : int):
    for i in range(0,iNo+1,2):
        print(i,end = " ")

    
iValue = int(input("Enter Number : "))
iRet = Display(iValue)
