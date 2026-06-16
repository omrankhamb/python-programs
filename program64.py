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


No = int(input("Enter Number : "))
iremainder = 0
iremainder = No % 2

if iremainder == 0 :
    print("Number is Even")
else :
    print("Number is Odd")
