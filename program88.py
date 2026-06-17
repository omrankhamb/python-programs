"""
    Program to concatenate dictionaries to create a new one. 
"""

# adding two dictionaries
def AddDic(dic : dict,dic2 : dict)-> dict:
    dicTemp = dict()
    dic["Name"] = "Harsh"
    for key,values in dic.items():
        dicTemp[key] = values

    for key,values in dic2.items():
        dicTemp[key] = values

    return dicTemp

dic = {
    "Name": "omprasad",
    "age" : 12,
}

dic2 = {
    "Name2" :"Soham",
    "age2" : 23
}

# call function
dic3 = AddDic(dic,dic2)
print(dic3)
