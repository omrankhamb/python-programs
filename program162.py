def Pattern(n : int) :
    # using Ord of n
    ch = ord('A')
    for i in range(1,n+1):
        if i % 2 == 0:
            print(f"*\t",end=" ")
        else :
            print(f"{chr(ch)}\t",end=" ")
            ch +=1


iValue = int(input("Enter Number : "))
Pattern(iValue)