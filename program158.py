# reverse using recursoin



Reverse = 0
def ReverseNumber (No : int)->int:
    if(No == 0):
        return 0
    global Reverse      # tells python to use global variable
    Reverse = Reverse*10 + (No%10)
    ReverseNumber(No//10)
    return Reverse

print(ReverseNumber(123))