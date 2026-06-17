# Class contaning array
# 1       *       3       *       5       *
class PatternX:
    def Display(self,ino : int):
        iCount = 0
        for i in range(1,ino+1):
            if i % 2 == 0:
                print("*\t",end="")
            else :
                iCount+=1
                print(f"{iCount}\t",end="")


aobj= PatternX()
iValue = int(input("Enter Number : "))
aobj.Display(iValue)
del aobj



        