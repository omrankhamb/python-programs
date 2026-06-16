# START
#         Accepet number as No
#         If No is Complrtley divisible by 2
#             by print even 
#         Otherwise 
#             print odd
#     STOP

#     START 
#         Accepet number as No
#         Divide No by 2
#         If remainder is 0
#             then print as Even 
#         otherwise 
#             print as Odd
#     STOP

def CheckEvenOdd(iNo: int) -> int:
    iRemainder = 0
    iRemainder = iNo // 2
    return iRemainder
        

No = int(input("Enter Number : "))

iRet = CheckEvenOdd(No)
if iRet == 0 :
    print("Number is Even")
else:
    print("Number is Odd")
