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

def CheckEvenOdd(iNo: int) -> str:
    if iNo % 2 == 0 :
        return "Even"
    else :
        return "Odd"
        

No = int(input("Enter Number : "))
print("Number is", CheckEvenOdd(No))
