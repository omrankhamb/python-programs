

# Consider 1 byte
# 1    0    1   1   0   0   0   0
# 0    1    0   0   0   0   0   0
def main()->None:
    iMask = 0xFFFFFFBF
    print(f"Before : {hex(iMask)}")
    print(f"Before : {bin(iMask)}")
    iMask = ~iMask
    print(f"After : {hex(iMask)}")
    print(f"After : {bin(iMask)}")
    
if __name__ == "__main__":
    main()