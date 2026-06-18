def Pattern(n : int) :
    i = 0
    while i <= 11 :
        # for input == 11
        # To print
        #   *   *   *   #   #   #   *   *   *   #   #
        for j in range(3):
            print(f"*\t",end="")
            i +=1
            if i == n:
                break
        if i == n :
            break

        for j in range(3):
            i +=1
            print(f"#\t",end=" ")
            if i == n :
                break

        if i == n :
            break
        


iValue = int(input("Enter Number : "))
Pattern(iValue)