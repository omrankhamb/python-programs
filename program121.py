"""
    N-Fibonaci Series

"""

def Fibonaci(ino : int):
    iValue = 0
    iValue2 = 1
    iCount = 0
    while ino != 0 :
        if iCount == 0:
            print(iValue,end = " ")
        elif iCount == 1:
            print(iValue2,end = " ")
        else :
            sum = iValue + iValue2
            print(sum,end =" ")
            iValue = iValue2
            iValue2 = sum
        iCount +=1
        ino = ino-1


iValue = int(input("Enter Number : "))
print("Fibonaci Sequence is :")
Fibonaci(iValue)

