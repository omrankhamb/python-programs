def Pattern(n : int) :
    # using Ord of n
    ch = ord('A')
    ch2 = ord('a')
    for i in range(1,n+1):
        if i % 2 == 0:
            print(f"{chr(ch2)}\t",end=" ")
            
        else :
            print(f"{chr(ch)}\t",end=" ")
            
        ch2 +=1
        ch +=1


iValue = int(input("Enter Number : "))
Pattern(iValue)