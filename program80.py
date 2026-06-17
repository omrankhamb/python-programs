"""
    Python program to obtain the marks in computer of some students and find mean median and mode. The marks are given as 84,95,76,54,96,88,91,92,95,75,91,97,80
"""
def MeanMedianMode(Lis:list )->int:
    mean = 0
    median = 0
    mode = 0
    frequency = len(Lis)

    # Mean Logic
    sum = 0
    for i in Lis :
        sum = sum + i

    mean = sum / frequency

    # Median Logic
    Lis.sort()
    iLen = len(Lis)
    if ((iLen % 2) == 0):
        median = Lis[iLen //2 ] + Lis[(iLen //2)+1] 
    else :
        median = Lis[iLen //2+1]

    # Mode 
    dic = {}
    for i in Lis :
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1

    mode = 0
    max = 0
    for Key,Value in dic.items():
        if max < Value :
            max = Value
            mode = Key

    return mean,median,mode
   

lLis = list(map(int,input("Enter Marks os Ftudent  by Comma Separated Values : ").split(",")))
mean,median,mode = MeanMedianMode(lLis)
print(f"Mean is : {mean}")
print(f"median is : {median}")
print(f"mode is : {mode}")


