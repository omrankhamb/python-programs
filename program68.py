def CheckEvenOdd(iNo: int) -> bool:
    iRemainder = 0
    iRemainder = iNo // 2
    if iRemainder == 0 :
        return True
    else :
        return False
    
    
        

No = int(input("Enter Number : "))

iRet = CheckEvenOdd(No)
if iRet == 0 :
    print(f"{No}cNumber is Even")
else:
    print(f"{No}Number is Odd")
