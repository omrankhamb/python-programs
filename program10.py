""" Continue and break statement"""

# Continue is used for to skip current iteration
for i in range(1,10,1):
    if i == 2:
        continue
    print(i)

# Break is used for terminate loop 
for i in range(1,10,1):
    if i == 2:
        break
    print(i)