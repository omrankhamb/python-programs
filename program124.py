"""
    .write a function count(word, letter) which takes a word and a letter as arguments 
    and returns the number of occurrences of that letter in the word.
"""

def CountWord(Word : str,letter : str)->int:
    Count = 0
    for i in Word:
        if i == letter:
            Count+=1
    return Count

sStr = str(input("Enter string : "))
char = str(input("Enter word to find : "))

iRet = CountWord(sStr,char)
print(f"Count of word is {iRet}")