# Class contaning array
# 1       *       3       *       5       *
class PatternX:
    def Display(self,ino : int):
        for i in range(1,ino+1):
            print(f"{(2*i-1)}\t*\t",end="")


aobj= PatternX()
iValue = int(input("Enter Number : "))
aobj.Display(iValue)
del aobj



        