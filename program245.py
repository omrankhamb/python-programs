
def main()->None:
    iMask = 0xFFFFFFFF
    print(f"Before : {hex(iMask)}")
    iMask = ~iMask
    print(f"After : {hex(iMask)}")
    
if __name__ == "__main__":
    main()