"""
    Program to merge two Python dictionaries.
"""
# adding two dictionaries
def AddDic(dic : dict,dic2 : dict)-> dict:
    return dic | dic2 # Adding two dictionaries

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
