# Write a Python program to find the list of words that are longer than n from a given list of words.
n=int(input("enter the no to find loger then n no from given list of words: "))
lst=['python','is','high','programming','language']
for i in lst:
    if len(i)>n:
        print(i,end=' ')