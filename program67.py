def CheckEvenOdd(iNo: int) -> int:
    iRemainder = 0
    iRemainder = iNo // 2
    return iRemainder
        

No = int(input("Enter Number : "))

iRet = CheckEvenOdd(No)
if iRet == 0 :
    print(f"{No}cNumber is Even")
else:
    print(f"{No}Number is Odd")
