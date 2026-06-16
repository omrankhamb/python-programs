# function
def CalculateTicketPrice(iAge : int)->int :
    # Input Updater
    if iAge < iAge :
        iAge = -iAge 
        
    if iAge >=0 and iAge <= 5 :
        return 0
    elif iAge >= 6 and iAge <= 18 :
        return 500
    elif iAge >= 19 and iAge <= 50 :
        return 900
    else :
        return 400


No = int(input("Enter Number : "))

iRet = CalculateTicketPrice(No)
print(f"Your TicketPrice Will be {iRet} Rupees")

