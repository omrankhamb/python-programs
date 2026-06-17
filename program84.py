"""
    Program to Find all Numbers in a Range which are Perfect Squares and Sum of 
    all Digits in the Number is Less than 10.
"""


import statistics as static

def MeanMedianMode(Lis:list )->int:
    return static.mean(Lis),static.median(Lis),static.mode(Lis)
   

lLis = list(map(int,input("Enter Marks os Ftudent  by Comma Separated Values : ").split(",")))
mean,median,mode = MeanMedianMode(lLis)
print(f"Mean is : {mean}")
print(f"median is : {median}")
print(f"mode is : {mode}")




