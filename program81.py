"""
    Program to Generate Random Numbers from 1 to 20 and append them to the List. 
"""
# importing random
import random

def Append(lLis : list)->list:
    iNo = random.randint(1,20)
    lLis.append(iNo)
    return lLis

Lis = []
def Add():
    Input = str(input("Input ADD to add and End to END :"))
    if( Input == 'ADD') :
        Append(Lis)
        print(Lis)
        # Calling To enter Again Input
        Add()
    else:
        return
    
Add()
