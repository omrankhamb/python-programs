"""Program to Put Even and Odd elements in a List into Two Different Lists. Given 
lists are L= [2,19,24,56,77,59,90,62,46]. """

# Entering a element of List
lArray = list(map(int,(input("Enter Elements of list : ").split(','))))


def OddAndEven(lArray:list)->list:
    # Getting Odd in lArray2 
    lArray2 = list(filter(lambda x : x%2 == 0,lArray))

    # Dettin Odd in lArray3
    lArray3 = list(filter(lambda x : x%2 == 1,lArray))
    
    return lArray2,lArray3

lLis1,lLis2= OddAndEven(lArray)
print(f"Even Filter List : {lLis1}")
print(f"Odd Filter List : {lLis2}")