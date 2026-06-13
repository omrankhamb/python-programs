"""Filter + (lamda)Function"""

c = [1,2,3,4,5,6]
Info = filter(lambda x : x % 2 == 0,c)
print(list(Info))


"""Map + Lambda(Function)"""

Info2 = map(lambda x : x*2 ,c)  
print(list(Info2))


