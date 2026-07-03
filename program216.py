
# & opreator
def main():
    iNo = int(input("Enter Number : "))
    iDigit = 0
    iCount = 0
    while iNo > 0:
        iDigit = iNo % 2
        if iDigit == 1 : 
            iCount+=1
        iNo  = iNo // 2

    print(f"Number of 1's are : ",iCount)


if __name__ == "__main__":
    main()