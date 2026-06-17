# Class contaning array
# 1       *       2       *       3       *       4       *       5       *
class PatternX:
    def Display(self,ino : int):
        for i in range(1,ino+1):
            print(f"{i}\t*\t",end="")


aobj= PatternX()
iValue = int(input("Enter Number : "))
aobj.Display(iValue)
del aobj



        