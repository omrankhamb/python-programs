
# & opreator
def main()->None:
    iMask = 0x80000000
   
    for i in range(1,34):   #Overflow
        print(f"{i} : {hex(iMask)}")
        iMask = iMask >> 1

if __name__ == "__main__":
    main()