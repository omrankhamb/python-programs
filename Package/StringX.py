class StringX:
    def __init__(self):
        pass

    # Converting List TO String
    def String(self,lis :list)->String:
        str = ""
        for i in lis:
            str += i
        return str

    # Convert the String To Capital
    def UpperX(self,Str : str)->String:
        lis = list(Str)
        for i in range(len(lis)):
            if lis[i] >= 'a' and lis[i] <= 'z':
                lis[i] = chr(ord(lis[i]) - 32)
        return self.String(lis)
    
    # Convert the String To Lower
    def LowerX(self,Str : str)->String:
        lis = list(Str)
        for i in range(len(lis)):
            if lis[i] >= 'A' and lis[i] <= 'Z':
                lis[i] = chr(ord(lis[i]) + 32)
        return self.String(lis)
    
    # Convert The String To Toggle
    def ToggleX(self,Str : str)->String:
        lis = list(Str)
        for i in range(len(lis)):
            if lis[i] >= 'A' and lis[i] <= 'Z':
                lis[i] = chr(ord(lis[i]) + 32)
            elif lis[i] >= 'a' and lis[i] <= 'z':
                lis[i] = chr(ord(lis[i]) - 32)
        return self.String(lis)
    
    # Finding Character present in string or not
    def FindX(self,Str : str,ch : str)->bool:
        for _ in Str:
            if ch == _:
                return True
        return False
    
    # Reversing The String : 
    def ReverseX(self,Str : str)->str:
        iRight = 0
        iLeft = self.LengthX(Str) -1
        lis = list(Str)
        while iRight <= iLeft:
            lis[iRight],lis[iLeft] = lis[iLeft],lis[iRight]
            iRight +=1
            iLeft -=1
        return self.String(lis)
        
    # Finding Length of String
    def LengthX(self,str : str)->int:
        iCnt = 0
        for i in str:
            iCnt += 1
        return iCnt
    

