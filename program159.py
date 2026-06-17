# reverse using recursoin




def ReverseNumber (No : int,rev = 0)->int:
    if(No == 0):
        return rev
    return ReverseNumber(No//10 , rev *10 + No%10)
    

print(ReverseNumber(int(input("Enter Number to reverse : ")))*100)