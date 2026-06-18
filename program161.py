def Pattern(n : int) :
    # using Ord of n
    ch = ord('a')
    for i in range(1,n+1):
        print(chr(ch),end=" ")
        ch +=1


iValue = int(input("Enter Number : "))
Pattern(iValue)