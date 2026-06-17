"""
    checkPalindrome
"""


class Demo:

    def __init__(self,iNo):
        self.iNo = iNo
        print("Inside Constructor ")

    def palindrome(self):
        iNumber = self.iNo
        iReverse = 0
        while(iNumber != 0):
            iReverse = (iReverse * 10) + (iNumber % 10)
            iNumber = iNumber // 10

        if iReverse == self.iNo :
            return True
        else : 
            return False
        
    def __del__(self):
        print("Inside Destructor")


iNo = int(input("Enter Number : "))
dobj = Demo(iNo)
iret = dobj.palindrome()

if iret :
    print(f"{iNo} is palindrome")
else :
    print(f"{iNo} is not palindrome")


    